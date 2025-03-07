class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0
        self.last_item_details = None  # Stores (title, price, quantity)

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction = price * quantity
        self.last_item_details = (title, price, quantity)

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            message = f"After the discount, the total comes to ${self.total}."
            print(message)
            return message
        else:
            message = "There is no discount to apply."
            print(message)
            return message

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.last_item_details:
            title, _, quantity = self.last_item_details
            for _ in range(quantity):
                if self.items and self.items[-1] == title:
                    self.items.pop()
        self.last_transaction = 0
        self.last_item_details = None
