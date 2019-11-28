import retromutator
import retromutator.ops as ops

def convert_to_ascii(in_seq, out_seq):
    for i, item in enumerate(in_seq):
        out_seq[i] = ops.ord(in_seq[i])

# >>> retromutator.run(convert_to_ascii, "Hello, world!")
# [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]

ascii_bytes = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
print(retromutator.find(convert_to_ascii, ascii_bytes)) # Hello, world!

def caesar_shift_3(in_seq, out_seq):
    for i, item in enumerate(in_seq):
        out_seq[i] = ops.chr(ops.add(3) (ops.ord(in_seq[i])))

# >>> retromutator.run(caesar_shift_3, "Hello, world!")
# 'Khoor/#zruog$'
# >>> retromutator.find(caesar_shift_3, 'Khoor/#zruog$')
# 'Hello, world!'