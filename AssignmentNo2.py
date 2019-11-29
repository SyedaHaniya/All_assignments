#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 1
total = 0;
while i < 6:
    a = input("Enter subject " + str(i) + " marks: ")
    total = total + int(a)
    i = i + 1

print("Total marks: " + str(total))


# In[2]:


num = int(input("Enter number:"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# In[14]:


def listLength(list):
    return len(list)

print("Length of the list is:")
print(listLength(["English", "Math", "Computer", "Chemistry", "Urdu", "Biology", "Physics"]))



# In[15]:


def numItems(list):
    i = 0
    sum = 0
    while i < len(list):
        sum = sum + int(list[i])
        i = i + 1
    
    return sum
print("Sum is:")
print(numItems([65, 93, 27, 12, 56]))


# In[13]:


def largestNum(list):
    largest = 0;
    for a in list:
        if a > largest:
           largest = a

    return largest

print("The largest number in the list is:")
print(largestNum([43, 25, 90, 12, 87]))


# In[ ]:


def lessThanFive(list):
    i = 0
    for num in list:
        if num < 5:
            print(num)



lessThanFive([2, 7, 54, 1, 4, 3, 8])

