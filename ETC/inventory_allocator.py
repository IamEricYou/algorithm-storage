class  InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory

    def allocation(self):
        # if not order or not self.inventory:
        #     return []
        print(order,type(inventory))
        for key in inventory[1].keys():
            print(inventory[1].get(key))
        # for key in order.keys():
        #     self.calculate_inventory(key)

    def calculate_inventory(self, key):
        for item in inventory.keys():
            print(item)



if __name__ == '__main__':
    print("Check")
    # d = dict()
    # var = input("input? ")
    # key, value = var.split()
    # d[key] = int(value)

    order = {'melon': 1, 'banana': 2, 'orange': 9}
    inventory = [{'name': 'owd', 'inventory': {'apple': 1, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 5} }]
    ia = InventoryAllocator(order,inventory)

    ia.allocation()

   