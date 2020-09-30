#this code passes on leetcode
#test is too complex to implement.
from threading import Lock


class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        leftmeal = philosopher
        rightmeal = (philosopher + 1) % 5
        if philosopher == 0:
            leftmeal, rightmeal = rightmeal, leftmeal
        with self.locks[leftmeal]:
            with self.locks[rightmeal]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
