from threading import Thread, Event

class Foo:
    def __init__(self):
        self.events=[Event(), Event()]

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.events[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.events[0].wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.events[1].set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.events[1].wait()
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