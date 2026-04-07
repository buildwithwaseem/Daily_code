#chessborad of 8 x 8 matrix
import numpy as np 
chess = np.zeros((8, 8) , dtype=int)


chess[0::2 , 1::2] = 1

chess[1::2, 0::2] = 1

print(chess)


#revise 1
import numpy as np
chess = np.zeros((8,8), dtype=int)

chess[0::2, 1::2] =1
chess[1::2, 0::2] = 1

print(chess)











#----------------------------------------------------------
#array
import numpy as np
vec = np.array([10,20,30])     #shape(3, )
#matrix
mat = np.arange(1,10).reshape(3, 3)

row_add = vec + mat
print(row_add)


vec_col = vec.reshape(3,1)
col_add = mat + vec_col
print(col_add)