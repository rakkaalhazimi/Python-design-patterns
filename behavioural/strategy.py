"""
Strategy pattern is a behavioural design that lets you to selecting algorithms in the runtime

In the code below, we will use discount price example
"""

import math
from abc import ABC, abstractmethod

# 1. Create promotion abstrac base class
class Promotions(ABC):
    @abstractmethod
    def discount(self):
        ...

# 2. Create pricing class to calculate how much do you need to pay
#    It also include promotion 
class Pricing:
    def __init__(self, total):
        self.total = total
        self.reduced_total = math.inf

    def use_promotion(self, promotion: Promotions):
        self.reduced_total = promotion.discount(self.total)

    def pay(self):
        return min(self.total, self.reduced_total)


# 3. Create the concrete promotion class
#    Different promotion have their own discount rule
class HotPromotion(Promotions):
    def discount(self, total: int):
        """
        Gives 50% discount for the total cost that more than 1 milion, else gives only 10% discount
        """
        return total * 0.5 if total > 1_000_000 else total * 0.9


class GoldPromotion(Promotions):
    def discount(self, total: int):
        """
        Gives 70% discount for the total cost that more than 0.5 milion, else gives no discount
        """
        return total * 0.7 if total > 100_000 else total


class UltraPromotion(Promotions):
    def discount(self, total: int):
        """
        Gives 60% discount for the total cost that more than 3 milion, else gives no discount
        """
        return total * 0.6 if total > 3_000_000 else total


if __name__ == "__main__":
    total = 1_000_000
    pricing = Pricing(total)
    
    hot_promotion = HotPromotion()
    ultra_promotion = UltraPromotion()
    gold_promotion = GoldPromotion()

    pricing.use_promotion(ultra_promotion)
    print(pricing.pay())
