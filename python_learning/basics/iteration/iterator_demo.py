class CountDown:
    def __init__(self, range):
        self.range = range

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.range <= 0:
            raise StopIteration
        
        self.range -= 1
        return self.range + 1
    
if __name__ == "__main__":
    countdown = CountDown(3)
    for i in countdown:
        print(i)