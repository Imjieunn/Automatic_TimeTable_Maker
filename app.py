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

        # 조건 선택에 따른 분류를 위한 입력한 과목별 시간 리스트 따로 생성
        time_list = []
        for i in list(testDict.keys()):
            if fnmatch.fnmatch(i, 'time*'):
                time_list.append(testDict[i])

    # 시간리스트 전처리 과정
    def time_scaling():
        # time_list = ['월(1-3)', '목(2-3)/수(2)']

        # # 원하는 결괏값 = [[0,1,3],[[3,2,3],[2,2]]]

        array_index_list = []

        for time in time_list:
            if '/' in time:
                time = time.split('/') #['목(2-4)', '수(5)']

                if time[0][0]  == '월':
                    array_index1 = 0
                    if time[1][0] == '월':
                        array_index1_1 = 0
                    elif time[1][0] == '화':
                        array_index1_1 = 1
                    elif time[1][0] == '수':
                        array_index1_1 = 2
                    elif time[1][0] == '목':
                        array_index1_1 = 3
                    else:
                        array_index1_1 = 4      

                elif time[0][0] == '화':
                    array_index1 = 1
                    if time[1][0] == '월':
                        array_index1_1 = 0
                    elif time[1][0] == '화':
                        array_index1_1 = 1
                    elif time[1][0] == '수':
                        array_index1_1 = 2
                    elif time[1][0] == '목':
                        array_index1_1 = 3
                    else:
                        array_index1_1 = 4    

                elif time[0][0] == '수':
                    array_index1 = 2
                    if time[1][0] == '월':
                        array_index1_1 = 0
                    elif time[1][0] == '화':
                        array_index1_1 = 1
                    elif time[1][0] == '수':
                        array_index1_1 = 2
                    elif time[1][0] == '목':
                        array_index1_1 = 3
                    else:
                        array_index1_1 = 4    

                elif time[0][0] == '목':
                    array_index1 = 3
                    if time[1][0] == '월':
                        array_index1_1 = 0
                    elif time[1][0] == '화':
                        array_index1_1 = 1
                    elif time[1][0] == '수':
                        array_index1_1 = 2
                    elif time[1][0] == '목':
                        array_index1_1 = 3
                    else:
                        array_index1_1 = 4    

                else:
                    array_index1 = 4
                    if time[1][0] == '월':
                        array_index1_1 = 0
                    elif time[1][0] == '화':
                        array_index1_1 = 1
                    elif time[1][0] == '수':
                        array_index1_1 = 2
                    elif time[1][0] == '목':
                        array_index1_1 = 3
                    else:
                        array_index1_1 = 4          
                
                if len(time[0])>4:
                    for i in range(1,10):
                        if time[0][2] == str(i):
                            array_index2 = i          
                    for i in range(1,10):
                        if time[0][4] == str(i):
                            array_index3 = i                
                else:
                    for i in range(1,10):
                        if time[0][2] == str(i):
                            array_index2 = i

                if len(time[1])>4:
                    for i in range(1,10):
                        if time[1][2] == str(i):
                            array_index2_1 = i          
                    for i in range(1,10):
                        if time[1][4] == str(i):
                            array_index3_1 = i
                    if len(time[0])>4: 
                        array_index_list.append([[array_index1, array_index2, array_index3], [array_index1_1,array_index2_1,array_index3_1]])     
                    else:
                        array_index_list.append([[array_index1, array_index2], [array_index1_1,array_index2_1,array_index3_1]])                        
                else:
                    for i in range(1,10):
                        if time[1][2] == str(i):
                            array_index2_1 = i
                    if len(time[0])>4: 
                        array_index_list.append([[array_index1, array_index2, array_index3], [array_index1_1,array_index2_1]])     
                    else:
                        array_index_list.append([[array_index1, array_index2], [array_index1_1,array_index2_1]])   

            else:
                if time[0] == '월':
                    array_index1 = 0
                    # array_index_list.append(array_index1)
                elif time[0] == '화':
                    array_index1 = 1
                    # array_index_list.append(array_index1)
                elif time[0] == '수':
                    array_index1 = 2
                    # array_index_list.append(array_index1)
                elif time[0] == '목':
                    array_index1 = 3
                    # array_index_list.append(array_index1)
                else:
                    array_index1 = 4      
                    # array_index_list.append(array_index1) 
                
                if len(time)>4:
                    for i in range(1,10):
                        if time[2] == str(i):
                            array_index2 = i          
                    for i in range(1,10):
                        if time[4] == str(i):
                            array_index3 = i  
                    array_index_list.append([array_index1, array_index2, array_index3])               

                else:
                    for i in range(1,10):
                        if time[2] == str(i):
                            array_index2 = i
                    array_index_list.append([array_index1, array_index2])

        return array_index_list

    # array로 scaling된 시간 data 2차원 metrics에 넣기(?? 필요한가잉 ??)
    
    # 입력 과목 수업시간 충돌시 처리 방법
    

    # 조건에 따른 score 배부


    # score에 따른 과목 sort(내림차순)

        
    # 상위 3개의 조합 top3_list 생성 -> result_list = top3_list
    return render_template("result.html", result_dict = testDict)

if __name__ == '__main__':
    app.run(debug=True)
