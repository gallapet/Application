def solution(S):
    stack = []
    try:
        for op in S.split():
            if op.isnumeric() == True:
                stack.append(op)
            elif op.upper() == 'POP':
                stack.pop(-1)
            elif op.upper() == 'DUP':
                stack.append(stack[-1])
            elif op == '+':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                stack.append(str(a + b))
            elif op == '-':
                c = int(stack.pop(-1))
                d = int(stack.pop(-1))
                stack.append(str(c - d))
            print(stack)
    except IndexError:
            return -1
    
        
    return int(stack[-1])
