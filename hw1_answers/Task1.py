class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, monetary_amount):
        self.discount += monetary_amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        return total_before_discount - self.discount

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"{item} ... £{price}")

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0

register_1 = CashRegister()


register_1.add_item({'Skirt': 25.00})
register_1.add_item({'Shoes': 50.00})
register_1.add_item({'Bag': 45.50})

register_1.remove_item('Bag')


register_1.show_items()
discount = 10.00
register_1.apply_discount(discount)
print('_________________')
print(f'Discount -£{discount}')
print(f'Total: {register_1.get_total()}')
register_1.reset_register()
