from collections import Counter

class InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        is_order_valid = False

    def run_allocation(self):
        print(order, inventory)
        total_inventory = self.parse_inventory()
        if not(self.check_inventory_have_item(total_inventory)):
            self.is_order_valid = False;

    def parse_inventory(self):
        temp_inventory = {}
        for x in self.inventory:
            temp_inventory = Counter(temp_inventory) + Counter(x['inventory'])
        
        return dict(temp_inventory)

    def calculate_inventory(self, product):
        for x in order[product]:
            print(x)

    #Call
    def check_inventory_have_item(self, inv):
        for order_item in self.order:
            if order_item not in inv:
                print("Inventory doesn't have the item in the order")
                return False

if __name__ == '__main__':
    print("Check")
    # d = dict()
    # var = input("input? ")
    # key, value = var.split()
    # d[key] = int(value)

    order = {'melon': 4, 'banana': 2, 'orange': 9}
    inventory = [{'name': 'owd', 'inventory': {'apple': 1, 'orange': 10}}, {
        'name': 'dm', 'inventory': {'banana': 5, 'orange': 5}}]
    ia = InventoryAllocator(order, inventory)
    
    print(ia.run_allocation())
