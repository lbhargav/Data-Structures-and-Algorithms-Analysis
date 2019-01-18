'''
 # Implements infix to postfix, postfix expression evaluation, prefix expression evaluation
 # @author Bhargav Lenka
'''
from stack import Stack

class Evaluation():
    # a+b*c = abc*+
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def __init__(self, precedence):
        self.precedence = precedence

    def infixToPostfix(self, object, expression):
        result = ""
        for exp in expression:
            if exp.isalpha():
                result += exp
            else:
                while not object.isEmpty() and self.precedence[exp] <= self.precedence[object.top()]:
                    result += object.top()
                    object.pop()
                object.push(exp)
        while not object.isEmpty():
            result += object.top()
            object.pop()
        return result

    def postfixEvaluation(self, object, expression):
        for exp in expression:
            if exp.isdigit():
                object.push(str(exp))
            if exp in self.precedence.keys():
                op2 = object.top()
                object.pop()
                op1 = object.top()
                object.pop()
                output = str(eval(str(op1) + exp + str(op2)))
                object.push(output)
        return object.top()

    def prefixEvaluation(self, object, expression):
        for exp in range(0, len(expression)):
            if expression[exp].isdigit():
                object.push(expression[exp])
            if expression[exp] in dict:
                op1 = object.top()
                object.pop()
                op2 = object.top()
                object.pop()
                output = eval(str(op1) + exp + str(op2))
                object.push(output)
        return object.top()
def main():
    tempStack = Stack()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    exp_eva = Evaluation(precedence)
    exp = "2*3+24"
    #print(exp_eva.infixToPostfix(tempStack, exp))
    print(exp_eva.postfixEvaluation(tempStack, exp))

if __name__ == '__main__':
    main()


