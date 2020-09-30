from threading import Barrier, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.b=Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.b.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.b.wait()
            printBar()

def printFoo():
    print('foo')

def printBar():
    print('bar')

my_foobar=FooBar(2)
foo_thread=Thread(target=my_foobar.foo,args=(printFoo,))
bar_thread=Thread(target=my_foobar.bar,args=(printBar,))
foo_thread.start()
bar_thread.start()