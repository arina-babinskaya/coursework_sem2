
#include <gtest/gtest.h>


TEST(ADDTest, BasicTest) {
    EXPECT_EQ(add(1, 1), /* expected */);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
