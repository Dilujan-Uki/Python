import numpy as np;

array1 = np.array([1,2,3,4,5,6]);
array2 = np.array([7,8,9,10,11,12]);
array3 = np.concatenate((array1, array2));
print("Concatenated 1D Array:", array3);

#split
arraySplit1 = np.array_split(array3, 3);
print("Split 1D Arrays:");
print(arraySplit1[0]);
print(arraySplit1[1]);
print(arraySplit1[2]);