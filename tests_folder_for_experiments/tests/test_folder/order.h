#pragma once
#include <string>
#include <vector>

enum class OrderStatus { NEW, PROCESSING, SHIPPED, DELIVERED, CANCELLED };

struct Item {
    std::string name;
    double price;
    int quantity;
};

class Order {
public:
    int id;
    std::vector<Item> items;
    OrderStatus status;
    bool isExpress;

    Order(int id, bool express) : id(id), status(OrderStatus::NEW), isExpress(express) {}
};
