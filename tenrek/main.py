from parser import CppParser
from analyzer import ComplexityAnalyzer
import json


def debug_print_ast(node, indent=0, file=None):
    line = "  " * indent + f"{node.kind} | {node.spelling}\n"
    file.write(line)
    for child in node.get_children():
        debug_print_ast(child, indent + 1, file)


def main():
    parser = CppParser("test_file.cpp")

    root = parser.parse()

    functions = parser.get_functions()

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== AST ===\n")
        debug_print_ast(root, file=f)

        f.write("\n=== FUNCTIONS ===\n")
        for func in functions:
            info = parser.get_function_info(func)
            f.write(str(info) + "\n")


    analyzer = ComplexityAnalyzer(parser)
    results = analyzer.analyze()

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()