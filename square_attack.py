import aes
import misc


class SquareAttack:
    @staticmethod
    def create_dset(active_byte):
        dset = []
        for i in range(0, 256):
            state = []
            for j in range(0, 16):
                if j == active_byte:
                    state.append(i)
                else:
                    state.append(0)
            dset.append(state)
        return dset

    @staticmethod
    def is_dset(dset):
        # dset shall contain 256 elements
        if len(dset) != 256:
            return None

        # find active byte
        state1 = dset[0]
        state2 = dset[1]
        state_len = len(state1)
        active_byte = [i for i in range(0, state_len) if state1[i] != state2[i]]
        if not active_byte:
            return None

        # check if dset
        for i in range(0, state_len):
            if i in active_byte:
                values = []
                for state in dset:
                    if state[i] not in values:
                        values.append(state[i])
                    else:
                        return None
            else:
                value = dset[0][i]
                for state in dset:
                    if state[i] != value:
                        return None

        return active_byte

    @staticmethod
    def encrypt_dset(key, rounds, dset):
        cipher = aes.Cipher(key)
        e_dset = []
        for state in dset:
            t = misc.bytelist_to_int(state)
            t = cipher.encrypt(t, rounds)
            t = misc.int_to_bytelist(t, 16)
            e_dset.append(t)
        return e_dset

    @staticmethod
    def reverse_state(byte, byte_pos, e_dset):
        aes_cipher = aes.Cipher(0)
        last_key = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        last_key[(byte_pos // 4)][(byte_pos % 4)] = byte
        reversed_bytes = []
        for state in e_dset:
            cipher_state = misc.int_to_matrix(misc.bytelist_to_int(state))
            aes_cipher.add_round_key(cipher_state, last_key)
            aes_cipher.inv_shift_rows(cipher_state)
            aes_cipher.inv_sub_bytes(cipher_state)
            reversed_bytes.append(cipher_state[((byte_pos % 4) + (byte_pos // 4)) % 4][byte_pos % 4])
        return reversed_bytes

    @staticmethod
    def check_key_guess(reversed_bytes):
        result = 0
        for b in reversed_bytes:
            result = result ^ b
        if result == 0:
            return True
        else:
            return False

    def guess_key_byte(self, byte_pos, e_dset):
        guess = []
        for byte in range(256):
            reversed_bytes = self.reverse_state(byte, byte_pos, e_dset)
            if self.check_key_guess(reversed_bytes):
                guess.append(byte)
        return guess

    def guess_key(self, e_dset):
        guess = []
        for k in range(16):
            guess.append(self.guess_key_byte(k, e_dset))
        return guess

    @staticmethod
    def assemble_possible_derived_keys(guess):
        possible_derived_keys = [[]]
        for g in guess:
            possible_derived_keys = misc.assemble_lists(possible_derived_keys, g)
        possible_derived_keys_matrix = []
        for key in possible_derived_keys:
            possible_derived_keys_matrix.append(misc.list_to_matrix(key))
        return possible_derived_keys_matrix

    @staticmethod
    def retrieve_possible_master_keys(possible_derived_keys):
        possible_master_keys = []
        for derived_key in possible_derived_keys:
            derived_key.reverse()
            retrieved_key = aes.AESTools.invert_key_schedule(derived_key=derived_key, rounds=4)
            possible_master_keys.append(retrieved_key)
        return possible_master_keys
