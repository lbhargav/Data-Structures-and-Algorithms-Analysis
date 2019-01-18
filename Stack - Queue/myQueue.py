#####################################################################
'''
 # Implements Queue data structure.
 # @author Bhargav Lenka
'''
#####################################################################

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def enqueue(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        return self.queue

    def dequeue(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.queue == []

    def build_queue(self, data):
        for i in data:
            self.push(i)
        return self.stack_data

def main():
    from random import randint
    queue_object = MyQueue()
    data = [randint(0, 100) for i in range(20)]
    print(queue_object.build_queue(data))
    queue_object.pop()

if __name__ == '__main__':
    main()