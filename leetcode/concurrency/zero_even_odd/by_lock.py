from threading import Lock, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_l=Lock()
        self.even_l = Lock()
        self.odd_l = Lock()
        self.even_l.acquire()
        self.odd_l.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_l.acquire()
            printNumber(0)
            if i % 2 != 0:
                self.odd_l.release()
            else:
                self.even_l.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_l.acquire()
            printNumber(i)
            self.zero_l.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_l.acquire()
            printNumber(i)
            self.zero_l.release()

def printNumber(n):
    print(n)

zeo=ZeroEvenOdd(10)
zero_t=Thread(target=zeo.zero,args=(printNumber,))
even_t=Thread(target=zeo.even,args=(printNumber,))
odd_t=Thread(target=zeo.odd,args=(printNumber,))
zero_t.start()
even_t.start()
odd_t.start()