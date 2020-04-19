


class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, seq):
        self.seq = seq
        self.index = len(seq)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.seq[self.index]

