import csv
import matplotlib.pyplot as plt

f1=open('Q1(서울).csv','r',encoding='ANSI')
f2=open('Q1(부산).csv','r',encoding='ANSI')
f3=open('Q1(제주).csv','r',encoding='ANSI')
f4=open('Q1(대전).csv','r',encoding='ANSI')
f5=open('Q1(전국).csv','r',encoding='ANSI')
data1=csv.reader(f1)
data2=csv.reader(f2)
data3=csv.reader(f3)
data4=csv.reader(f4)
data5=csv.reader(f5)
header1=next(data1)
header2=next(data2)
header3=next(data3)
header4=next(data4)
header5=next(data5)

seoul_x_data = []
seoul_y_data = []
for row in data1:
    seoul_x_data.append(row[0])  
    seoul_y_data.append(float(row[2]))  

busan_x_data = []
busan_y_data = []
for row in data2:
    busan_x_data.append(row[0])
    busan_y_data.append(float(row[2]))

jeju_x_data = []
jeju_y_data = []
for row in data3:
    jeju_x_data.append(row[0])
    jeju_y_data.append(float(row[2])) 

daejeon_x_data = []
daejeon_y_data = []
for row in data4:
    daejeon_x_data.append(row[0])
    daejeon_y_data.append(float(row[2]))

all_x_data = []
all_y_data = []
for row in data5:
    all_x_data.append(row[0])
    all_y_data.append(float(row[2]))  

plt.plot(seoul_x_data, seoul_y_data, label='Seoul')  
plt.plot(busan_x_data, busan_y_data, label='Busan')
plt.plot(jeju_x_data, jeju_y_data, label='Jeju')
plt.plot(daejeon_x_data, daejeon_y_data, label='Daejeon')
plt.plot(all_x_data, all_y_data, label='All')
plt.title("2022 temperature by region")
plt.legend()  
plt.xticks(rotation=90)
plt.show()

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()