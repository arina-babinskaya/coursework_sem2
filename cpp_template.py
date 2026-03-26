def wrap_tests(tests: str):
    return f"""
#include <gtest/gtest.h>

{tests}

int main(int argc, char **argv) {{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}}
"""
