int deep_nesting(int a, int b, int c, int d, int e) {
    int result = 0;

    if (a > 0) {
        if (b > 0) {
            if (c > 0) {
                if (d > 0) {
                    if (e > 0) {
                        result = a + b + c + d + e;
                    }
                }
            }
        }
    }

    return result;
}
