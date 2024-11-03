import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([80,85,90,95,100,105,110,115,120,125])
# ypoints = np.array([240,250,260,270,280,290,300,310,320,330])
# plt.plot(xpoints,ypoints,'o-.r', ms=20, mec= 'g', mfc='c')
# plt.show()

# font1 = {'family':'serif','color':'blue','size':'20'}
# font2 = {'family':'serif','color':'darkred','size':'15'}


# plt.plot(xpoints,ypoints)
# plt.scatter(xpoints,ypoints)
# plt.title('Sports Watch Data',fontdict=font1)
# plt.xlabel('Average pulse',fontdict=font2)
# plt.ylabel('Calories Burnes',fontdict=font2)
# plt.grid()
# plt.show()

# day one the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y, color='#88c999')



#day two the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x,y, color='hotpink')

# plt.show()

y = np.array([35,25,25,25])
mylabel = ["Apple","Banana","Cherry","Dates"]
plt.pie(y,labels=mylabel)
plt.legend(title="Four Fruits")
plt.show()