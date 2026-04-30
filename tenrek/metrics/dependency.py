from clang.cindex import CursorKind
from file_dependency import calculate as file_calc


def calculate(node):
    includes = set()
    types = set()

    tu = node.translation_unit  # not just node.tu?

    try:
        for inc in tu.get_includes():
            includes.add(inc.include.name)
    except:
        pass

    def visit(n):
        if n.kind == CursorKind.TYPE_REF:
            if n.spelling:
                types.add(n.spelling)

        elif n.kind == CursorKind.TEMPLATE_REF:
            if n.spelling:
                types.add(n.spelling)

        elif n.kind == CursorKind.DECL_REF_EXPR:
            if n.type and n.type.spelling:
                types.add(n.type.spelling)

        for child in n.get_children():
            visit(child)

    visit(node)

    # --- 3. очистка ---
    current_name = getattr(node, "spelling", None)

    if current_name:
        types = {t for t in types if current_name not in t}

    # убираем примитивы
    primitives = {
        "int", "char", "float", "double", "void", "bool",
        "short", "long", "size_t"
    }

    cleaned_types = set()
    for t in types:
        base = t.replace("const", "").replace("&", "").replace("*", "").strip()
        if base not in primitives:
            cleaned_types.add(base)

    types = cleaned_types

    # --- 4. результат ---
    return {
        "includes": len(includes),
        "types": len(types),
        "total": len(includes) + len(types),
        "include_list": list(includes),
        "type_list": list(types)
    }
