"""
CSE331 Project 4 FS24
Circular Double-Ended Queue
solution.py
"""

from typing import TypeVar, List

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by a front enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #
    # Your code goes here!
    #
    def __len__(self) -> int:
        """
        Returns the current number of elements in the deque.
        :return: Integer representing the number of elements in the deque.
        """
        return self.size 
    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.
        :return: True if the deque is empty, False otherwise.
        """
        if self.size == 0:
            return True
        return False

    def front_element(self) -> T:
        """
        Retrieves the element at the front of the deque without removing it.
        :return: The element at the front, or None if the deque is empty.
        """
        try:
          return self.queue[self.front]
        except (IndexError, TypeError):
            return None

    def back_element(self) -> T:
        """
        Retrieves the element at the back of the deque without removing it.
        :return: The element at the back, or None if the deque is empty.
        """
        try:
          return self.queue[self.back]
        except (IndexError, TypeError):
            return None

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds an element to either the front or the back of the deque.
        :param value: The element to add to the deque.
        :param front: If True, the element is added to the front; if False, to the back.
        """
        
        if self.is_empty():
            self.front = 0
            self.queue[self.front] = value
            self.back = (self.front )
        
        elif front:
            self.front = (self.front -1 + self.capacity) % self.capacity
            self.queue[self.front] = value

        else:
            self.back = (self.back + 1 ) % self.capacity
            self.queue[self.back] = value
        
        self.size += 1

        if self.size == self.capacity:
            self.grow()


    def dequeue(self, front: bool = True) -> T:
        """
        Removes an element from either the front or the back of the deque.
        :param front: If True, removes the element from the front; if False, from the back.
        :return: The removed element, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        
        elif front:
            element = self.queue[self.front]
            #self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
        
        elif not front:
            element = self.queue[self.back]
            #self.queue[self.back] = None
            self.back = (self.back - 1 + self.capacity) % self.capacity
            self.size -= 1
        


        if(self.size<= self.capacity/4 and self.capacity//2 >= 4): 
            self.shrink()
        

        return element


    def grow(self) -> None:
        """
        Doubles the capacity of the deque when it becomes full, reassigning all elements.
        """

        self.capacity *= 2
        new_q : List[T] = [None] * self.capacity 

        
        for index in range(self.size):
            new_q[index] = self.queue[(index + self.front) % self.size]
        
        self.front = 0
        self.back = self.size - 1
        
        self.queue = new_q


    def shrink(self) -> None:
        """
        Halves the capacity of the deque when the number of elements is one-fourth the current capacity,
        reassigning all elements in a smaller array.
        """

        self.capacity //= 2
    
        new_q : List[T] = [None] * self.capacity 
        

        for index in range(self.size):
            new_q[index] = self.queue[(self.front + index) % len(self.queue)]
        
        self.front = 0
        self.back = self.size - 1 if self.size > 0 else 0

        self.queue = new_q


def get_winning_numbers(numbers: List[int], size: int) -> List[int]:
    """
    Takes in a list of numbers and a sliding window size, returning the maximum value
    in each sliding window as it moves one step to the right at each iteration.
    
    :param numbers: A list of numbers over which the sliding window will move.
    :param size: The size of the sliding window (1 <= size <= len(numbers)).
    :return: A list containing the maximum value of the sliding window at each step.
    """
    
    if not numbers or size == 0:
        return []

    result = []
    window = CircularDeque()

    for i, num in enumerate(numbers):
        if not window.is_empty() and window.front_element() <= i - size:
            window.dequeue(front=True)

        while not window.is_empty() and numbers[window.back_element()] <= num:
            window.dequeue(front=False)

        window.enqueue(i ,front=False)

        if i >= size - 1:
            result.append(numbers[window.front_element()])  
    return result
    


def get_winning_probability(winning_numbers: List[int]) -> int:
    """
    Calculates the probability of winning by finding the largest sum of non-adjacent numbers
    from a list of winning numbers.

    :param winning_numbers: A list of winning numbers that the algorithm will analyze.
    :return: An integer representing the probability of winning, or 0 if the list is empty.
    """

    if not winning_numbers:
        return 0
    elif len(winning_numbers) == 1:
        return winning_numbers[0]

    dp = [0] * len(winning_numbers)
    dp[0] = winning_numbers[0]
    dp[1] = max(winning_numbers[0], winning_numbers[1])

    for i in range(2, len(winning_numbers)):
        dp[i] = max(dp[i - 1], dp[i - 2] + winning_numbers[i])

    return dp[-1]





