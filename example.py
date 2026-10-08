from codebeat import code_tracker
def fun1(x, y):
    m = 0
    for i in range(x):
        for j in range(y):
            m += i*j 
    return m

obj = code_tracker(fun1,12) # modify, create executable
a=int(input('enter the first number'))
b=int(input('enter the second number'))
print(obj(a, b)) # for loop for n times and call fun and display final result

def matrix_sum(x, y):
    total = 0
    for i in range(x):
        row = 0
        for j in range(y):
            row += i + j
        total += row
    return total

obj = code_tracker(matrix_sum)
print(obj(5, 6))  # Expect outer loop ~2x inner time
