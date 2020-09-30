from threading import Semaphore, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.current='zero'
        self.condition=Condition()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            with self.condition:
                self.condition.wait_for(lambda:self.current=='zero')
                printNumber(0)
                self.current='odd' if i %2 != 0 else 'even'
                self.condition.notify(2)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            with self.condition:
                self.condition.wait_for(lambda:self.current=='even')
                printNumber(i)
                self.current='zero'
                self.condition.notify(2)

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            with self.condition:
                self.condition.wait_for(lambda:self.current=='odd')
                printNumber(i)
                self.current='zero'
                self.condition.notify(2)

def printNumber(n):
    print(n)

zeo=ZeroEvenOdd(10)
zero_t=Thread(target=zeo.zero,args=(printNumber,))
even_t=Thread(target=zeo.even,args=(printNumber,))
odd_t=Thread(target=zeo.odd,args=(printNumber,))
zero_t.start()
even_t.start()
odd_t.start()