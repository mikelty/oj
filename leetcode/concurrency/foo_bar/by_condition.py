from threading import Condition, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_counter=0
        self.bar_counter=0
        self.condition=Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda:self.foo_counter==self.bar_counter)
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.foo_counter+=1
                self.condition.notify(1)

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda:self.foo_counter>self.bar_counter)
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.bar_counter+=1
                self.condition.notify(1)

def printFoo():
    print('foo')

def printBar():
    print('bar')

my_foobar=FooBar(2)
foo_thread=Thread(target=my_foobar.foo,args=(printFoo,))
bar_thread=Thread(target=my_foobar.bar,args=(printBar,))
bar_thread.start()
foo_thread.start()