from typing import List

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums = {str(x): x for x in range(1,10)}
nums.update({word: i+1 for i, word in enumerate(words)})
nums.update({word: i+1 for i, word in enumerate(x[::-1] for x in words)})

min_num_length = min(len(x) for x in nums)
max_num_length = max(len(x) for x in nums)


def fairy_numbers_generator(text: str) -> str:
    for i in range(len(text)):
        for j in range(min_num_length, max_num_length + 1):
            if i+j <= len(text):
                yield text[i:i+j]


def fairy_parser(file_path: str) -> int:
    with open(file_path, 'r') as file:
        for line in file:
            yield 10 * find_first(line) + find_last(line)

def find_first(text: str) -> int:
    for word in fairy_numbers_generator(text):
        if word in nums:
            return nums[word]

def find_last(text: str) -> int:
    return find_first(text[::-1])

print(sum(fairy_parser('./input.txt')))