import numpy as np
arr=np.array([10,20,30,40,50,60,70,80,90,100]);
print("Original Array:",arr);
print(arr[3:8]);          #Slicing from index 3 to 7
print(arr[4:]);
print(arr[3:8:3]);    #Slicing with step 2

#Slicing in 2D Array
arr2D=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]);
print("Original 2D Array:\n",arr2D);
print(arr2D[1,1:4]);      #Slicing row 1, columns 1 to 3