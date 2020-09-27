


class Cipher:
    def subkeys_generation(self, key: list):
        if len(key) <= 128:
            n = 128
            key = key + [0] * (n - len(key))
        elif len(key) <= 192:
            n = 192
            key = key + [0] * (n - len(key))
        elif len(key) <= 256:
            n = 256
            key = key + [0] * (n - len(key))
        else:
            exit(1)
        k = n/64


