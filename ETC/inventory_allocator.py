from collections import Counter

class InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory

    def allocation(self):
        print(order, inventory)

        total_inventory = {}
        for x in inventory:
            total_inventory = Counter(total_inventory) + Counter(x['inventory'])
            
        print(total_inventory)
        

    def parse_inventory(self, item):
        i = 4

    def calculate_inventory(self, product):
        for x in order[product]:
            print(x)

    #Call
    def check_inventory_have_item(self, item):
        for inventory_dict in inventory:
            for item_in_inventory in inventory_dict['inventory']:
                if item_in_inventory != item:
                    print(item_in_inventory)
                    print(item)
                    print("Inventory doesn't have what you order")
                    return False


if __name__ == '__main__':
    print("Check")
    # d = dict()
    # var = input("input? ")
    # key, value = var.split()
    # d[key] = int(value)

    order = {'banana': 2, 'orange': 9}
    inventory = [{'name': 'owd', 'inventory': {'apple': 1, 'orange': 10}}, {
        'name': 'dm', 'inventory': {'banana': 5, 'orange': 5}}]
    ia = InventoryAllocator(order, inventory)

    print(ia.allocation())
