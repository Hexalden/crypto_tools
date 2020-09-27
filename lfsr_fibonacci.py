
class Cipher:
    def __init__(self, state, taps, verbose=False):
        self.verbose = verbose

        self.state = state
        self.taps = taps
        while len(self.state) < len(self.taps):
            self.state.append(0)
        while len(self.state) > len(self.taps):
            self.taps.append(0)

    def __repr__(self):
        print(self.state)
        print(self.taps)

    def step(self):
        new_bit = 0
        for i in range(0, len(self.taps)):
            if self.taps[i]:
                new_bit = new_bit ^ self.state[i]
        self.state.append(new_bit)
        self.state.pop(0)
        return new_bit

    def generate(self, n):
        new_bits = []
        for _ in range(0, n):
            new_bits.append(self.step())
        return new_bits

    def encrypt_bit_list(self, m):
        size = len(m)
        pool = self.generate(size)
        return [m ^ k for m, k in zip(m, pool)]

    def decrypt_bit_list(self, c):
        size = len(c)
        pool = self.generate(size)
        return [c ^ k for c, k in zip(c, pool)]

