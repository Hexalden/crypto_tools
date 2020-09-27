import square_attack


class TestSquareAttack:
    def test_dset(self):
        attack = square_attack.SquareAttack()
        dset = attack.create_dset(0)
        assert(attack.is_dset(dset) == [0])
        dset = attack.create_dset(5)
        assert(attack.is_dset(dset) == [5])
        dset = attack.create_dset(5)
        dset[10][10] = 12
        assert (attack.is_dset(dset) is None)

    def test_encrypt_dset(self):
        key = 0x00010203040506070809101112131415
        attack = square_attack.SquareAttack()
        dset = attack.create_dset(1)
        e_dset = attack.encrypt_dset(key, 1, dset)
        assert(e_dset[1] == [31, 144, 145, 147, 138, 255, 167, 182, 64, 138, 58, 25, 171, 135, 54, 75])
        assert(attack.is_dset(e_dset) == [13])

    def test_3_rounds(self):
        key = 0x00010203040506070809101112131415
        attack = square_attack.SquareAttack()
        dset = attack.create_dset(0)
        e_dset = attack.encrypt_dset(key, 3, dset)
        assert(attack.is_dset(e_dset) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_attack1(self):
        key = 0x00010203040506070809101112131415
        attack = square_attack.SquareAttack()
        dset = attack.create_dset(0)
        e_dset = attack.encrypt_dset(key, 4, dset)
        guess = attack.guess_key(e_dset)
        possible_derived_keys = attack.assemble_possible_derived_keys(guess)
        possible_master_keys = attack.retrieve_possible_master_keys(possible_derived_keys)
        assert(key in possible_master_keys)

    def test_attack2(self):
        key = 0x38208ab17bb294def029301928374441
        attack = square_attack.SquareAttack()
        dset = attack.create_dset(0)
        e_dset = attack.encrypt_dset(key, 4, dset)
        guess = attack.guess_key(e_dset)
        possible_derived_keys = attack.assemble_possible_derived_keys(guess)
        possible_master_keys = attack.retrieve_possible_master_keys(possible_derived_keys)
        assert (key in possible_master_keys)

    def test_attack3(self):
        key = 0x44444444444444444444444444444444
        attack = square_attack.SquareAttack()
        dset = attack.create_dset(0)
        e_dset = attack.encrypt_dset(key, 4, dset)
        guess = attack.guess_key(e_dset)
        possible_derived_keys = attack.assemble_possible_derived_keys(guess)
        possible_master_keys = attack.retrieve_possible_master_keys(possible_derived_keys)
        assert (key in possible_master_keys)
