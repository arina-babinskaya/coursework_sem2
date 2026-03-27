import clang.cindex

class cppParser:
    def __init__(self):
        self.index = clang.cindex.Index.create() #make main odject

    def parse_file(self, file_path):
        tu = self.index.parse(file_path, args=['-std=c++20']) #translation unit
        funcs = []

        for node in tu.cursor.get_children():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECLARATION: #need function typr only
                func_data = {
                    "name": node.spelling, #returns spelling of node
                    "return_type": node.return_type.spelling,
                    "args": []
                }
                for arg in node.get_arguments():
                    func_data["args"].append({
                        "type": arg.type.spelling, #detection of links and const
                        "name": arg.spelling
                    })
                funcs.append(func_data)
        return funcs


