import random
import time

my_list = random.sample(range(100), 10)

print(my_list)

n = len(my_list) # find list range, 10 in this case
# loop_time = time.time() # start loop timer
for i in range(n-1): # number of passes through a list
    swapped = False # tracks whether any swap occurs in this pass

    for j in range(n-i-1): # compare adjacent elements, ignore sorted tail (i = last element, -1 prevents out of range access)
        if my_list[j] > my_list[j+1]: # logic to check if elements are in wrong order
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j] # swap elements to put in ascending order
            swapped = True # confirmed swapping of elements

    if not swapped: # break loop if list is already sorted
        break

# print(f'loop_time: {(time.time() - loop_time)}') # calculate end of loop
print(my_list)
