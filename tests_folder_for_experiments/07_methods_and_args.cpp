class Calculator {
public:
    int sum(int a, int b) {
        return a + b;
    }

    int manyArgs(int a, int b, int c, int d, int e, int f, int g, int h) {
        return a + b + c + d + e + f + g + h;
    }

    int branchyMethod(int x) {
        if (x < 0) return -1;
        if (x == 0) return 0;
        if (x == 1) return 1;
        if (x == 2) return 2;
        return 100;
    }
};
