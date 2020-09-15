import random
import matplotlib.pyplot as plt
import numpy as np


CITYNUM = 10
MAXDIS = 30

# 初始化城市位置
arrAddress = [[random.randint(1,MAXDIS / 1.5) for _ in range(2)] for __ in range(CITYNUM)]
# arrAddress = [[7, 19], [18, 11], [13, 13], [10, 15], [11, 5], [20, 7], [11, 6], [13, 16], [6, 12], [18, 1]]
arr = []
for i in range(CITYNUM):
    temp = []
    for j in range(CITYNUM):
        if i == j:
            temp.append(0)
        else:
            temp.append(((arrAddress[i][0] - arrAddress[j][0]) ** 2 + (arrAddress[i][1] - arrAddress[j][1]) ** 2) ** 0.5)
    arr.append(temp)

# 贪心算法解决问题
def greedyAlgro(arr , beginId):
    disCnt = 0
    arrCity = [_ for _ in range(CITYNUM)]
    arrCity[0] , arrCity[beginId] = arrCity[beginId] , arrCity[0]
    for i in range(1 , CITYNUM):
        dis = MAXDIS
        tarj = CITYNUM
        for j in range(i , CITYNUM):
            if dis > arr[arrCity[i - 1]][arrCity[j]]:
                tarj = j
                dis = arr[arrCity[i - 1]][arrCity[j]]
        arrCity[i] , arrCity[tarj] = arrCity[tarj] , arrCity[i]
        disCnt += arr[arrCity[i - 1]][arrCity[i]]
    disCnt += arr[arrCity[CITYNUM - 1]][arrCity[0]]       
    return (disCnt , arrCity)


# 暴力遍历解决问题(递归解决全排列问题)
def bruteForceAlgro(arr):
    disCnt = [CITYNUM * MAXDIS]
    tarCityOrder = [0]
    arrCity = [_ for _ in range(CITYNUM)]  
    def core(curTurn , cnt):
        if curTurn == CITYNUM:
            # 完成闭环
            cnt += arr[arrCity[0]][arrCity[curTurn - 1]]
            if disCnt[0] > cnt:
                disCnt[0] = cnt
                tarCityOrder[0] = arrCity.copy()
            return 0
        for i in range(curTurn , CITYNUM):
            if i != curTurn:
                arrCity[i] , arrCity[curTurn] = arrCity[curTurn] , arrCity[i]
            if curTurn == 0:
                core(curTurn + 1 , 0)
            else:
                core(curTurn + 1 , cnt + arr[arrCity[curTurn]][arrCity[curTurn - 1]])           
    core(0 , 0)
    return (disCnt[0] , tarCityOrder[0])

a = [greedyAlgro(arr , _) for _ in range(CITYNUM)]
b = bruteForceAlgro(arr)


# 得到画图坐标点
a_arr = [[[],[]] for _ in range(CITYNUM)]
b_arr = [[],[]]
for i in range(CITYNUM):
    b_arr[0].append(arrAddress[b[1][i]][0])
    b_arr[1].append(arrAddress[b[1][i]][1])
    for j in range(CITYNUM):
        a_arr[i][0].append(arrAddress[a[i][1][j]][0])
        a_arr[i][1].append(arrAddress[a[i][1][j]][1])
    else:
        a_arr[i][0].append(arrAddress[a[i][1][0]][0])
        a_arr[i][1].append(arrAddress[a[i][1][0]][1])
else:
    b_arr[0].append(arrAddress[b[1][0]][0])
    b_arr[1].append(arrAddress[b[1][0]][1])

# 画出坐标图，画图默认是10个城市
fig , axarr = plt.subplots(3 , 4 , figsize = (20 , 14))
plt.suptitle('The Greedy and BruteForce of TSP')
plt.subplots_adjust(wspace = 0.5 , hspace = 0.5)
for i in range(CITYNUM):
    axarr[i // 4][i % 4].scatter(a_arr[i][0] , a_arr[i][1] , marker = "o" , color = 'r')
    axarr[i // 4][i % 4].plot(a_arr[i][0] , a_arr[i][1])
    axarr[i // 4][i % 4].axis([0 , int(MAXDIS / 1.414) , 0 , int(MAXDIS / 1.414)])
    axarr[i // 4][i % 4].scatter(a_arr[i][0][0] , a_arr[i][1][0] , marker = "s" , color = 'k')
    axarr[i // 4][i % 4].set_title('{}{}'.format('Greedy_dis = \n' , a[i][0]))

axarr[2][2].plot(b_arr[0] , b_arr[1])
axarr[2][2].scatter(b_arr[0] , b_arr[1], marker = "o" , color = 'r')
axarr[2][2].axis([0 , int(MAXDIS / 1.414) , 0 , int(MAXDIS / 1.414)])
axarr[2][2].set_title('{}{}'.format('BF_dis = ' , b[0]))

# 获得城市的分布，用于做PPT
# axarr[2][2].scatter(b_arr[0] , b_arr[1], marker = "o" , color = 'r')
# axarr[2][2].axis([0 , int(MAXDIS / 1.414) , 0 , int(MAXDIS / 1.414)])
# axarr[2][2].set_title('The position of cities:')

axarr[2][3].axis('off')
axarr[2][3].text(0.2 , 0.5 ,
                '{}{}'.format('quality = \n\naverage(Greedy) / BF =\n\n ' , sum(map(lambda x: x[0],a)) / CITYNUM / b[0]),
                # s
                horizontalalignment = 'center',
                verticalalignment = 'center',)
                
plt.savefig('anwser.png')
plt.show()

