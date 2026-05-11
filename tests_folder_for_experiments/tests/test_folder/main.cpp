#include "order.h"
#include "order_processor.h"
#include <iostream>

int main() {
    OrderProcessor processor;

    // Создаем тестовый заказ
    Order order1(101, true);
    order1.items.push_back({"Laptop", 1200.0, 1});
    order1.items.push_back({"Mouse", 25.0, 3});
    order1.items.push_back({"Cable", 10.0, 12});

    std::cout << "--- Processing Order 101 ---" << std::endl;
    double price1 = processor.processOrder(order1);
    std::cout << "Final Price: $" << price1 << std::endl;

    // Создаем второй заказ для проверки логики
    Order order2(102, false);
    order2.items.push_back({"Keyboard", 45.0, 1});
    
    double price2 = processor.processOrder(order2);
    std::cout << "\n--- Processing Order 102 ---" << std::endl;
    std::cout << "Final Price: $" << price2 << std::endl;

    std::cout << "\nTotal orders processed: " << processor.getProcessedCount() << std::endl;

    return 0;
}
