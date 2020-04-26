#EverythingWithPython #womenintech #100DaysOfCode 
#Let's make a pie pie chart!
import matplotlib.pyplot as plt

labels = 'Blueberry', 'Apple', 'Pear', 'Cherry'
sizes = [20, 30, 10, 40]
explode = (0, 0, 0, 0.1)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, startangle=90)
ax.axis('equal')

plt.show()
