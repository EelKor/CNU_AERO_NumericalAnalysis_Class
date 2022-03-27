# 2022 수치해석 HW2
# 충남대학교 항공우주공학과 이승신(202004142)
# NACA0009 Cp 데이터 
# Ansys Fluent CFD 이용

# #### Simulation Parameters #####
#  Air
#  Density : 1.225 kg/m^3
#  Viscosity: 1.7894E-5
#  Inlet Velocity: 55 m/s
#  Tubulance Intensity: 5%
#  Tubulance Viscosity Ratio: 10


import numpy as np
import matplotlib.pyplot as plt

airfoil_x=[]
airfoil_y=[]
cp_airfoil_x = []
cp_airfoil_y = []

x = np.arange(0.0, 2*np.pi, 0.001)   # sin 함수 그리기 위한 x값 선언

# 에어포일 데이터 불러오기
# TIP 
# 첫 시도에서 그래프 그리는데 선이 뒤죽박죽 되는 현상 발생
# 원인은 Ansys Fluent 으로부터 데이터 추출하는 과정에서
# X크기순으로 정렬 옵션때문에 일어난 일

data=open('Cp_NACA0009.txt','r')   
data.readlines(1)
for ln in data:
    cp_airfoil_x.append(eval(ln.split()[0]))
    cp_airfoil_y.append(eval(ln.split()[1]))
data.close()

airfoil_data = open('NACA0009_fin.txt','r')
airfoil_data.readlines(1)
for ln in airfoil_data:
    airfoil_x.append(eval(ln.split()[0]) * 2)
    airfoil_y.append(eval(ln.split()[1]) * 2)
data.close()

plt.subplot(2,1,1)
plt.plot(cp_airfoil_x, cp_airfoil_y, linewidth = 1)
plt.title('NACA0009 Result of CFD, air, 55 m/s')
plt.xlabel('Postition [m]')
plt.ylabel('Pressure Coefficent')
plt.xlim(0,2)
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(airfoil_x, airfoil_y)
plt.title('NACA0009 Shape')
plt.xlim(0,2)
plt.ylim(-0.4,0.4)
plt.grid(True)
plt.show()
