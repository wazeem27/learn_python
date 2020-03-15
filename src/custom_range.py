"""Custom range"""



class MyRange:
    def __init__(self, start, end, step=1):
        self.value = start
        self.start = start
        self.end = end
        self.step = step
        self._ok = True
        self.__validate()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step == 0:
            raise ValueError
        if self.value >= self.end and self.step > 0 or self.value <= self.end and self.step < 0:
            raise StopIteration
        if self._ok:
            current = self.value
            self.value += self.step
            return current
        raise StopIteration
    
    def validate(self):
        if self.step == 0:
            raise ValueError("step cannot be zero value")
        if self.start < self.end:
            if not self.end - (self.start + self.step) < (self.end - self.start):
                self._ok = False
        else:
            if not self.end - (self.start + self.step) > (self.end - self.start):
                self._ok = False
    __validate = validate


myrange = MyRange(1, 10, -2)
for i in myrange:
    print(i)
