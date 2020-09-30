from threading import Semaphore, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

        self.z = Semaphore(1)
        self.e = Semaphore(0)
        self.o = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.z.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.e.release()
            else:
                self.o.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()

def printNumber(n):
    print(n)

zeo=ZeroEvenOdd(10)
zero_t=Thread(target=zeo.zero,args=(printNumber,))
even_t=Thread(target=zeo.even,args=(printNumber,))
odd_t=Thread(target=zeo.odd,args=(printNumber,))
zero_t.start()
even_t.start()
odd_t.start()