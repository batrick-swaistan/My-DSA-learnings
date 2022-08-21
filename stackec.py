op=['(','[','{']
cl=[')',']','}']
def check(rstr):
    stack=[]
    for i in rstr:
        if i in op:
            stack.append(i)
        elif i in cl:
            pos=cl.index(i)
            if (len(stack)>0) and (op[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"
inp=str(input())
check(inp)
