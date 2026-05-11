const char* long_message() {
    return "This is a very long string that should trigger the longest_string metric because it intentionally exceeds common line length thresholds used in code style checks and readability guidelines.";
}

int small_function() {
    return 42;
}
