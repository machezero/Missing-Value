import numpy as np
import matplotlib.pyplot as plt
import array
from numpy.linalg import inv

data = np.array([[1, 1, 1, 0, 3, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                 [1, 1, 1, 0, 3, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2],
                 [1, 1, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                 [1, 1, 2, 0, 3, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                 [1, 1, 2, 0, 3, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                 [1, 1, 2, 0, 3, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2],
                 [1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2],
                 [1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                 [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2],
                 [1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2],
                 [1, 2, 1, 1, 3, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2],
                 [1, 2, 1, 1, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2],
                 [1, 2, 1, 1, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                 [1, 2, 1, 1, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                 [1, 2, 1, 1, 3, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                 [1, 2, 1, 1, 0, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2],
                 [1, 2, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2],
                 [1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2],
                 [1, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2],
                 [1, 2, 1, 2, 3, 2, 0, 2, 2, 2, 2, 2, 0, 2, 1, 2, 1, 2]])

def showData(data):
    print('This is data.')
    print(data)
    print('\n')

def find_missing(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i][:])):
            if (data[i][j] == 0):
                count = count + 1
    print('There are', count, 'missing data.')


def find_index_missing(data):
    for i in range(len(data)):
        for j in range(len(data[i][:])):
            if (data[i][j] == 0):
                print('row =', i, 'colum =', j)
    print('\n')


def DriectMethod_Linear(data):
    n = 0
    for i in range(len(data)):
        for j in range(len(data[i][:])):
          if (i == 0):                          #first Line
              if(data[i][j] == 0):
                  for k in range(len(data)):
                    if (data[i][j] == 0):
                        n = n + 1
                        data[i][j] = data[i + n][j]
                    else :
                        #print(data[i], n)
                        break
          if(i > 0 and i < len(data)-1):
              if(data[i][j] == 0):
                 #print('line',i,data[i-1],'/',data[i+1])
                  #print('colum',j,data[i-1][j],'/',data[i+1][j])
                  b1 = i-1
                  b2 = i+1
                  c1 = data[i-1][j]
                  c2 = data[i+1][j]
                  #print('b1',b1,'c1',c1,'b2',b2,'c2',c2,'\n')
                  x = np.matrix([[1,b1],[1,b2]])
                  y = np.matrix([[c1],[c2]])
                  #print('x',x,'\n','y',y)
                  a = (inv(x)*y)
                  #print('inA',a)
                  a0 = a[0]
                  a1 = a[1]
                  t = i
                  ans = a0 + a1 * i
                  if(ans < 1):
                      ans = 1
                  # print(a0, a1)
                  # print('Ans =', ans ,'\n')
                  data[i][j] = ans
          if(i == len(data)-1):                     #last line
              if (data[i][j] == 0):
                  for k in range(len(data)):
                      if (data[i][j] == 0):
                          n = n + 1
                          data[i][j] = data[i - n][j]
                      else:
                          # print(data[i], n)
                          break
    print('This is new data by Driect Method Linear Interpolation.')
    print(data,'\n')


def DriectMethod_Quadratic(data):
    n = 0
    for i in range(len(data)):
        for j in range(len(data[i][:])):
            if (i == 0):                                # first Line
                if (data[i][j] == 0):
                    for k in range(len(data)):
                        if (data[i][j] == 0):
                            n = n + 1
                            data[i][j] = data[i + n][j]
                        else:
                            # print(data[i], n)
                            break
            if (i > 0 and i < len(data) - 1):
                if (data[i][j] == 0):
                    # print('line',i,data[i-1],'/',data[i+1])
                    # print('colum',j,data[i-1][j],'/',data[i+1][j])
                    b1 = i - 1
                    b2 = i + 1
                    b3 = i + 2
                    c1 = data[i - 1][j]
                    c2 = data[i + 1][j]
                    c3 = data[i + 2][j]
                    # print('b1',b1,'c1',c1,'b2',b2,'c2',c2,'\n')
                    x = np.matrix([[1,b1,b1**2],[1,b2,b2**2],[1,b3,b3**2]])
                    y = np.matrix([[c1], [c2],[c3]])
                    # print('x',x,'\n','y',y)
                    a = (inv(x) * y)
                    # print('inA',a)
                    a0 = a[0]
                    a1 = a[1]
                    a2 = a[2]
                    t = i
                    ans = a0 + (a1 * i) + (a2 * i**2)
                    if (ans < 1):
                        ans = 1
                    # print(a0, a1)
                    # print('Ans =', ans ,'\n')
                    data[i][j] = ans
            if (i == len(data) - 1):                      #last line
                if (data[i][j] == 0):
                    for k in range(len(data)):
                        if (data[i][j] == 0):
                            n = n + 1
                            data[i][j] = data[i - n][j]
                        else:
                            # print(data[i], n)
                            break
    print('This is new data by Driect Method Quadratic Interpolation.')
    print(data)


showData(data)
find_missing(data)
find_index_missing(data)
DriectMethod_Linear(data)
DriectMethod_Quadratic(data)

print('\n','--------------- The End ---------------','\n')