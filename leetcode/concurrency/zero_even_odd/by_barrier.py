from threading import Barrier, Lock, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_l=Lock()
        self.bs=[Barrier(2),Barrier(2)]

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_l.acquire()
            printNumber(0)
            self.bs[i % 2].wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.bs[0].wait()
            printNumber(i)
            self.zero_l.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.bs[1].wait()
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