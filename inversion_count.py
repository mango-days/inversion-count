array = [ 8, 4, 2, 1 ]
inversion_count = 0

for index in range(1, len(array)):
    compare_with = array[index]
    i = index-1
    
    while ( i >= 0 and compare_with < array[i] ) :
        array[ i+1 ] = array[ i ]
        i -= 1
        inversion_count += 1

    array[ i + 1 ] = compare_with

print (inversion_count)
