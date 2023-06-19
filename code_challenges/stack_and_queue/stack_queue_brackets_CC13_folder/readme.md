# stack-queue-brackets

checking if the string is balanced in parentheses 
## Whiteboard Process
![lab13](https://github.com/ahmaderaqi/reading-notes/assets/118004544/7be6e28c-6ba7-4026-9f6a-6f6cc7ebaa70)

## Approach & Efficiency
checking if the string is balanced in parentheses 


## Algorithm of stack:
 ### The algorithm for adding an element to a stack (also known as "pushing" onto the stack) is:

1. declare three variables each one is for one bracket.

2. splitting the string into char using list method and store them inside an array

3. looping throw the array and check if three's a parentheses

4. if it's an openning parentheses,add one to the variable that's related to it, and if it's an closed parentheses subtract one

5. to check if it's balanced, we check if all the variables are equal to zero,if yes, they are balanced 
6. return trueif yes, and false if no



Big O
time complexity is O(n)
space complexity is O(1)

## Solution
|Code challenge13  |    [code1](./stack_queue_brackets_file.py)


