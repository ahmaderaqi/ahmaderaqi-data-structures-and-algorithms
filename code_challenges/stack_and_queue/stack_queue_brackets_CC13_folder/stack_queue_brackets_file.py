from code_challenges.stack_and_queue.stack_file import Stack
from code_challenges.stack_and_queue.node import Node
from queue import Queue
from collections import deque
def is_balanced_parenthesis(sequence):
    stack = []
    queue = deque()

    for char in sequence:
        if char == '(':
            stack.append(char)
            queue.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
            queue.popleft()

    return len(stack) == 0 and len(queue) == 0


# way 1
# def validate_brackets(str):
#     round_brackets=0
#     curly_brackets=0
#     square_brackets=0
#     str1=list(str)
#     for i in str1:
        
#         if i=='(':
#             round_brackets+=1
            
#         if i==')':
#             round_brackets-=1 

#         if i=='[':
#             square_brackets+=1
#         if i==']':
#             square_brackets-=1

#         if i=='{':
#             curly_brackets+=1
#         if i=='}':
#             curly_brackets-=1
    
#     if round_brackets==0 and curly_brackets==0 and square_brackets==0:
#         return True
#     else:
#         return False
# way 2
# def validate_brackets_2(str):
#     stack=Stack()
#     str1=list(str)
#     str2=[]
#     for j in str1:
#         if j=='(' or j=='[' or j=='{':
#             str2.append(j)
#     # print(str2)
    
#     for j in str1:
#         if j==')' or j==']' or j=='}':
#             str2.append(j)
#     # print(str2)
#     # print(str1)
    
#     for i in str2:
#         # print(i)
#         if i =='(' or i=='[' or i=='{':
#             stack.push(i)
#         if i==')':
#             if stack.pop_specific_value('(') is None:
#                 return False
#         elif i==']':
#             if stack.pop_specific_value('[') is None:
#                 return False
#         elif i=='}':
#             if stack.pop_specific_value('{') is None:
#                 return False
            
#     if stack.get_size()==0:
#         return True
#     else:
#         return False

# strr="hello mr. (ahm)[a)d"
# result=validate_brackets(strr)
# print(result)