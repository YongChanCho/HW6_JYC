import csv
import matplotlib.pyplot as plt

f1=open('Q3(2019).csv','r',encoding='ANSI')
f2=open('Q3(2020).csv','r',encoding='ANSI')
f3=open('Q3(2021).csv','r',encoding='ANSI')
f4=open('Q3(2022).csv','r',encoding='ANSI')
data1=csv.reader(f1)
data2=csv.reader(f2)
data3=csv.reader(f3)
data4=csv.reader(f4)
header1=next(data1) 
data1 = next(data1)
header2=next(data2)
data2 = next(data2)
header3=next(data3)
data3 = next(data3)
header4=next(data4)
data4 = next(data4)

year=["2019","2020","2021","2022"]
male_pop=[int(data1[3]),int(data2[3]),int(data3[3]),int(data4[3])]
female_pop=[int(data1[4]),int(data2[4]),int(data3[4]),int(data4[4])]

plt.plot(year,male_pop,'r.',label="Male")
plt.plot(year,female_pop,'g.',label="Female")
plt.title("Population of Jeju Island by Gender")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.show()

f1.close()
f2.close()
f3.close()
f4.close()
