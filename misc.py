def bytelist_to_int(l, b_order):
    bytes_list = bytes(l)
    return int.from_bytes(bytes_list, byteorder=b_order)


def int_to_bytelist(x, b_order, size):
    bytes_list = x.to_bytes((x.bit_length() + 7) // 8, byteorder=b_order)
    lb = []
    for b in bytes_list:
        lb.append(int(b))
    while len(lb) < size:
        lb.insert(0, 0)
    return lb


def bytelist_to_wordlist(l: list):
    wordlist = []
    #word = int of 8bytes
    #we assume that bytelist size is multiple of 8
    for i in range(len(l) // 8):
        word = l[(i*8):(i*8)+8]
        wordlist.append(bytelist_to_int(word, 'big'))
    return wordlist


def wordlist_to_bytelist(w: list):
    bytelist = []
    for word in w:
        word_bytes = int_to_bytelist(word, 'big', 8)
        for b in word_bytes:
            bytelist.append(b)
    return bytelist


def int_to_matrix(text):
    matrix = []
    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xFF
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[i // 4].append(byte)
    return matrix


def matrix_to_int(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[i][j] << (120 - 8 * (4 * i + j)))
    return text


def assemble_lists(ll, ltoappend):
    return [x + [y] for x in ll for y in ltoappend]


def list_to_matrix(l):
    matrix = []
    for i in range(16):
        if i % 4 == 0:
            matrix.append([l[i]])
        else:
            matrix[i // 4].append(l[i])
    return matrix
