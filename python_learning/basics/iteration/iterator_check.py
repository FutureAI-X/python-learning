from collections.abc import Iterator
from iterator_demo import CountDown

if __name__ == '__main__':
    print(isinstance(CountDown(3), Iterator))               # True
    print(isinstance([], Iterator))                         # False
    print(isinstance((), Iterator))                         # False
    print(isinstance({}, Iterator))                         # False 
    print(isinstance(set(), Iterator))                      # False
    print(isinstance(range(10), Iterator))                  # False
    print(isinstance((x for x in range(10)), Iterator))     # True
    print(isinstance(iter([]), Iterator))                   # True
    print(isinstance(iter(()), Iterator))                   # True