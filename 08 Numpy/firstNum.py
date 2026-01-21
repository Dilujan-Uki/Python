import numpy as np;

#Single Dimensional Array
arr=np.array([1,2,3,4,5]);
print(arr);
print(type(arr));

print(arr[2])
print(arr[2]+arr[4]);

#2D Array
arr2D=np.array([[1,2,3],[4,5,6]]);
print(arr2D);
print(arr2D[1][2]);

#3D Array
arr3D = np.array([[[10,34,67],[15,74,55]],[[23,45,78],[89,12,90]]]);
print(arr3D);