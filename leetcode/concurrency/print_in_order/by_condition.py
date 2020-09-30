from threading import Thread, Condition

class Foo:
    def __init__(self):
        self.cond_var=Condition()
        self.to_print='first'
        self.to_print_second=lambda: self.to_print=='second'
        self.to_print_third = lambda: self.to_print == 'third'

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.cond_var:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.to_print='second'
            self.cond_var.notify(2) #wakes up the other two threads

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cond_var:
            self.cond_var.wait_for(self.to_print_second)
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.to_print='third'
            self.cond_var.notify()  # wakes up the last thread

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cond_var:
            self.cond_var.wait_for(self.to_print_third)
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