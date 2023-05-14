import matplotlib.pyplot as plt
import random
import csv

dice_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100000):
    dice = random.randint(1, 6)
    dice_count[dice] += 1

with open('dice_count(4).csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['주사위 숫자', '횟수'])
    for dice_number, count in dice_count.items():
        writer.writerow([dice_number, count])