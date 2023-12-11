def fairy_parser(file_path: str) -> int:
    with open(file_path, 'r') as file:
        for line in file:
            yield 10 * find_first(line) + find_last(line)

def find_first(text: str) -> int:
    for c in text:
        if c.isdigit():
            return int(c)

def find_last(text: str) -> int:
    return find_first(text[::-1])

print(sum(fairy_parser('./input.txt')))