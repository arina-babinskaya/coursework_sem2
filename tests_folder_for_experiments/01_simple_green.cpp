int add(int a, int b) {
    return a + b;
}

int max_value(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}

class Point {
private:
    int x;
    int y;

public:
    Point(int x_value, int y_value) : x(x_value), y(y_value) {}

    int getX() const {
        return x;
    }

    int getY() const {
        return y;
    }
};
