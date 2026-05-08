from storage import StorageSection
from stock import StockCounter
from shortquantity import QuantityShort

class CommerceApp:
    def __init__(self):
        self.storage = StorageSection()
        self.stock = StockCounter()
        self.short_quantity = QuantityShort()
        
    def start_shopping(self):
        print(f"\n {'*' * 20} WELCOME TO ECAMART {'*' * 20}\n")
        
        # FIX 1: Added () to call the method
        total_milk_stock = self.storage.milkcapacity() 
        
        try:
            user_input = input("Hello, enter your name: ")
            qty_input = float(input(f"Hi {user_input},currently the available quantity is {total_milk_stock} enter the liters required: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

        # Capacity Check
        if qty_input > total_milk_stock:
            print(f"Sorry {user_input}, we are short of stock! Available: {total_milk_stock}L")
            return

        # Get values from stock counter
        packs, remaining = self.stock.stock(qty_input, self.storage)
        
        # Calculation
        ten_val = packs[0] * 10
        five_val = packs[1] * 5
        two_val = packs[2] * 2
        one_val = packs[3] * 1
        half_val = packs[4] * 0.5
        
        total_given = ten_val + five_val + two_val + one_val + half_val

        # Update Inventory
        self.storage.ten_litre_milk -= packs[0]
        self.storage.five_litre_milk -= packs[1]
        self.storage.two_litre_milk -= packs[2] 
        self.storage.one_litre_milk -= packs[3]
        self.storage.five_hundred_ml_milk -= packs[4]

        # Shortfall Logic
        if remaining > 0:
            print(f"Notice: Exact quantity not available. Shortfall: {remaining}L")
            # FIX 2: Ensure this name matches your class method exactly
            extra = self.short_quantity.shortofquantity(self.storage)
            total_given += extra
            print(f"✅ Added smallest available pack: {extra}L")

        print(f"Final Quantity Delivered: {total_given}L")
        
        # FIX 3: Call the display function here
        self.display_remaining_stock()

    def display_remaining_stock(self):
        s = self.storage
        print(f"\n{'*' * 20} Remaining Stock {'*' * 20}")
        print(f"10L: {s.ten_litre_milk} | 5L: {s.five_litre_milk} | 2L: {s.two_litre_milk} | 1L: {s.one_litre_milk} | 0.5L: {s.five_hundred_ml_milk}")
        print(f"Total available now: {s.milkcapacity()}L")
        print(f"{'*' * 60}\n")

if __name__ == "__main__":
    app = CommerceApp()
    while True:
        app.start_shopping()
        choice = input("Do you want to continue shopping? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for shopping with us! Have a great day!")
            break