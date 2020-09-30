from threading import Thread
from collections import deque


class H2O:
    def __init__(self):
        self._hq = deque()
        self._oq = deque()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self._hq.append(releaseHydrogen)
        self.build()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self._oq.append(releaseOxygen)
        self.build()

    def build(self):
        if len(self._hq) > 1 and len(self._oq) > 0:
            self._hq.pop()()
            self._hq.pop()()
            self._oq.pop()()

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