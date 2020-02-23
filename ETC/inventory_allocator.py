class InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        order_list = []

    def allocation(self):
        total_inventory = {}
        # if not order or not self.inventory:
        #     return []
        print(order, inventory)
        # for item in inventory:
        #     self.parse_inventory(item)
        for x in inventory:
            self.parse_inventory(x)
            
            
            # self.calculate_inventory(key)
            # if(not(self.check_inventory_have_item(key))):
            #     return []

    def parse_inventory(self, item):
        print(item)

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
