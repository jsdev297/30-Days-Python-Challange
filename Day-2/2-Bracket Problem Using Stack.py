
def isBalanced (input_str):
    s = list()
    for ch in input_str:
        if ch == '(':
            s.append(ch)
        if ch == ')':
            if not s:
                return False
            s.pop()
    return not s

string = "())"
if isBalanced(string) == True: print(string+" is balanced")
else: print(string + " is not balanced")
