from threading import Lock, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_ready=Lock()
        self.bar_ready=Lock()
        self.bar_ready.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_ready.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_ready.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_ready.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_ready.release()

def printFoo():
    print('foo')

def printBar():
    print('bar')

my_foobar=FooBar(2)
foo_thread=Thread(target=my_foobar.foo,args=(printFoo,))
bar_thread=Thread(target=my_foobar.bar,args=(printBar,))
bar_thread.start()
foo_thread.start()