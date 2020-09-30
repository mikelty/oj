from threading import Event, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_e=Event()
        self.zero_e.set()
        self.even_e = Event()
        self.even_e.clear()
        self.odd_e = Event()
        self.odd_e.clear()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_e.wait()
            self.zero_e.clear()
            printNumber(0)
            if i%2!=0:
                self.odd_e.set()
            else:
                self.even_e.set()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_e.wait()
            self.even_e.clear()
            printNumber(i)
            self.zero_e.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_e.wait()
            self.odd_e.clear()
            printNumber(i)
            self.zero_e.set()

def printNumber(n):
    print(n)

zeo=ZeroEvenOdd(10)
zero_t=Thread(target=zeo.zero,args=(printNumber,))
even_t=Thread(target=zeo.even,args=(printNumber,))
odd_t=Thread(target=zeo.odd,args=(printNumber,))
zero_t.start()
even_t.start()
odd_t.start()