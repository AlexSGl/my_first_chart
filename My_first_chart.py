'''
Информация взята из источника:
https://pythonru.com/biblioteki/pyplot-uroki
'''


import matplotlib.pyplot as plt
import math
import numpy as np


plt.subplot(211)
plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})  # выражения LaTeX
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.plot([1,2,3,4],[0.2,1,3,5])
plt.legend(['First series','Second series','Third series'], loc=2)

plt.subplot(212)
t = np.arange(0,4,0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t+math.pi/2)
y3 = np.sin(math.pi*t-math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')

plt.show()

plt.savefig('my_first_chart.png')
