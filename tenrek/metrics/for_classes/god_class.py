from clang.cindex import CursorKind

METHOD_LIMIT = 20
FIELD_LIMIT = 15

def calculate(node):
    classes = []

    def visit(n):
        if n.kind == CursorKind.CLASS_DECL:
            methods = 0
            fields = 0

            for child in n.get_children():
                if child.kind == CursorKind.CXX_METHOD:
                    methods += 1
                elif child.kind == CursorKind.FIELD_DECL:
                    fields += 1

            score = methods + fields
            is_god = methods > METHOD_LIMIT or fields > FIELD_LIMIT

            classes.append({
                "methods": methods,
                "fields": fields,
                "score": score,
                "is_god": is_god
            })

        for child in n.get_children():
            visit(child)

    visit(node)
    return classes
