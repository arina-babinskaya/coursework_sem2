#pragma once
#include "order.h"

class DiscountCalculator {
public:
    // Высокая цикломатическая сложность из-за обилия условий
    static double calculateDiscount(const Order& order, double totalSum) {
        double discount = 0.0;

        if (order.items.size() > 5) {
            discount += 0.05;
            if (totalSum > 1000.0) {
                discount += 0.05;
                if (order.isExpress) {
                    discount -= 0.02; // Штраф за срочность
                }
            }
        } else if (order.items.size() > 2) {
            discount += 0.02;
        }

        // Глубокая вложенность
        for (const auto& item : order.items) {
            if (item.quantity > 10) {
                if (item.price > 100.0) {
                    discount += 0.03;
                }
            }
        }

        if (discount > 0.30) {
            discount = 0.30; // Максимальная скидка
        }

        return discount;
    }
};
