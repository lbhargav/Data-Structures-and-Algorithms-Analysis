#####################################################################
'''
 # Implements min element stack data structure.
 # @author Bhargav Lenka
'''
#####################################################################


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack_data:
            self.stack_data.append((x, x))
        else:
            self.stack_data.append((x, min(x, self.stack_data[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack_data:
            self.stack_data.pop()[0]
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.stack_data:
            return self.stack_data[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack_data:
            return self.stack_data[-1][1]
        else:
            return None

    def build_stack(self, data):
        for i in data:
            self.push(i)
        return self.stack_data


def main():
    from random import randint
    stack_object = MinStack()
    data = [randint(0, 10) for i in range(5)]
    print(stack_object.build_stack(data))
    print(stack_object.getMin())


if __name__ == '__main__':
    main()