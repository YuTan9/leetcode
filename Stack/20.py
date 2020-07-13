class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # top ---- bottom
        for char in s:
            if char == '(':
                stack = ['('] + stack
            elif char == '{':
                stack = ['{'] + stack
            elif char == '[':
                stack = ['['] + stack

            elif char == ')':
                if stack == []:
                    return False
                if stack[0] != '(':
                    return False
                else:
                    stack = stack[1:]
            elif char == '}':
                if stack == []:
                    return False
                if stack[0] != '{':
                    return False
                else:
                    stack = stack[1:]
            elif char == ']':
                if stack == []:
                    return False
                if stack[0] != '[':
                    return False
                else:
                    stack = stack[1:]

            else:
                print "invalid input"
                return False

        return stack == []

"""
Better Solution:

stack = []
for brac in s:
    if brac == '(':
        stack.append(')')
    elif brac == '[':
        stack.append(']')
    elif brac == '{':
        stack.append('}')
    else:
        if len(stack) > 0 and stack.pop() == brac:
            continue
        else:
            return False
return True if len(stack) == 0 else False
"""