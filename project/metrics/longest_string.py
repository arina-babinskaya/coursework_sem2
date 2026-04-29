def calculate(node):
    max_length = 0

    try:
        with open(node.location.file.name, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                max_length = max(max_length, len(line.rstrip('\n')))
    except:
        pass

    return max_length
