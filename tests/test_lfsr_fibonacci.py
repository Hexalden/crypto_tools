import lfsr_fibonacci


class TestClass:
    def test_lfsr_fibonacci_1(self):
        init = [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
        taps = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        lfsr = lfsr_fibonacci.Cipher(init, taps)
        new_bit = lfsr.step()
        assert(new_bit == 1)
        assert(lfsr.state == [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1])
        assert(lfsr.taps == taps)

        new_bits = lfsr.generate(5)
        assert(new_bits == [1, 0, 0, 1, 0])
        assert(lfsr.state == [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0])
        assert(lfsr.taps == taps)

    def test_lfsr_fibonacci_2(self):
        init = [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1]
        taps = [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
        lfsr = lfsr_fibonacci.Cipher(init, taps)
        new_bit = lfsr.step()
        assert(new_bit == 1)
        assert(lfsr.state == [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1])
        assert(lfsr.taps == taps)

        new_bits = lfsr.generate(5)
        assert(new_bits == [0, 1, 0, 1, 0])
        assert(lfsr.state == [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0])
        assert(lfsr.taps == taps)

    def test_encryption(self):
        init = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
        taps = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
        m = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        lfsr = lfsr_fibonacci.Cipher(init, taps)
        c = lfsr.encrypt_bit_list(m)
        assert(c == [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0])

    def test_decryption(self):
        init = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
        taps = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
        c = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]
        lfsr = lfsr_fibonacci.Cipher(init, taps)
        m = lfsr.encrypt_bit_list(c)
        assert(m == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
