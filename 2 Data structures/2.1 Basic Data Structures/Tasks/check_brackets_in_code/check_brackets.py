# Problem Introduction
# In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the
# code.

# Task. Your friend is making a text editor for programmers. He is currently working on a feature that will
# find errors in the usage of different types of brackets. Code can contain any brackets from the set
# []{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them
# are ],}, and ).
# For convenience, the text editor should not only inform the user that there is an error in the usage
# of brackets, but also point to the exact place in the code with the problematic bracket. First priority
# is to find the first unmatched closing bracket which either doesnt have an opening bracket before it,
# like ] in ](), or closes the wrong opening bracket, like } in ()[}. If there are no such mistakes, then
# it should find the first unmatched opening bracket without the corresponding closing bracket after it,
# like ( in {}([]. If there are no mistakes, text editor should inform the user that the usage of brackets
# is correct.
# Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.
# More formally, all brackets in the code should be divided into pairs of matching brackets, such that in
# each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either
# one of them is nested inside another one as in (foo[bar]) or they are separate as in f(a,b)-g[c].
# The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).

# Input Format. Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
# marks and brackets from the set []{}().

# Constraints. The length of 𝑆 is at least 1 and at most 105.

# Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
# output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
# brackets, output the 1-based index of the first unmatched opening bracket.

import sys


# making class Bracket with type and position
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    # method to match brackets types
    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()
    top = ""
    opening_brackets_stack = []
    ans = 0
    # searching for brackets in the text and putting them into stack
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
        # for closing brackets checking the top bracket in the stack to match it correctly
        elif next == ')' or next == ']' or next == '}':
            # check the stack to have elements
            if opening_brackets_stack == []:
                ans = i + 1
                break
            top = opening_brackets_stack.pop()
            if not top.match(next):
                ans = i + 1
                break
    if ans != 0:
        print(ans)
    elif opening_brackets_stack != []:
        print(opening_brackets_stack[len(opening_brackets_stack) - 1].position + 1)
    else:
        print('Success')
# Example of input:
# {[]}()
# Output:
# Success

# Example of Input:
# {[}
# Output:
# 3
