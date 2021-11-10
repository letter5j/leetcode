from typing import Dict, List


class FreqStack:
    max_frequency: int
    value_frequency_mapping: Dict[int, int]
    frequency_stack_mapping: Dict[int, List[int]]

    def __init__(self):
        self.max_frequency = 0
        self.value_frequency_mapping = dict()
        self.frequency_stack_mapping = dict()

    def push(self, val: int) -> None:
        self.value_frequency_mapping.setdefault(val, -1)
        frequency = self.value_frequency_mapping[val]
        frequency = frequency + 1
        self.frequency_stack_mapping.setdefault(frequency, list())
        self.frequency_stack_mapping[frequency].append(val)
        self.value_frequency_mapping[val] = frequency
        if frequency > self.max_frequency:
            self.max_frequency = frequency

    def pop(self) -> int:
        value = self.frequency_stack_mapping[self.max_frequency].pop()
        self.value_frequency_mapping[value] = self.value_frequency_mapping[value] - 1
        if len(self.frequency_stack_mapping[self.max_frequency]) == 0:
            self.frequency_stack_mapping.pop(self.max_frequency, None)
            self.max_frequency = self.max_frequency - 1

        return value
