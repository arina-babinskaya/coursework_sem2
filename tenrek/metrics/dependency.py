from clang.cindex import CursorKind
from tenrek.metrics.file_dependency import calculate as file_calc
# CBO (Coupling Between Objects)


def calculate(node):
    includes = set()
    types = set()

    tu = node.translation_unit 

    file_result = file_calc(node)
    includes.update(file_result["include_list"])

    def normalize_type(type_name: str) -> str:
        if not type_name:
            return ""

        garbage = ["const", "&", "*", "volatile", "struct", "class"]
        result = type_name

        for g in garbage:
            result = result.replace(g, "")

        return " ".join(result.split()).strip()

    def visit(n):
        if n.kind in {
            CursorKind.TYPE_REF,
            CursorKind.TEMPLATE_REF,
        }:
            if n.spelling:
                types.add(n.spelling)

        elif n.kind == CursorKind.DECL_REF_EXPR:
            if n.type and n.type.spelling:
                types.add(n.type.spelling)

        for child in n.get_children():
            visit(child)

    visit(node)

    current_name = getattr(node, "spelling", "")

    if current_name:
        types = {t for t in types if current_name not in t}

    primitives = {
        "int", "char", "float", "double", "void", "bool",
        "short", "long", "size_t", "unsigned", "signed",
        "wchar_t", "char16_t", "char32_t"
    }

    cleaned_types = set()
    for t in types:
        base = normalize_type(t)

        if base and base not in primitives:
            cleaned_types.add(base)

    return {
        "includes": len(includes),
        "types": len(cleaned_types),
        "total": len(includes) + len(cleaned_types),
        "include_list": sorted(includes),
        "type_list": sorted(cleaned_types),
    }
