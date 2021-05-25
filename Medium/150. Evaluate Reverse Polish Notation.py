"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3755/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any division
by zero operation.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """

    i = 0
    tmp = 0
    replace = 0
    while i < len(tokens):
        if tokens[i].isdigit() or (len(tokens[i]) > 1 and tokens[i][0] == '-'):
            i = i + 1
        else:
            if tokens[i] == "+":
                tmp = int(int(tokens[i-2]) + int(tokens[i-1]))
            if tokens[i] == "/":
                tmp = int(int(tokens[i-2]) / int(tokens[i-1]))
            if tokens[i] == "*":
                tmp = int(int(tokens[i-2]) * int(tokens[i-1]))
            if tokens[i] == "-":
                tmp = int(int(tokens[i-2]) - int(tokens[i-1]))
                
            tokens[i-2] = str(tmp)
            del tokens[i-1:i+1]
            i = 0
            tmp = 0

    return int(tokens[0])
            
#>>> tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#>>> evalRPN(tokens)
#>>> 22

            
            
        




    


