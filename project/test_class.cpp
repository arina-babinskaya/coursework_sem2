#include <iostream>
#include <vector>
#include <string>

// Нормальный класс
class User {
private:
    std::string name;
    int age;

public:
    User(const std::string& name, int age) : name(name), age(age) {}

    void printInfo() {
        std::cout << "Name: " << name << ", Age: " << age << std::endl;
    }

    int getAge() const {
        return age;
    }
};

// Пограничный класс
class DataProcessor {
private:
    std::vector<int> data;

public:
    void add(int value) {
        data.push_back(value);
    }

    int sum() {
        int s = 0;
        for (int v : data) s += v;
        return s;
    }

    double average() {
        if (data.empty()) return 0;
        return (double)sum() / data.size();
    }

    void clear() {
        data.clear();
    }

    int max() {
        int m = data[0];
        for (int v : data) if (v > m) m = v;
        return m;
    }

    int min() {
        int m = data[0];
        for (int v : data) if (v < m) m = v;
        return m;
    }

    void print() {
        for (int v : data) std::cout << v << " ";
        std::cout << std::endl;
    }
};

// Явный God Class
class SuperManager {
private:
    int config;
    std::string name;
    std::vector<int> cache;
    std::vector<std::string> logs;
    double value;
    bool flag;
    int counter;
    std::string state;
    std::vector<double> metrics;
    int errorCode;

public:
    // методы работы с конфигом
    void loadConfig() {}
    void saveConfig() {}
    void resetConfig() {}

    // логика
    void process() {}
    void processData() {}
    void processMoreData() {}

    // логирование
    void logInfo(const std::string&) {}
    void logWarning(const std::string&) {}
    void logError(const std::string&) {}

    // работа с кэшем
    void addToCache(int v) { cache.push_back(v); }
    void clearCache() { cache.clear(); }
    int getFromCache(int i) { return cache[i]; }

    // состояние
    std::string getState() { return state; }

    // метрики
    void addMetric(double m) { metrics.push_back(m); }
    double getMetric(int i) { return metrics[i]; }

    // счётчики
    void increment() { counter++; }
    void decrement() { counter--; }
    int getCounter() { return counter; }

    // misc
    void start() {}
    void stop() {}
    void restart() {}
    void update() {}
    void shutdown() {}
    void init() {}
    void cleanup() {}
    void debug() {}
    void validate() {}
};

int main() {
    User u("Alice", 25);
    u.printInfo();

    DataProcessor dp;
    dp.add(1);
    dp.add(2);
    dp.add(3);
    dp.print();

    SuperManager sm;
    sm.init();
    sm.process();

    return 0;
}
