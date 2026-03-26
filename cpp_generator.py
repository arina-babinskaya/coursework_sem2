def generate_test(func):
    name = func["name"]

    args = func["args"]
    test_args = []

    for arg_type, arg_name in args:
        if arg_type in ["int", "float"]:
            test_args.append("1")
        else:
            test_args.append("0")

    args_str = ", ".join(test_args)

    return f"""
TEST({name.upper()}Test, BasicTest) {{
    EXPECT_EQ({name}({args_str}), /* expected */);
}}
"""