class StorageSection:
    
    def __init__(self):   #available in the storage section
        self.ten_litre_milk = 2
        self.five_litre_milk = 4
        self.two_litre_milk = 10
        self.one_litre_milk = 0
        self.five_hundred_ml_milk = 5

    def milkcapacity(self):
        return (self.ten_litre_milk * 10)+\
               (self.five_litre_milk * 5)+\
                (self.two_litre_milk * 2)+\
                (self.one_litre_milk * 1)+\
                (self.five_hundred_ml_milk * 0.5)