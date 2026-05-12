class StockCounter:
    def stock(self,item,quantity):
        temp_balance = item
        
        ten_litre_milk = min(temp_balance // 10, quantity.ten_litre_milk)
        temp_balance -= ten_litre_milk * 10
        
        five_litre_milk = min(temp_balance // 5, quantity.five_litre_milk)
        temp_balance -= five_litre_milk *5
        
        two_litre_milk = min(temp_balance //2, quantity.two_litre_milk)
        temp_balance -= two_litre_milk * 2
        
        one_litre_milk = min(temp_balance //1, quantity.one_litre_milk)
        temp_balance -=one_litre_milk*1
        
        fivehundered_ml_milk = min(temp_balance // 0.5, quantity.five_hundred_ml_milk)
        temp_balance -= fivehundered_ml_milk * 0.5
        
        return [ten_litre_milk, five_litre_milk, two_litre_milk, one_litre_milk, fivehundered_ml_milk], temp_balance