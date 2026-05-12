class QuantityShort:
    def shortofquantity(self, quantity):
        short_quantity = 0
        # Start from the SMALLEST to satisfy "Smallest stock available"
        if quantity.five_hundred_ml_milk > 0:
            short_quantity = 0.5
            quantity.five_hundred_ml_milk -= 1
        elif quantity.one_litre_milk > 0:
            short_quantity = 1
            quantity.one_litre_milk -= 1
        elif quantity.two_litre_milk > 0:
            short_quantity = 2
            quantity.two_litre_milk -= 1
        elif quantity.five_litre_milk > 0:
            short_quantity = 5
            quantity.five_litre_milk -= 1
        elif quantity.ten_litre_milk > 0:
            short_quantity = 10
            quantity.ten_litre_milk -= 1
            
        return short_quantity