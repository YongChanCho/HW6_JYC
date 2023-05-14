import csv
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
f=open('Q4.csv')
data=csv.reader(f)
next(data)
next(data)

morning_boarding={}
morning_alighting={}
morning_total={}

for row in data:
    for i in range(10,14):
        row[i]=int(row[i])
    morning_boarding[row[1]+" "+row[3]] = morning_boarding.get(row[3], 0) + (row[10] + row[12])
    morning_alighting[row[1]+" "+row[3]] = morning_alighting.get(row[3], 0) + (row[11] + row[13])
    morning_total[row[1]+" "+row[3]] = morning_total.get(row[3], 0) + (row[10] + row[11] + row[12] + row[13])

morning_boarding = sorted(morning_boarding.items(), key=lambda x: x[1], reverse=True)[:30]
morning_alighting = sorted(morning_alighting.items(), key=lambda x: x[1], reverse=True)[:30]
morning_total = sorted(morning_total.items(), key=lambda x: x[1], reverse=True)[:30]

morning_boarding_names, morning_boarding_counts = zip(*morning_boarding)
morning_alighting_names, morning_alighting_counts = zip(*morning_alighting)
morning_total_names, morning_total_counts = zip(*morning_total)

plt.bar(morning_boarding_names, morning_boarding_counts, color='blue')
plt.title('출근 시간에 승차한 인원이 가장 많은 지하철역 상위 30개')
plt.xticks(rotation=90)
plt.show()

plt.bar(morning_alighting_names, morning_alighting_counts, color='red')
plt.title('출근 시간에 하차한 인원이 가장 많은 지하철역 상위 30개')
plt.xticks(rotation=90)
plt.show()

plt.bar(morning_total_names, morning_total_counts, color='pink')
plt.title('출근 시간에 승하차한 인원이 가장 많은 지하철역 상위 30개')
plt.xticks(rotation=90)
plt.show()
