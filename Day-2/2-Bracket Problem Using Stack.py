
def isBalanced (string):
    length = len(string)
    stack = list()
    for i in range(length):
        if string[i] == "(":
            stack.append(string[i])
        else:
            if string[i] == ")":
                if len(stack) == 0:
                    return False
                stack.pop()
    if len(stack) == 0:
        return True

inputString = input()
check = isBalanced(inputString)
if check == True:
    print("The String is Balanced")
else:
    print("The String is not Balanced")