from threading import Semaphore, Thread

class Foo:
    def __init__(self):
        self.first_second=Semaphore(0)
        self.second_third = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_second.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_second:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_third.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_third:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


def printFirst():
    print('first')

def printSecond():
    print('second')

def printThird():
    print('third')

if __name__=='__main__':
    foo=Foo()
    first_thread=Thread(target=foo.first,args=(printFirst,))
    second_thread = Thread(target=foo.second, args=(printSecond,))
    third_thread = Thread(target=foo.third, args=(printThird,))
    third_thread.start()
    second_thread.start()
    first_thread.start()