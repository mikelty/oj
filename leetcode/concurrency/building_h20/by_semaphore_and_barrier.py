from threading import Thread, Semaphore, Barrier


class H2O:
    def __init__(self):
        self.h=Semaphore(2)
        self.o=Semaphore(1)
        self.b=Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        self.b.wait()
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.b.wait()
        releaseOxygen()
        self.o.release()

def releaseHydrogen():
    print('H')

def releaseOxygen():
    print('O')

h20_obj=H2O()
hydrogen_threads, oxygen_threads=[],[]
for _ in range(10):
    hydrogen_threads.append(Thread(target=h20_obj.hydrogen,args=(releaseHydrogen,)))
    hydrogen_threads.append(Thread(target=h20_obj.hydrogen, args=(releaseHydrogen,)))
    oxygen_threads.append(Thread(target=h20_obj.oxygen,args=(releaseOxygen,)))

for t in hydrogen_threads:
    t.start()

for t in oxygen_threads:
    t.start()