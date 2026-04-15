#returns a set of values
# in future: add possibility to make personalized comments about input format
from typing import List, Tuple

def normalize_type(t: str) -> str:
    t = t.replace("const", "").replace("&", "").replace("*", "")
    return " ".join(t.split())

#парсинг вложенных типов будет здесь -мне кажется так удобнее
def split_template_args(s: str) -> List[str]:
    args = []
    depth = 0
    current = ""

    for c in s:
        if c == "<":
            depth += 1
            current += c
        elif c == ">":
            depth -= 1
            current += c
        elif c == "," and depth == 0:
            args.append(current.strip())
            current = ""
        else:
            current += c

    if current:
        args.append(current.strip())

    return args


def parse_template(t: str) -> Tuple[str, List[str]]:
    t = normalize_type(t)

    if "<" not in t:
        return t, []

    base = t[:t.find("<")].strip()
    inside = t[t.find("<") + 1 : -1]

    args = split_template_args(inside)
    return base, args

def get_basic_values(base_type: str) -> List[str]: #решила выделить эту часть в отдельную функцию
    if base_type in {"int"}:
        return ["0", "1", "-1", "42", str(2**31 - 1), str(-2**31)]
    if base_type in {"short"}:
        return ["0", "1", "-1", "42", str(2**15 - 1), str(-2**15)]
    if base_type in {"long long"}:
        return ["0", "1", "-1", "42", str(2**63 - 1), str(-2**63)]
    
    if base_type == "int8_t":
        return ["0", "1", "-1", "127", "-128"]
    if base_type == "int16_t":
        return ["0", "1", "-1", str(2**15 - 1), str(-2**15)]
    if base_type == "int32_t":
        return ["0", "1", "-1", str(2**31 - 1), str(-2**31)]
    if base_type == "int64_t":
        return ["0", "1", "-1", str(2**63 - 1), str(-2**63)]

    if base_type == "uint8_t":
        return ["0", "1", "255"]
    if base_type == "uint16_t":
        return ["0", "1", str(2**16 - 1)]
    if base_type == "uint32_t":
        return ["0", "1", str(2**32 - 1)]
    if base_type == "uint64_t":
        return ["0", "1", str(2**64 - 1)]
    
    if base_type in {"unsigned int"}:
        return ["0", "1", "42", str(2**32 - 1)]
    if base_type in {"unsigned long"}:
        return ["0", "1", "42", str(2**64 - 1)]
    
    if base_type in {"float"}:
        return ["0.0", "1.0", "-1.0", "3.14", "3.4e38", "-3.4e38"]
    if base_type in {"double"}:
        return ["0.0", "1.0", "-1.0", "3.14", "1.7e308", "-1.7e308"]
    
    if base_type == "bool":
        return ["true", "false"]
    
    if base_type == "char" :
        return ["'a'", "'\\0'", "'Z'", "'\\x7F'"]
    if base_type in {"std::string", "string"}:
        return ['""', '"test"', '"' + 'a'*1000 + '"']

    return [f"/*UNKNOWEN_TYPE:{base_type}*/"]


def get_values(arg_type: str) -> List[str]:
    base_type = normalize_type(arg_type)
    return get_basic_values(base_type)







# В РАЗРАБОТКЕ - НЕ СМОТРЕТЬ

# def get_values(arg_type: str) -> List[str]:
#     base, template_args = parse_template(arg_type)

#     # ---------- VECTOR ----------
#     if base in {"std::vector", "vector"} and len(template_args) == 1:
#         inner_vals = get_values(template_args[0])

#         result = ["{}"]

#         for v in inner_vals[:2]:
#             result.append(f"{{{v}}}")

#         if len(inner_vals) >= 2:
#             result.append(f"{{{inner_vals[0]}, {inner_vals[1]}}}")

#         return result

#     # ---------- SET ----------
#     if base in {"std::set", "set"} and len(template_args) == 1:
#         inner_vals = get_values(template_args[0])

#         result = ["{}"]

#         for v in inner_vals[:2]:
#             result.append(f"{{{v}}}")

#         if len(inner_vals) >= 2:
#             result.append(f"{{{inner_vals[0]}, {inner_vals[1]}}}")

#         return result

#     # ---------- PAIR ----------
#     if base in {"std::pair", "pair"} and len(template_args) == 2:
#         left_vals = get_values(template_args[0])
#         right_vals = get_values(template_args[1])

#         result = []

#         for l in left_vals[:2]:
#             for r in right_vals[:2]:
#                 result.append(f"{{{l}, {r}}}")

#         return result

#     # ---------- MAP ----------
#     if base in {"std::map", "map"} and len(template_args) == 2:
#         key_vals = get_values(template_args[0])
#         val_vals = get_values(template_args[1])

#         result = ["{}"]

#         for k in key_vals[:2]:
#             for v in val_vals[:2]:
#                 result.append(f"{{{{{k}, {v}}}}}")

#         if len(key_vals) >= 2 and len(val_vals) >= 2:
#             result.append(
#                 f"{{{{{key_vals[0]}, {val_vals[0]}}}, {{{key_vals[1]}, {val_vals[1]}}}}}"
#             )

#         return result

#     # ---------- POINTER ----------
#     if "*" in arg_type:
#         return ["nullptr"]

#     # ---------- BASE ----------
#     return get_basic_values(base)
    

    
