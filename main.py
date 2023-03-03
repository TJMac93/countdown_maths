from time import sleep
from random import randint
from abc import ABC
from functools import lru_cache
import numpy as np


class MathsOperator(ABC):
    def __init__(self, left , right):
        self.left = left
        self.right = right

    def value(self):
        ...
    @lru_cache    
    def __add__(self, other):
        if isinstance(other, MathsOperator):
            return self.value + other.value
        else:
            return self.value + other
    
    @lru_cache    
    def __sub__(self, other):
        if isinstance(other, MathsOperator):
            return self.value - other.value
        else:
            return self.value - other

    @lru_cache    
    def __truediv__(self,other):
        if isinstance(other, MathsOperator):
            return self.value / other.value
        else:
            return self.value / other

    @lru_cache    
    def __mul__(self, other):
        if isinstance(other, MathsOperator):
            return self.value * other.value
        else:
            return self.value * other

class Multiply(MathsOperator):
    @property
    def value(self):
        l_val = self.left.value if isinstance(self.left, MathsOperator) else self.left
        r_val = self.right.value if isinstance(self.right, MathsOperator) else self.right
        return l_val * r_val

    def __str__(self):
        return "(" + str(self.left) + "*" + str(self.right) + ")"

class Add(MathsOperator):
    @property
    def value(self):
        l_val = self.left.value if isinstance(self.left, MathsOperator) else self.left
        r_val = self.right.value if isinstance(self.right, MathsOperator) else self.right
        return l_val + r_val

    def __str__(self):
        return "(" + str(self.left) + "+" + str(self.right) + ")"

class Subtract(MathsOperator):
    @property
    def value(self):
        l_val = self.left.value if isinstance(self.left, MathsOperator) else self.left
        r_val = self.right.value if isinstance(self.right, MathsOperator) else self.right
        return l_val - r_val

    def __str__(self):
        return "(" + str(self.left) + "-" + str(self.right) + ")"

class Divide(MathsOperator):
    @property
    def value(self):
        l_val = self.left.value if isinstance(self.left, MathsOperator) else self.left
        r_val = self.right.value if isinstance(self.right, MathsOperator) else self.right
        return l_val / r_val
    def __str__(self):
        return "(" + str(self.left) + "/" + str(self.right) + ")"
# @lru_cache
def solve(goal, nums, verbose = True):
    if verbose:
        print(f"Aiming for {goal} using {nums}")
        print("-"*35)

    # Check the first item in the list against all others
    for idx, i in enumerate(nums):
        # Create a sublist to exclude the same number
        nums_without_i = nums[idx+1:]
        for idx2, j in enumerate(nums_without_i):
            x = Add(i,j)

            # Create a new list that does not contain j either
            # But does contain i+j
            nums_without_ij = nums_without_i[idx2+1:]
            nums_without_ij.insert(0,x)
        
            # If it doesn't get the answer, recurse
            if x.value == goal:
                print(x, " = ", x.value)
                return x
            solve(goal, nums_without_ij, verbose = False)
            x = Multiply(i,j)

            # Create a new list that does not contain j either
            # But does contain i*j
            nums_without_ij = nums_without_i[:idx2] + nums_without_i[idx2+1:]
            nums_without_ij.insert(0,x)
        
            # If it doesn't get the answer, recurse
            if x.value == goal:
                print(x, " = ", x.value)
                return x
            solve(goal, nums_without_ij, verbose = False)
            x = Divide(i,j)

            # Create a new list that does not contain j either
            # But does contain i/j
            nums_without_ij = nums_without_i[:idx2] + nums_without_i[idx2+1:]
            nums_without_ij.insert(0,x)
        
            # If it doesn't get the answer, recurse
            if x.value == goal:
                print(x, " = ", x.value)
                return x
            solve(goal, nums_without_ij, verbose = False)
            x = Subtract(i,j)

            # Create a new list that does not contain j either
            # But does contain i-j
            nums_without_ij = nums_without_i[:idx2] + nums_without_i[idx2+1:]
            nums_without_ij.insert(0,x)
        
            # If it doesn't get the answer, recurse
            if x.value == goal:
                print(x, " = ", x.value)
                return x
            solve(goal, nums_without_ij, verbose = False)

def main():

    while True:
        big = [25,50,75,100]
        small = [i for i in range(1,11)]
        small += small
        n_big = -1
        while n_big <0 or n_big >4:
            n_big =  int(input("How many big numbers? (MAX 4):\t"))
        n_small = 6-n_big
        goal = randint(1,1000)

        ns = list(np.concatenate((np.random.choice(big, n_big, replace = False),np.random.choice(small, n_small, replace = False))))
        print("-"*25)
        print("Your numbers are:")
        for n in ns:
            print(n)
            sleep(0.3)

        print("And your goal is:")
        sleep(0.3)
        print(f"---{goal}---")
        print(ns)

        sleep(3)
        print()
        solve(goal, ns)

        replay = input("Play again? (Y/N) ")
        if replay in ("N","n"):
            break

if __name__ == '__main__':
    main()
