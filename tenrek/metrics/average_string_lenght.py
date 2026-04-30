def calculate(node):
    total_length = 0
    line_count = 0

    with open(node.location.file.name, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            total_length += len(line.rstrip('\n'))
            line_count += 1

    if line_count == 0:
        return 0

    return total_length / line_count