from dataclasses import dataclass, field
from typing import List, Callable

@dataclass
class Operation:
    apply: Callable
    inverse: Callable

    def __call__(self, *args, **kwargs):
        if len(args) == 1 and type(args[0]) is SequenceItem:
            seq_item = args[0]
            return SequenceItem(seq_item.orig_index, operations_applied=[*seq_item.operations_applied, self])
        else:
            return self.apply(*args, **kwargs)

    def invert(self):
        return Operation(self.inverse, self.apply)

@dataclass
class SequenceItem:
    orig_index: int
    operations_applied: List[Operation] = field(default_factory=list)

class InputSequence:
    def __init__(self, length):
        self.items = [SequenceItem(i) for i in range(length)]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __iter__(self):
        yield from self.items

    def __str__(self):
        return str(self.items)

class OutputSequence:
    def __init__(self, in_seq):
        self.items = [None for _ in range(len(in_seq))]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __iter__(self):
        yield from self.items

    def __str__(self):
        return str(self.items)

def invert_operations(operations, initial):
    value = initial
    for operation in reversed(operations):
        value = operation.inverse(value)
    return value

def run(mutator, in_seq):
    result = [item for item in in_seq]
    mutator(in_seq, result)
    return __coerce(result)

def invert(mutator, sequence_len):
    analysis_in_seq = InputSequence(sequence_len)
    analysis_out_seq = OutputSequence(analysis_in_seq)
    mutator(analysis_in_seq, analysis_out_seq)

    def retromutator(in_seq):
        out_seq = [item for item in in_seq]

        for index, mutated_item in enumerate(analysis_out_seq):
            out_seq[mutated_item.orig_index] = invert_operations(mutated_item.operations_applied, in_seq[index])

        return out_seq

    return retromutator

def find(mutator, target):
    result = invert(mutator, len(target))(target)

    return __coerce(result)

def __coerce(result):
    # Quality of life: If all the values in 'result' are characters, we can transform the result into a string:
    if all([type(item) is str and len(item) == 1] for item in result):
        return "".join(result)

    return result
