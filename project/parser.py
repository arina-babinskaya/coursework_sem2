from clang import cindex
from clang.cindex import CursorKind
from pathlib import Path

class CppParser:
    def __init__(self, filename: str, clang_args=None):
        self.filename = str(Path(filename).resolve())
        self.index = cindex.Index.create()
        self.clang_args = clang_args or [ "-std=c++17" ]
        self.tu = None #tu - translation_unit

    #main parser
    def parse(self):
        self.tu = self.index.parse(self.filename, args=self.clang_args)

        if not self.tu:
            raise RuntimeError("Failed to parse file")
        
        return self.tu.cursor
    
    # filter - parse except include's
    def _is_from_main_file(self, node):
        if node.location.file is None:
            return False
        return str(Path(node.location.file.name).resolve()) == self.filename

    # to avoid dublicates in code
    def _visit(self, node, callback):
        callback(node)
        for child in node.get_children():
            self._visit(child, callback)

    # functions
    def get_functions(self):
        result = []

        def callback(node):
            if node.kind == CursorKind.FUNCTION_DECL and self._is_from_main_file(node):
                result.append(node)

        self._visit(self.tu.cursor, callback)
        return result

    #methods
    def get_methods(self):
        result = []

        def callback(node):
            if node.kind == CursorKind.CXX_METHOD and self._is_from_main_file(node):
                result.append(node)

        self._visit(self.tu.cursor, callback)
        return result

    # classes ans struncts
    def get_classes(self):
        result = []

        def callback(node):
            if node.kind in [CursorKind.CLASS_DECL, CursorKind.STRUCT_DECL] and self._is_from_main_file(node):
                result.append(node)

        self._visit(self.tu.cursor, callback)
        return result

    # Cursor -> dict
    def get_function_info(self, node):
        return {
            "name": node.spelling,
            "start_line": node.extent.start.line,
            "end_line": node.extent.end.line,
            "args_count": len(list(node.get_arguments()))
        }
    # далее можно добавлять значения. для начала этого хватит

    def get_class_info(self, node):
        bases = []

        for child in node.get_children():
            if child.kind == CursorKind.CXX_BASE_SPECIFIER and child.referenced:
                bases.append(child.referenced.spelling)

        return {
            "name": node.spelling,
            "bases": bases
        }