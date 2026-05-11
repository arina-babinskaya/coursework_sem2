from clang.cindex import CursorKind
from .fifo_help_functions import get_all_types_from_type, walk


# the number of external types on which this class depends
def calculate(source_class, parser):
    source_name = source_class.spelling
    used = set()

    def add_types(type_obj):
        if not type_obj:
            return

        for t in get_all_types_from_type(type_obj):
            if t and t != source_name:
                used.add(t)

    for child in source_class.get_children():

        if child.kind == CursorKind.CXX_BASE_SPECIFIER:
            add_types(child.type)

        elif child.kind == CursorKind.FIELD_DECL:
            add_types(child.type)

        elif child.kind in [CursorKind.CXX_METHOD, CursorKind.CONSTRUCTOR]:
            for arg in child.get_arguments():
                add_types(arg.type)
            
            if hasattr(child, "result_type"):
                add_types(child.result_type)

            for node in walk(child):
                if node.kind == CursorKind.VAR_DECL:
                    add_types(node.type)
                
                elif node.kind == CursorKind.TYPE_REF:
                    add_types(node.type)
                
                elif node.kind == CursorKind.CALL_EXPR and node.referenced:
                    parent = node.referenced.semantic_parent
                    if (
                        parent 
                        and parent.spelling 
                        and parent.spelling != source_name 
                        and parent.kind in [CursorKind.CLASS_DECL, CursorKind.STRUCT_DECL]
                    ):
                        add_types(parent.spelling)

    return len(used)