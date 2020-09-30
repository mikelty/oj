from threading import Semaphore, Thread


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sem = Semaphore()  # default is 1
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem15 = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(3, self.n + 1, 3):
            if i % 5 != 0:
                self.sem3.acquire()
                printFizz()
                self.sem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(5, self.n + 1, 5):
            if i % 3 != 0:
                self.sem5.acquire()
                printBuzz()
                self.sem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n + 1, 15):
            self.sem15.acquire()
            printFizzBuzz()
            self.sem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem.acquire()
            if i % 15 == 0:
                self.sem15.release()
            elif i % 5 == 0:
                self.sem5.release()
            elif i % 3 == 0:
                self.sem3.release()
            else:
                printNumber(i)
                self.sem.release()

def printFizz():
    print('Fizz')

def printBuzz():
    print('Buzz')

def printFizzBuzz():
    print('FizzBuzz')

def printNumber(i):
    print(i)

fb_obj=FizzBuzz(15)
fizz_t=Thread(target=fb_obj.fizz,args=(printFizz,))
buzz_t=Thread(target=fb_obj.buzz,args=(printBuzz,))
fizzbuzz_t=Thread(target=fb_obj.fizzbuzz,args=(printFizzBuzz,))
number_t=Thread(target=fb_obj.number,args=(printNumber,))
fizz_t.start()
buzz_t.start()
fizzbuzz_t.start()
number_t.start()