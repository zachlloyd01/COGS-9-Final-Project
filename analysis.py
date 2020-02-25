import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Data/MinSet.csv') as f:
    plots = csv.DictReader(f, delimiter = ',')
    for row in plots:
        x.append(float(row['speechiness']))
        y.append(float(row['popularity']))

plt.scatter(x,y, label="Speechiness against Popularity!")
plt.xlabel('Speechiness')
plt.ylabel('Popularity')
plt.title('Speechiness against Popularity!')
plt.show()