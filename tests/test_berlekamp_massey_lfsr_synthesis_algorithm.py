import berlekamp_massey_lfsr_synthesis_algorithm

class TestClass:
    def test_berlekamp_massey_lfsr_synthesis_algorithm_input1(self):
        s1 = [0, 0, 1, 1, 0, 1, 1, 1, 0]
        o1 = berlekamp_massey_lfsr_synthesis_algorithm.BerlekampMasseyLfsrSynthesisAlgorithm(s1)
        o1_taps_correct = [0, 0, 1, 0, 1]
        o1_lfsr_correct = [0, 1, 1, 0, 0]
        assert(o1.taps == o1_taps_correct)
        assert(o1.lfsr == o1_lfsr_correct)

    def test_berlekamp_massey_lfsr_synthesis_algorithm_input2(self):
        s2 = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
        o2 = berlekamp_massey_lfsr_synthesis_algorithm.BerlekampMasseyLfsrSynthesisAlgorithm(s2)
        o2_taps_correct = [1, 0, 0, 1]
        o2_lfsr_correct = [1, 1, 1, 1]
        assert(o2.taps == o2_taps_correct)
        assert(o2.lfsr == o2_lfsr_correct)
