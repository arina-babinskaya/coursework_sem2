#pragma once
#include "order.h"
#include "discount_calc.h"
#include <iostream>

class OrderProcessor {
private:
    int processedCount = 0;

public:
    double processOrder(Order& order) {
        if (order.status != OrderStatus::NEW) {
            return 0.0;
        }

        order.status = OrderStatus::PROCESSING;
        double rawTotal = 0.0;

        // Цикл для расчета базовой стоимости
        for (size_t i = 0; i < order.items.size(); ++i) {
            rawTotal += order.items[i].price * order.items[i].quantity;
        }

        // Вызов связанного класса
        double discountRate = DiscountCalculator::calculateDiscount(order, rawTotal);
        double finalTotal = rawTotal * (1.0 - discountRate);

        if (order.isExpress) {
            finalTotal += 15.0; // Стоимость доставки
        }

        order.status = OrderStatus::SHIPPED;
        processedCount++;
        
        return finalTotal;
    }

    int getProcessedCount() const { return processedCount; }
};
