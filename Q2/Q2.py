import csv
import matplotlib.pyplot as plt

f1=open('dice_count(1).csv','r',encoding='ANSI')
f2=open('dice_count(2).csv','r',encoding='ANSI')
f3=open('dice_count(3).csv','r',encoding='ANSI')
f4=open('dice_count(4).csv','r',encoding='ANSI')
data1=csv.reader(f1)
data2=csv.reader(f2)
data3=csv.reader(f3)
data4=csv.reader(f4)
header1=next(data1) 
header2=next(data2)
header3=next(data3)
header4=next(data4)

counts1 = {}
counts2 = {}
counts3 = {}
counts4 = {}

for row in data1:
    value, count = map(int, row)
    counts1[value] = count

for row in data2:
    value, count = map(int, row)
    counts2[value] = count

for row in data3:
    value, count = map(int, row)
    counts3[value] = count

for row in data4:
    value, count = map(int, row)
    counts4[value] = count

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].bar(counts1.keys(), counts1.values())
axs[0, 0].set_title('Dice 1')
axs[0, 1].bar(counts2.keys(), counts2.values())
axs[0, 1].set_title('Dice 2')
axs[1, 0].bar(counts3.keys(), counts3.values())
axs[1, 0].set_title('Dice 3')
axs[1, 1].bar(counts4.keys(), counts4.values())
axs[1, 1].set_title('Dice 4')

plt.tight_layout()
plt.show()

f1.close()
f2.close()
f3.close()
f4.close()
