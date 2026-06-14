'''Write a python program to do line plotting, scatter plotting, Bar chart,
box plot , histogram and pie chart.'''
import matplotlib.pyplot as m
import numpy.random as r
x = [2, 3, 5, 7, 8, 9, 10]
y = [23, 54, 58, 65, 87, 89, 90]
m.plot(x, y, linestyle="-.", color='y', marker='*')
m.xlabel("X-axis")
m.ylabel("Y-axis")
m.title("Line Plot")
m.show()
c = ['b', 'g', 'b', 'g', 'b', 'g', 'b']
m.scatter(x, y, marker='D', color=c, s=50)
m.xlabel("X-axis")
m.ylabel("Y-axis")
m.title("Scatter Plot")
m.show()
m.bar(x, y, width=[0.5, 0.6, 0.7, 0.6, 0.7, 0.8, 0.6], color=c, align="edge")
m.xlabel("X-axis")
m.ylabel("Y-axis")
m.title("Bar Chart")
m.show()
m.boxplot(y, vert=True, sym='mX', widths=0.4, notch=True)
m.xlabel("X-axis")
m.ylabel("Y-axis")
m.title("Box Plot")
m.show()
m.hist(y, 10, range=(0, 100), histtype='stepfilled',
       color='y', rwidth='0.9')
m.xlabel("X-axis")
m.ylabel("Y-axis")
m.title("Histogram")
m.show()
m.pie(y, colors=['r', 'y', 'b', 'g', 'm', 'c', 'k'], labels=['Maths', 'English', 'Science',
      'Social Studies', 'Gujarati', 'Hindi', 'Sanskrit'], shadow=False, counterclock=True, explode=[0.3, 0, 0, 0, 0, 0, 0], autopct='%1.2f%%')
m.title("Result")
m.show()
