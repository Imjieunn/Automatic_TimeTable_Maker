import fnmatch
#1 과목명 분류
testDict = {'subject1':'오픈소스소프트웨어', 'time1':'목(1,2,3,4)', 'num1':'1', 'subject2':'프로그래밍입문2', 'time2':'월(5,6,7)/목(4,5)', 'num2':'2', 'subject3':'기계학습', 'time3':'금(4)/월(5,6,7)', 'num3':'1',
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

# 4단계 -> 입력한 교과목 중 시간대가 겹친다면?! -> 겹치는 과목 중에서 score이 높은거 선택 & 다른 하나는 버리기
def overlap_detect():
    overlap_list = []
    for i in range(len(step1())-1):
        for j in range(i+1, len(step1())):
            if len(step1()[i][1][0])==2:
                if(len(step1()[j][1][0]))==2:
                    if ((step1()[i][1][0][0] == step1()[j][1][0][0]) and (compare_list(step1()[i][1][0][1], step1()[j][1][0][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                    elif ((step1()[i][1][1][0] == step1()[j][1][0][0]) and (compare_list(step1()[i][1][1][1], step1()[j][1][0][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])    
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                    elif ((step1()[i][1][0][0] == step1()[j][1][1][0]) and (compare_list(step1()[i][1][0][1], step1()[j][1][1][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]]) 
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                    elif ((step1()[i][1][1][0] == step1()[j][1][1][0]) and (compare_list(step1()[i][1][1][1], step1()[j][1][1][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]]) 
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                else:
                    if((step1()[i][1][0][0] == step1()[j][1][0]) and (compare_list(step1()[i][1][0][1],step1()[j][1][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                    elif((step1()[i][1][1][0] == step1()[j][1][0]) and (compare_list(step1()[i][1][1][1],step1()[j][1][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])
                        else:
                            overlap_list.append([step1()[j],step1()[i]])                      
            else:
                if len(step1()[j][1][0])==2:
                    if((step1()[i][1][0] == step1()[j][1][0][0]) and (compare_list(step1()[i][1][1], step1()[j][1][0][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                    elif((step1()[i][1][0] == step1()[j][1][1][0]) and (compare_list(step1()[i][1][1], step1()[j][1][1][1])==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
                else:
                    if((step1()[i][1][0] == step1()[j][1][0]) and (compare_list(step1[i][1][1], step1([j][1][1]))==True)):
                        if(step1()[i][3] >= step1()[j][3]):
                            overlap_list.append([step1()[i],step1()[j]])
                        else:
                            overlap_list.append([step1()[j],step1()[i]])
    return overlap_list
