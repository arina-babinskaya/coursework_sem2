from clang.cindex import CursorKind


def walk(node):
    yield node
    for child in node.get_children():
        yield from walk(child)


def get_all_types_from_type(t):
    names = []
    
    canonical = t.get_canonical()
    decl = canonical.get_declaration()

    if decl and decl.spelling:
        names.append(decl.spelling)
    elif canonical.spelling:
        names.append(canonical.spelling.split("::")[-1].strip())

    num_args = canonical.get_num_template_arguments()

    if num_args > 0:
        for i in range(num_args):
            arg_type = canonical.get_template_argument_type(i)
            if arg_type:
                names.extend(get_all_types_from_type(arg_type))

    return names


# does another class use target_name
def class_uses_type(clas, target_name): 
    for node in walk(clas):
        if node.kind == CursorKind.FIELD_DECL:
            if target_name in get_all_types_from_type(node.type):
                return True
            
        elif node.kind == CursorKind.TYPE_REF:
            if node.spelling == target_name:
                return True

        elif node.kind == CursorKind.CALL_EXPR and node.referenced:
            parent = node.referenced.semantic_parent
            if parent and parent.spelling == target_name:
                return True
    return False


# does function/method use target_name
def callable_uses_type(func, target_name):
    for arg in func.get_arguments():
        if target_name in get_all_types_from_type(arg.type):
            return True

    if hasattr(func, "result_type"): #safely check if it exists
        if target_name in get_all_types_from_type(func.result_type):
            return True

    for node in walk(func):
        if node.kind == CursorKind.VAR_DECL:
            if target_name in get_all_types_from_type(node.type):
                return True

        elif node.kind == CursorKind.TYPE_REF:
            if node.spelling == target_name:
                return True

        elif node.kind == CursorKind.CALL_EXPR and node.referenced:
            parent = node.referenced.semantic_parent
            if parent and parent.spelling == target_name:
                return True
        
        elif node.kind == CursorKind.CONSTRUCTOR:
            if node.spelling == target_name:
                return True

    return False


