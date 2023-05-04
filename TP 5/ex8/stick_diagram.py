import matplotlib.pyplot as plt
import csv

with open('utmb_results_2017.csv', encoding="utf8") as f:
    reader = csv.reader(f)

    d = {}
    for row in reader:
        print(row)
        
        if row[3] not in d:
            if row[3] != "Cat.":
                d[row[3]] = 1
        else:
            d[row[3]] += 1

    print(d)

fig = plt.figure()

x = []
height = []
width = 1.0

for key, value in d.items():
    x.append(key)
    height.append(value)

plt.bar(x, height, width, color='b' )

plt.savefig('utmb_diagram.png')
plt.show()