import fnmatch
#1 과목명 분류
testDict = {'subject1':'오픈소스소프트웨어', 'time1':'목(1,2)/금(3)', 'num1':'1',
 'subject2':'프로그래밍입문2', 'time2':'목(1,2,3,4)', 'num2':'1',
 'subject3':'프입1', 'time3':'목(3,4)', 'num3':'2',
 'subject4':'지식재산권', 'time4':'목(2,3,4)/수(4,5,6)', 'num4':'3',
 'avoid_time':'1교시', '점심시간':'예', '공강날짜':'금'}


def subject_info():
    subject_list = []
    for i in list(testDict.keys()):
        if fnmatch.fnmatch(i,'subject*'):
            subject_list.append(testDict[i])
    # print(subject_list) #['오픈소스소프트웨어', '프로그래밍입문2']

    #2. 수업시간 분류
    time_list = []
    for i in list(testDict.keys()):
        if fnmatch.fnmatch(i, 'time*'):
            time_list.append(testDict[i])
    # print(time_list) #['목(1,2,3,4)', '월(5,6,7)/화(4,5)']

    #2-1. 수업시간 리스트로 정리 '목(1,2,3,4)' -> [목,[1,2,3,4]]]
    class_list=[]
    for time in time_list:
        if '/' in time:
            time = time.split('/')  #['월(5,6,7)','화(4,5)']
            class_list.append([[time[0][0], time[0][2:len(time[0])-1].split(',')] ,[time[1][0], time[1][2:len(time[1])-1].split(',')]])
            #[['월', ['5', '6', '7']], ['화', ['4', '5']]]
        else:
            class_list.append([time[0], time[2:len(time)-1].split(',')]) #['목', ['1', '2', '3', '4']]

    #3. 순위 분류
    num_list = []
    for i in list(testDict.keys()):
        if fnmatch.fnmatch(i, 'num*'):
            num_list.append(int(testDict[i]))
    # print(num_list) #[1, 2]

    result_list=[]
    for i in range(len(subject_list)):
        result_list.append([subject_list[i],class_list[i],num_list[i]])
    
    return result_list

    #['오픈소스소프트웨어', ['목', ['1', '2', '3', '4']], 1]
    #['프로그래밍입문2', [['월', ['5', '6', '7']], ['화', ['4', '5']]], 2]
# print(subject_info())

# for idx, info in enumerate(subject_info()):
#     print(idx, info)
# 0 ['오픈소스소프트웨어', ['목', ['1', '2', '3', '4']], 1]
# 1 ['프로그래밍입문2', [['월', ['5', '6', '7']], ['화', ['4', '5']]], 2]

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
        select2 = testDict['공강날짜']
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
        if info[2] == 1:
            score += 10000
        elif info[2] == 2:
            score += 5
        else:
            pass

        info.append(score)
        result_list.append(info)
    return result_list

# print(step1())
#[['오픈소스소프트웨어', ['목', ['1', '2', '3', '4']], 1, 10007], ['프로그래밍입문2', [['월', ['5', '6', '7']], ['목', ['4', '5']]], 2, 13], ['기계학습', [['금', ['4']], ['월', ['5', '6', '7']]], 1, 10001]]

def compare_list(list_1, list_2):
    for i in list_1:
        if i in list_2:
            return True
        else:
            pass

# print(compare_list(step1()[0][1][1],step1()[2][1][1]))
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
# print(overlap_detect())

def non_overlap():
    non_overlap = []
    a, b = overlap_detect()
    c=a+b

    for x in step1():
        if x not in c:
            non_overlap.append(x)

    return non_overlap

def result_process():
    overlap_list, _ = overlap_detect()
    result_list = overlap_list + non_overlap()

    if (len(result_list) > 8):
        return(result_list[:8])
    else:
        return result_list

print(result_process())

# result_list 에서 겹치는 요소 제거
def delete_elements():
    new_list = []
    for v in result_process():
        if v not in new_list:
            new_list.append(v)
    return new_list

print(delete_elements())

# score 중심으로 sort!
def sorted_list():
    sort_list = sorted(delete_elements(),key=lambda x: x[3], reverse=True)
    return sort_list

