from cpp_parser import parse_func
from cpp_generator import generate_test
from cpp_template import wrap_tests


def main():
    with open("examples/sample1.cpp") as f:
        code = f.read()

    funcs = parse_func(code)

    test = ""
    for fn in funcs:
        test += generate_test(fn)

    final = wrap_tests(test)

    with open("output.cpp", "w") as f:
        f.write(final)

if __name__ == "__main__":
    main()
