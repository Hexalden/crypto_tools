
def print_line():
    print("--------------------------------")


class BerlekampMasseyLfsrSynthesisAlgorithm:
    def __init__(self, s, verbose=False):
        self.verbose = verbose

        self.s = s
        self.lfsr = []
        self.taps = []

        self.berlekamp_massey_algo()

    def __repr__(self):
        print("s = ", end="")
        for i in self.s:
            print(i, end="")
        print("\nlfsr = {0}".format(self.lfsr))

    def berlekamp_massey_algo(self):
        verbose_print = print if self.verbose else lambda *a, **k: None

        # step 1. Initialization
        s_length = len(self.s)
        verbose_print("input string (length {0}):".format(s_length))
        for i in self.s:
            verbose_print("{0}".format(i), end="")
        verbose_print()
        verbose_print("(the leftmost bit was the first input)")

        b, c, t = [0] * s_length, [0] * s_length, [0] * s_length
        p = 0
        ll = 0
        m = 0
        b[0] = 1
        n = 0

        for i in range(0, s_length):
            c[i] = 0

        # step 2
        while n < s_length:
            verbose_print("--------------------------------")
            verbose_print("begin iteration {0} = N:".format(n))

            # step 2.1. Compute the next discrepancy d.
            k = 0
            for i in range(1, ll + 1):
                if c[i]:
                    k += self.s[n - i]

            d = int((self.s[n] != (k % 2)))
            if d:
                verbose_print("\td = 1")
            else:
                verbose_print("\td = 0")

            # step 2.2. If d = 1, then do the following:
            if d == 1:
                bound = n + 1
                p = n - m

                for i in range(1, bound):
                    t[i] = c[i]

                j = 0
                for i in range(p, bound):
                    if b[j]:
                        if c[i]:
                            c[i] = 0
                        else:
                            c[i] = 1
                    j += 1

                if ll <= (n / 2):
                    verbose_print("\t\tL <= (N / 2)")
                else:
                    verbose_print("\t\tL > (N / 2)")

                if ll <= (n / 2):
                    ll = n + 1 - ll
                    m = n
                    for i in range(1, bound):
                        b[i] = t[i]

            # step 2.3. N <-- N+1
            n += 1

            verbose_print("\tat end of iteration:")
            
            if self.verbose:
                if n < s_length:
                    print("\t\ts[N] = {0}, ".format(self.s[n]), end="")
                else:
                    print("\t\ts[N] = ?, ", end="")
                print("N = {0}, L = {1}, m = {2}, p = {3}".format(n, ll, m, p))
                print("\t\tb: ", end="")
                for i in range(0, s_length):
                    print(b[i], end="")
                print()
    
                print("\t\tc: ", end="")
                for i in range(0, s_length):
                    print(c[i], end="")
                print()
    
                print("\t\tt: ", end="")
                for i in range(0, s_length):
                    print(t[i], end="")
                print()

        verbose_print("--------------------------------")
        self.convert_result(ll, c)
        if self.verbose:
            self.print_lfsr(ll)

    def convert_result(self, ll, c):
        for i in range(ll):
            self.lfsr.append(self.s[ll-i-1])
            self.taps.append(c[i+1])

    def print_lfsr(self, ll):
        print("lfsr (length {0}, taps {1}):".format(ll, len(self.taps)))
        print("lfsr: ", end="")
        for x in self.lfsr:
            print(x, end="")
        print()
        print("taps: ", end="")
        for i in range(0, ll):
            if self.taps[i]:
                print(i, end="")

        print("\twhere the leftmost cell is number 0.")
        print("The initial cell values are the reverse of the")
        print("leftmost {0} values of the input bit sequence".format(len(self.lfsr)))
        print("The lfsr generates bits from right to left.")
