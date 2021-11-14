array = [ 8, 4, 2, 1 ]
inversion_count = 0
for index1 in range ( 0, len(array)-1 ) :
        for index2 in range ( 0, len(array)-1-index1 ) :
            if array[ index2 ] > array[ index2+1 ] : inversion_count+=1
print (inversion_count)