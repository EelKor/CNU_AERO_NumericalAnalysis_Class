import numpy as np
import matplotlib.pyplot as plt

# 회전 행렬 함수 - 라디안값 각도와 열벡터를 인자로 받음
def ROT(theta, array):

    result = np.array([(np.cos(theta), -np.sin(theta)), (np.sin(theta), np.cos(theta))]) @ array    #행렬곱셈
    return result

airfoil_x=[]
airfoil_y=[]
airfoil_mat = []

x = np.arange(0.0, 2*np.pi, 0.001)   # sin 함수 그리기 위한 x값 선언

# 에어포일 데이터 불러오기
data=open('NACA0009_fin.txt','r')   
data.readlines(1)
for ln in data:
    airfoil_x.append(eval(ln.split()[0]))
    airfoil_y.append(eval(ln.split()[1]))
data.close()

# 에어포일 데이터를 파이썬 리스트 형식에서 넘파이 행렬 형식으로 형변환
for i in range(0, len(airfoil_x)):
    airfoil_mat.append(np.array([airfoil_x[i]-0.5, airfoil_y[i]]))

# airfoil_mat = 리스트환
# airfoil_mat 안의 원소는 np.array형식
# airfoil_mat = [np.array, np.array ... ]

rot_airfoil_x = []
rot_airfoil_y = []
result_x = []
result_y = []
testcase = [0, 0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2, 4.8, 5.2]    # 에어 포일을 그리는 기준 x 좌표

for case in testcase: # 에어포일 기준좌표 불러오기
    angle = np.arctan(np.cos(case)) # 해당 x좌표 에서 sin 함수에 접하는 직선이 X축과 이루는 각도 구하기
    for i in range(0,len(airfoil_mat)):
        tmp = ROT(angle, airfoil_mat[i])    # 에어포일 좌표값을 위에서 구한 각도 만큼 회전
        tmp.tolist()
        rot_airfoil_x.append(tmp[0] + case) # 회전시킨 에어포일의 좌표값을 X방향으로 평행이동
        rot_airfoil_y.append(tmp[1] + np.sin(case)) # 회전 시킨 에어포일의 좌표값을 Y방향으로 평행이동

    result_x.append(rot_airfoil_x)      # 계산 완료된 에어포일의 X좌표값의 집합을 저장
    result_y.append(rot_airfoil_y)      # 계산 완료된 에어포일의 Y좌표값의 집합을 저장

for i in range(0, len(result_x)):
    plt.scatter(result_x[i], result_y[i], s = 0.5)
    
plt.plot(x, np.sin(x), color='red')
plt.grid(True)
plt.show()



    






