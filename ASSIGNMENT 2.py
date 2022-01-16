#!/usr/bin/env python
# coding: utf-8

# Q1.What are the two values of the Boolean data type? How do you write them?
# 
# Ans)True and False are the two types of boolean data types. We write them using capital T and F, with the rest of the word in lowercase i.e True and False.

# Q2)What are the three different types of Boolean operators?
# 
# Ans)AND (&&) = only if all the arguments are true then it returns true.
# (True and False = False)
# 
# or (||) = if any one of the arguments is true then it returns true.
# (True or False = True)
# 
# not (!) = if argument is true returns false and vice versa. (not True = 
# False)

# Q3)  Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# Ans)TRUE TABLE FOR AND
#     Operator A	Operator B	 Logical AND result
#         True	   True	            True
#         True	   False	        False
#         False	   True	            False
#         False	   False	        False
# TRUE TABLE FOR OR
#     Operator A	Operator B	 Logical OR Result
#         True	   True	            True
#         True	   False	        True
#         False	   True	            True
#         False	   False	        False
# TRUE TABLE FOR NOT
#     Operator A	Logical NOT Result
#         True	    False
#         False	    True

# 4. What are the values of the following expressions?
# 

# In[1]:


print((5 > 4) and (3 == 5))     ### FALSE


# In[2]:


not (5 > 4)                    ### FALSE


# In[3]:


(5 > 4) or (3 == 5)           ###TRUE


# In[4]:


not ((5 > 4) or (3 == 5))    ###FALSE


# In[5]:


(True and True) and (True == False)    ###FALSE


# In[6]:


(not False) or (not True)        ###TRUE


# 5. What are the six comparison operators?
# 
# Ans)There are six main comparison operators: equal to(=), not equal to(!=), greater than(>), greater than or equal to(>=), less than(<), and less than or equal to(<=).

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# Ans) The “=” (assignment operator) is used to assign the value on the right to the variable on the left. The '==' operator checks whether the two given operands are equal or not. If so, it returns true.
# 

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 
# Ans)The three blocks are everything inside the if statement and the lines print('bacon') and print('ham').
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# 

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# 

# In[7]:


spam=eval(input("Enter 1,2 or anything"))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# Ans) Press ctrl-C to stop a program stuck in an endless loop.

# 10. How can you tell the difference between break and continue?
# 
# Ans) The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# Ans) They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0,10) explicitly tells the loop to start at 0 , and range (0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration.
# 

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[8]:


for i in range (1,11):
    print (i)


# In[10]:


i=1
while i<=10:
    print(i)
    i=i+1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# Ans) This function can be called with spam.bacon().

# In[ ]:




