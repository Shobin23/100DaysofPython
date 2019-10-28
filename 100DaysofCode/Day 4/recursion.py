# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# numbers=[]
# for i in range(2000,3200):
#     if i % 7 ==0 and i%5!=0:
#         numbers.append(i)
#
# print(numbers)
#
# a=[i for i in range(2000,3000) if i%7==0 and i%5!=0]
#
# print(a)

# HOLY SHIT I JUST WROTE MY FIRST LIST COMPREHENSION
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# fact=[]
# #inp= input("Please enter a number:- ")
# inp=8
#
# inp=int(inp)
#
# counter=inp
# temp=inp
# while True:
#     a =temp*(counter-1)
#     temp=a
#     counter -= 1
#     if counter == 1:
#         print(temp)
#         break
#
# # AMAZINGGGGGGGGGGGGGGGGGGGGGGG

#Trying Bubble

# a = [10,9,8,7,6,97,4,321,62,1,89,6]
# print(a)
#
# Swapped=True
#
# while Swapped:
#     Swapped = False
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
#             Swapped=True
# print(a)

# Trying Selection

# a = [10,9,8,7,6,97,4,321,62,1,89,6]
# for i in range(len(a)):
#     minval= i
#     for j in range(i+1,len(a)):
#         if a[i+1]<=minval:
#             if a[j] < a[minval]:
#                 minval = j
#
#     a[i],a[minval] = a[minval],a[i]
#

# MergeSORT

# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2  # Finding the mid of the array
#         L = arr[:mid]  # Dividing the array elements
#         R = arr[mid:]  # into 2 halves
#
#         mergeSort(L)  # Sorting the first half
#         mergeSort(R)  # Sorting the second half
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
#
# # Code to print the list
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
#
# # driver code to test the above code
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")
#     printList(arr)
#     mergeSort(arr)
#     print("Sorted array is: ", end="\n")
#     printList(arr)
#
# c=8
# a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# b={x:x**2 for x in range(1,c+1)}
# print(b)

# import numpy as np
# import time
# import sys
# s = range(1000)
# print(sys.getsizeof(5)*len(s))
# a = np.array([(1,2,3),(4,5,6)])4

# a = input("Enter the nuber")
# print(type(a))
# print(a.split())
# print(tuple(a))

# class A():
#     def getstring(self):
#         s=input("Please enter a value :")
#         return s
#
#     def printstring(self,str):
#         print(str.capitalize())
#
# obj=A()
# b = obj.getstring()
# obj.printstring(b)













