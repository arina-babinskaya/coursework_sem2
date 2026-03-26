import re

FUNC_PATTERN = re.compile ( 
    r'(\w+)\s+(\w+)\((.*?)\)\s*\{',
    re.DOTALL
)

def parse_func(code: str):
    funcs = []

    for match in FUNC_PATTERN.finditer(code):
        return_type = match.group(1)
        name = match.group(2)
        args = match.group(3)

        arg_list = []
        if args.strip():
            for arg in args.split(','):
                arg_type, arg_name = arg.strip().split()
                arg_list.append((arg_type, arg_name))

        funcs.append({
            "return_type": return_type,
            "name": name,
            "args": arg_list
        })

    return funcs


