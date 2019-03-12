# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  20:34:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
cv2.kmeans()对数据进行分类

输入参数
1. samples: 应该是np.float32 类型的数据，每个特征应该放在一列。
2. nclusters(K): 聚类的最终数目。
3. criteria: 终止迭代的条件。当条件满足时，算法的迭代终止。它应该是
一个含有3 个成员的元组，它们是（typw，max_iter，epsilon）：
• type 终止的类型：有如下三种选择：
– cv2.TERM_CRITERIA_EPS 只有精确度epsilon 满足是
停止迭代。
– cv2.TERM_CRITERIA_MAX_ITER 当迭代次数超过阈值
时停止迭代。
– cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
上面的任何一个条件满足时停止迭代。
• max_iter 表示最大迭代次数。
• epsilon 精确度阈值。
4. attempts: 使用不同的起始标记来执行算法的次数。算法会返回紧密度
最好的标记。紧密度也会作为输出被返回。
5. flags：用来设置如何选择起始重心。通常我们有两个选择：cv2.KMEANS_PP_CENTERS
和cv2.KMEANS_RANDOM_CENTERS。

输出参数
1. compactness：紧密度，返回每个点到相应重心的距离的平方和。
2. labels：标志数组（与上一节提到的代码相同），每个成员被标记为0，1
等
3. centers：由聚类的中心组成的数组。
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

#假设我们有一组数据，每个数据只有一个特征（1 维）。例如前面的T 恤
#问题，我们只使用人们的身高来决定T 恤的大小。
#y①
x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z = np.hstack((x,y))

z = z.reshape((50,1))
z = np.float32(z)

plt.hist(z,256,[0,256]),plt.show()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)

A = z[labels==0]
B = z[labels==1]

plt.hist(A,256,[0,256],color = 'r')
plt.hist(B,256,[0,256],color = 'b')
plt.hist(centers,32,[0,256],color = 'y')
plt.show()

#②现在把体重加进去，成为一个二维特征的
import numpy as np
import cv2
from matplotlib import pyplot as plt
X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))
# convert to np.float32
Z = np.float32(Z)
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
# Plot the data
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()


#③颜色量化
import numpy as np
import cv2

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\home.jpg'

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\home.jpg')
#**************************???????????**********存在问题
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()


