
# coding: utf-8

# # Iterators

# 
#     Anything which can be used to iterate a loop. It has two necessary methods:
#         __iter__,__next__
#         Lists, tuples, dict, strings, sets are examples of inbuilt iterators.

# In[1]:



l=['a','b','c','d']
t=('a','b','c','d')
str="abcd"
d={'a':1,
   'b':2,
   'c':3,
   'd':4
  }
print("iterators in List")
for i in l:
    print(i)
print("iterators in Tuples")    
for i in t:
    print(i)
print("iterators in String")    
for i in str:
    print(i)
print("iterators in Dictionary")    
for i in d:
    print("%s %d" %(i,d[i]))


# # Zip

# 
#   Mapping similiar index of multiple iterables or container. 
#   Parameters : Python iterables or containers ( list, string etc )
#   Return Value  :  Returns a single iterator object, having mapped values from all the containers.

# In[2]:



name = ["Sakshi","Sahil","Swapnil",]
rollno = [28, 27, 45]
marks = [90, 92, 95] 
info = set(zip(name, rollno, marks))
print("output of zipped function: ")
print(info)


# # Map

# 
# 
# map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# 
# Parameters :
# 
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
# 
# 
# 
# 

# In[15]:


numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 


# # Reduce

# In[4]:



import functools 
lis = [ 1 , 3, 5, 6]
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 
  


# # list comprehension

# In[14]:



l = [2,3,5,6]
new = [x*x for x in l]
new


# # RMS calculation

# In[8]:



l=[]
sum = 0
n = int(input("Enter total no. of numbers:"))
for i in range(n):
    l.append(int(input()))
for i in l:
    sum = sum + i**2
rms = (sum ** 0.5)/len(l)  
print(rms)


# # Distance formula for n-dimensional coordinate system

# In[12]:



p1 = []
p2 = []
temp = 0
n = int(input("Enter no. of dimensions"))
print("Enter coordinates of point 1:")
for i in range(n):
    p1.append(int(input()))
print("Enter coordinates of point 2:")    
for i in range(n):
    p2.append(int(input()))
for i in range(n):
    temp = temp + (p1[i] - p2[i])**2
print("Distance between two points:",temp**0.5)
    

