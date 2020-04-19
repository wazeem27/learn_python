"""

For loop in the background calls iter function an loop untils StopIterator exception occurs.

print(dir([])) --- contains __iter__ method. which means you can call __iter__() on list to get iterator object
Iterator is an object with a state so it remembers where is during iteration they get their next value using __next__ method

next([1,2,3,4]) it's actually trying to run __next__() method on that object
Iterator object can't go backwards only go forwards.

"""



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

