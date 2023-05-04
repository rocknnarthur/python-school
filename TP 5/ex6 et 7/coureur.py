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

with open('es_utmb_results_2017.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    with open('utmb_results_2017.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[-1] == "ES":
                writer.writerow(row)