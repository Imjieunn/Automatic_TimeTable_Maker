from flask import Flask, render_template, request, redirect, url_for
import fnmatch

app = Flask(__name__)

@app.route('/') # 기본적 page -> main page
def main():
    # 원하는 파이썬 코드 작성 -> 해당 html로 변수 넘겨주기
    return render_template("main.html")

# @app.route('/login.html')
# def login():
#     # id = request.args.get("id")
#     # pw = request.args.get("pw")
#     import crawling
#     return render_template("login.html")


@app.route('/select')
def select():
    return render_template("select.html")

# @app.route('/subject.html')
# def subject():
#     return render_template("subject.html")

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        testDict = request.form.to_dict(flat=True)

        def subject_info():
            subject_list = []
            for i in list(testDict.keys()):
                if fnmatch.fnmatch(i,'subject*'):
                    if (testDict[i] != ''):
                        subject_list.append(testDict[i])

            #2. 수업시간 분류
            time_list = []
            for i in list(testDict.keys()):
                if fnmatch.fnmatch(i, 'time*'):
                    if (testDict[i] != ''):
                        time_list.append(testDict[i])

            # 2-1. 수업시간 리스트로 정리 '목(1,2,3,4)' -> [목,[1,2,3,4]]]
            class_list=[]
            for time in time_list:
                if '/' in time:
                    time = time.split('/')  
                    class_list.append([[time[0][0], time[0][2:len(time[0])-1].split(',')] ,[time[1][0], time[1][2:len(time[1])-1].split(',')]])
                else:
                    class_list.append([time[0], time[2:len(time)-1].split(',')]) 

            #3. 순위 분류
            num_list = []
            for i in list(testDict.keys()):
                if fnmatch.fnmatch(i, 'num*'):
                    if (testDict[i] != ''):
                        num_list.append(testDict[i])


            result_list=[]
            for i in range(len(subject_list)):
                result_list.append([subject_list[i], class_list[i], num_list[i]])
            
            return result_list        

        #이 과정에서 사용하는 조건(3개 -> avoid_time, 점심시간, 공강날짜)
        def step1():
            result_list = []
            for info in subject_info():
                score = 0

                # 피하고 싶은 교시
                select = testDict['avoid_time']

                if len(info[1][0])==2:
                    if select[0] in (info[1][0][1] or info[1][1][1]):
                        pass
                    else:
                        score+=10
                else:
                    if select[0] in info[1][1]:
                        pass
                    else:
                        score += 10
                
                # 점심시간
                if testDict['점심시간'] == '예':
                    if len(info[1][0]) == 2:
                        for i in range(len(info[1][0][1])):
                            if(info[1][0][1][i]) in ('4','5','6'):
                                score-=3
                        for i in range(len(info[1][1][1])):
                            if(info[1][1][1][i]) in ('4','5','6'):
                                score-=3

                    else:
                        for i in range(len(info[1][1])):
                            if(info[1][1][i]) in ('4','5','6'):
                                score-=3


                # 공강날짜
                select2 = testDict['공강']
                if len(info[1][0])==2:
                    if select2[0] in (info[1][0][0] or info[1][1][0]):
                        pass
                    else:
                        score+=10
                else:
                    if select2[0] in info[1][0]:
                        pass
                    else:
                        score += 10

                # 과목 우선순위(1,2,3)
                if info[2] == '1':
                    score += 10000
                elif info[2] == '2':
                    score += 5
                else:
                    pass

                info.append(score)
                result_list.append(info)
            return result_list

        def compare_list(list_1, list_2):
            for i in list_1:
                if i in list_2:
                    return True
                else:
                    pass

        # 4단계 -> 입력한 교과목 중 시간대가 겹친다면?! -> 겹치는 과목 중에서 score이 높은거 선택 & 다른 하나는 버리기
        def overlap_detect():
            overlap_list = []
            minor_list = []
            for i in range(len(step1())-1):
                for j in range(i+1, len(step1())):
                    if len(step1()[i][1][0])==2:
                        if(len(step1()[j][1][0]))==2:
                            if ((step1()[i][1][0][0] == step1()[j][1][0][0]) and (compare_list(step1()[i][1][0][1], step1()[j][1][0][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                            elif ((step1()[i][1][1][0] == step1()[j][1][0][0]) and (compare_list(step1()[i][1][1][1], step1()[j][1][0][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])  
                                    minor_list.append(step1()[j])  
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                            elif ((step1()[i][1][0][0] == step1()[j][1][1][0]) and (compare_list(step1()[i][1][0][1], step1()[j][1][1][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i]) 
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                            elif ((step1()[i][1][1][0] == step1()[j][1][1][0]) and (compare_list(step1()[i][1][1][1], step1()[j][1][1][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i]) 
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                        else:
                            if((step1()[i][1][0][0] == step1()[j][1][0]) and (compare_list(step1()[i][1][0][1],step1()[j][1][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                            elif((step1()[i][1][1][0] == step1()[j][1][0]) and (compare_list(step1()[i][1][1][1],step1()[j][1][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])    
                                    minor_list.append(step1()[i])             
                    else:
                        if len(step1()[j][1][0])==2:
                            if((step1()[i][1][0] == step1()[j][1][0][0]) and (compare_list(step1()[i][1][1], step1()[j][1][0][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                            elif((step1()[i][1][0] == step1()[j][1][1][0]) and (compare_list(step1()[i][1][1], step1()[j][1][1][1])==True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
                        ## 오류 포인트
                        else:
                            if((step1()[i][1][0] == step1()[j][1][0]) and (compare_list(step1()[i][1][1], step1()[j][1][1]) == True)):
                                if(step1()[i][3] >= step1()[j][3]):
                                    overlap_list.append(step1()[i])
                                    minor_list.append(step1()[j])
                                else:
                                    overlap_list.append(step1()[j])
                                    minor_list.append(step1()[i])
            return overlap_list, minor_list

        def non_overlap():
            non_overlap = []
            a, b = overlap_detect()
            c=a+b

            for x in step1():
                if x not in c:
                    non_overlap.append(x)

            return non_overlap

        def result_process():
            overlap_list, minor_list = overlap_detect()

            # overlap_list에서 겹치는 요소 제거
            new_overlap_list = []
            for v in overlap_list:
                if v not in new_overlap_list:
                    new_overlap_list.append(v)

            # minor_list에 있는데 overlap_list에 있는 요소 제거
            overlap_result_list = []
            for element in new_overlap_list:
                if element not in minor_list:
                    overlap_result_list.append(element)
            
            result_list = overlap_result_list + non_overlap()
            if (len(result_list) > 8):
                return(result_list[:8])
            else:
                return result_list

        # score 중심으로 sort!
        def sorted_list():
            sort_list = sorted(result_process(),key=lambda x: x[3], reverse=True)
            return sort_list
    return render_template("result.html", result = sorted_list())

if __name__ == '__main__':
    app.run(debug=True)
