#include <iostream>

int foo(int x) {
    auto check_logic = [](int val) {
        if (val > 5 && val < 20 || val == 42) {
            return val * 2;
        }
        return val;
        
    };

    if (x > 0) {
        if (x > 2) {
            return check_logic(x) - 1;
        }
        return check_logic(x);
    }
    return 0;
}

int bar() {
    for (int i = 0; i < 10; i++) {}
    return 1;
}
