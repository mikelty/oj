from threading import Event, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_ready=Event()
        self.foo_ready.set()
        self.bar_ready=Event()
        self.bar_ready.clear()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_ready.wait()
            self.foo_ready.clear()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_ready.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_ready.wait()
            self.bar_ready.clear()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_ready.set()

def printFoo():
    print('foo')

def printBar():
    print('bar')

my_foobar=FooBar(2)
foo_thread=Thread(target=my_foobar.foo,args=(printFoo,))
bar_thread=Thread(target=my_foobar.bar,args=(printBar,))
bar_thread.start()
foo_thread.start()