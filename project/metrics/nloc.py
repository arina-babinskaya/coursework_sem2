import re


def calculate(node):
    with open(node.location.file.name, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'//.*', '', content)

    lines = content.splitlines()
    nloc = sum(1 for line in lines if line.strip())

    return nloc