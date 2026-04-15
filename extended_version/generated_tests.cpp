#include <gtest/gtest.h>
#include "level1.cpp"


TEST(Add_Test,aZero_bZero) {
    auto result = add(0, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aOne_bZero) {
    auto result = add(1, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aNegative_bZero) {
    auto result = add(-1, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aVal_bZero) {
    auto result = add(42, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aMax_Val_bZero) {
    auto result = add(2147483647, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aMin_Val_bZero) {
    auto result = add(-2147483648, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aZero_bOne) {
    auto result = add(0, 1);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aZero_bNegative) {
    auto result = add(0, -1);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aZero_bVal) {
    auto result = add(0, 42);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aZero_bMax_Val) {
    auto result = add(0, 2147483647);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Add_Test,aZero_bMin_Val) {
    auto result = add(0, -2147483648);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Subtract_Test,aZero_bZero) {
    auto result = subtract(0.0, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aOne_bZero) {
    auto result = subtract(1.0, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aNegative_bZero) {
    auto result = subtract(-1.0, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aVal_bZero) {
    auto result = subtract(3.14, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aMax_Val_bZero) {
    auto result = subtract(3.4e38, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aMin_Val_bZero) {
    auto result = subtract(-3.4e38, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aZero_bOne) {
    auto result = subtract(0.0, 1.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aZero_bNegative) {
    auto result = subtract(0.0, -1.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aZero_bVal) {
    auto result = subtract(0.0, 3.14);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aZero_bMax_Val) {
    auto result = subtract(0.0, 3.4e38);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Subtract_Test,aZero_bMin_Val) {
    auto result = subtract(0.0, -3.4e38);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Multiply_Test,aZero_bZero) {
    auto result = multiply(0, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Multiply_Test,aOne_bZero) {
    auto result = multiply(1, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Multiply_Test,aVal_bZero) {
    auto result = multiply(42, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Multiply_Test,aMax_Val_bZero) {
    auto result = multiply(4294967295, 0);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Multiply_Test,aZero_bOne) {
    auto result = multiply(0, 1);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Multiply_Test,aZero_bVal) {
    auto result = multiply(0, 42);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Multiply_Test,aZero_bMax_Val) {
    auto result = multiply(0, 4294967295);
    EXPECT_EQ(result, /*expected*/);
}

TEST(Divide_Test,numeratorZero_denominatorZero) {
    auto result = divide(0.0, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorOne_denominatorZero) {
    auto result = divide(1.0, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorNegative_denominatorZero) {
    auto result = divide(-1.0, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorVal_denominatorZero) {
    auto result = divide(3.14, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorMax_Val_denominatorZero) {
    auto result = divide(1.7e308, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorMin_Val_denominatorZero) {
    auto result = divide(-1.7e308, 0.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorZero_denominatorOne) {
    auto result = divide(0.0, 1.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorZero_denominatorNegative) {
    auto result = divide(0.0, -1.0);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorZero_denominatorVal) {
    auto result = divide(0.0, 3.14);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorZero_denominatorMax_Val) {
    auto result = divide(0.0, 1.7e308);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Divide_Test,numeratorZero_denominatorMin_Val) {
    auto result = divide(0.0, -1.7e308);
    EXPECT_NEAR(result, /*expected*/, 1e-5);
}

TEST(Logical_and_Test,aTrue_bTrue) {
    auto result = logical_and(true, true);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Logical_and_Test,aFalse_bTrue) {
    auto result = logical_and(false, true);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Logical_and_Test,aTrue_bFalse) {
    auto result = logical_and(true, false);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aZero_bZero) {
    auto result = is_equal(0, 0);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aOne_bZero) {
    auto result = is_equal(1, 0);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aNegative_bZero) {
    auto result = is_equal(-1, 0);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aVal_bZero) {
    auto result = is_equal(42, 0);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aMax_Val_bZero) {
    auto result = is_equal(9223372036854775807, 0);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aMin_Val_bZero) {
    auto result = is_equal(-9223372036854775808, 0);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aZero_bOne) {
    auto result = is_equal(0, 1);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aZero_bNegative) {
    auto result = is_equal(0, -1);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aZero_bVal) {
    auto result = is_equal(0, 42);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aZero_bMax_Val) {
    auto result = is_equal(0, 9223372036854775807);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}

TEST(Is_equal_Test,aZero_bMin_Val) {
    auto result = is_equal(0, -9223372036854775808);
    EXPECT_TRUE(result);  // or EXPECT_FALSE
}


#ifndef HAS_CUSTOM_MAIN
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
#endif
