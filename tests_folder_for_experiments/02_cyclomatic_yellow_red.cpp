int complex_decision(int x, int y, int z) {
    int result = 0;

    if (x > 0) result++;
    if (x > 10) result++;
    if (y > 0) result++;
    if (y > 10) result++;
    if (z > 0) result++;
    if (z > 10) result++;

    for (int i = 0; i < x; i++) {
        if (i % 2 == 0) {
            result += i;
        } else {
            result -= i;
        }
    }

    while (result < 100) {
        if (result % 3 == 0) {
            result += 5;
        } else if (result % 5 == 0) {
            result += 7;
        } else {
            result++;
        }
    }

    switch (z) {
        case 1: result += 1; break;
        case 2: result += 2; break;
        case 3: result += 3; break;
        case 4: result += 4; break;
        default: result += 10; break;
    }

    return result;
}
