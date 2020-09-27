import aes
import misc


class TestAES:
    def test_encryption_1(self):
        aes_cipher = aes.Cipher(0x2b7e151628aed2a6abf7158809cf4f3c)
        plaintext = 0x3243f6a8885a308d313198a2e0370734
        encrypted = aes_cipher.encrypt(plaintext, 10)
        assert(encrypted == 0x3925841d02dc09fbdc118597196a0b32)

    def test_encryption_2(self):
        aes_cipher = aes.Cipher(0x000102030405060708090a0b0c0d0e0f)
        plaintext = 0x00112233445566778899aabbccddeeff
        encrypted = aes_cipher.encrypt(plaintext, 10)
        assert(encrypted == 0x69c4e0d86a7b0430d8cdb78070b4c55a)

    def test_encryption_3(self):
        aes_cipher = aes.Cipher(0x2b7e151628aed2a6abf7158809cf4f3c)
        plaintext = 0x000102030405060708090a0b0c0d0e0f
        ciphertext = aes_cipher.encrypt(plaintext, 10)
        assert(ciphertext == 0x50FE67CC996D32B6DA0937E99BAFEC60)
        plaintext = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        ciphertext = aes_cipher.encrypt(misc.bytelist_to_int(plaintext), 10)
        assert(ciphertext == 0x50FE67CC996D32B6DA0937E99BAFEC60)
        decrypted = misc.int_to_bytelist(aes_cipher.decrypt(ciphertext, 10), 16)
        assert(decrypted == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_decryption_1(self):
        aes_cipher = aes.Cipher(0x2b7e151628aed2a6abf7158809cf4f3c)
        ciphertext = 0x3925841d02dc09fbdc118597196a0b32
        decrypted = aes_cipher.decrypt(ciphertext, 10)
        assert(decrypted == 0x3243f6a8885a308d313198a2e0370734)

    def test_decryption_2(self):
        aes_cipher = aes.Cipher(0x2b7e151628aed2a6abf7158809cf4f3c)
        ciphertext = 0x50FE67CC996D32B6DA0937E99BAFEC60
        decrypted = aes_cipher.decrypt(ciphertext, 10)
        assert(decrypted == 0x000102030405060708090a0b0c0d0e0f)
        decrypted = misc.int_to_bytelist(aes_cipher.decrypt(ciphertext, 10), 16)
        assert(decrypted == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_invert_key_schedule(self):
        aes_cipher = aes.Cipher(0x2b7e151628aed2a6abf7158809cf4f3c)
        last_key = aes_cipher.round_keys[-4:]
        last_key.reverse()
        retrieved_key = aes.AESTools.invert_key_schedule(derived_key=last_key, rounds=10)
        assert(retrieved_key == 0x2b7e151628aed2a6abf7158809cf4f3c)

        aes_cipher = aes.Cipher(0x000102030405060708090a0b0c0d0e0f)
        last_key = aes_cipher.round_keys[-4:]
        last_key.reverse()
        retrieved_key = aes.AESTools.invert_key_schedule(derived_key=last_key, rounds=10)
        assert(retrieved_key == 0x000102030405060708090a0b0c0d0e0f)
