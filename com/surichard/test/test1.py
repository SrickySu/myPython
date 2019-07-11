# coding=utf-8
'''
Created on 2019年5月7日

@author: su.qingjia
'''
import numpy as np
import pandas as pd
a = np.array([[1,2,3],[4,5,3]], dtype=[('x', np.int64), ('y', np.int32)])
#print a[0][1]['x']

b = pd.Series([2, 3, 4], index=['a', 'b', 'c'])
print b