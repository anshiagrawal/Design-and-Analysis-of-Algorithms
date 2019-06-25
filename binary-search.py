###########BINARY SEARCH###########################
import math
l=[]

n=int(input("how many numbers in list"))
for i in range(0,n):
    l.append(int(input("enter number")))
f=int(input("enter number you want to find"))


def binary_search(l,low,high,f):
              if(low<=high):
                  mid=math.floor((low+high)/2)
                  if(l[mid]==f):
                       print("we found element at index ",mid)
                  elif(l[mid]<f):
                       binary_search(l,mid+1,high,f)
                  else:
                       binary_search(l,low,mid-1,f)
binary_search(l,0,len(l)-1,f)
    
