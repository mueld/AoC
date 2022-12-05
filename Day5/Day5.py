import numpy as np


    
stack = [[],["L","N","W","T","D"],["C","P","H"],["W","P","H","N","D","G","M","J"],["C","W","S","N","T","Q","L"],["P","H","C","N"],["T","H","N","D","M","W","Q","B"],["M","B","R","J","G","S","L"],["Z","N","W","G","V","B","R","T"],["W","G","D","N","P","L"]]

f = open("Day5/Inputdata.txt", "r")
for line in f.readlines():
    count = int(line.split()[1])
    stackFrom = int(line.split()[3])
    stackTo = int(line.split()[5])
    viewFrom = stack[stackFrom][-(count):]
    for i in range(count):
        stack[stackTo].append(viewFrom[i])
    
    for i in range(count):
        stack[stackFrom].pop(len(stack[stackFrom])-1)
        
message = ""
for i in range(1,len(stack)):
    message = message + stack[i][len(stack[i])-1]
print(message)