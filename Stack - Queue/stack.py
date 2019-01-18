#####################################################################
'''
 # Implements stack data structure.
 # @author Bhargav Lenka
'''
#####################################################################

class Stack:
    def __init__(self):
        self.stack_data = []
    def isEmpty(self):
        return self.stack_data == []
    def push(self, x):
        self.stack_data.append(x)
    def pop(self):
        if self.isEmpty() is True:
            return -1
        else:
            self.stack_data.pop()
    def top(self):
        if self.isEmpty() is True:
            return -1
        else:
            return self.stack_data[-1]
    def __sizeof__(self):
        return len(self.stack_data)

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in dict.values():
                stack.append(char)
            else:
                if not stack or dict[char] != stack[-1]:
                    return False
                stack.pop()
        return stack == []
    def build_stack(self, data):
        for i in data:
            self.push(i)
        return self.stack_data


def main():
    from random import randint
    stack_object = Stack()
    data = [randint(0, 100) for i in range(20)]
    print(stack_object.build_stack(data))
    print(stack_object.top)

if __name__ == '__main__':
    main()

