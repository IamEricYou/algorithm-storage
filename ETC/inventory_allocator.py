class  InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        order_list = []

    def allocation(self):
        # if not order or not self.inventory:
        #     return []
        print(order,inventory)
        # for item in inventory:
        #     self.parse_inventory(item)
        for key in order.keys():
            #self.calculate_inventory(key)
            if(self.check_inventory_have_item(key)):
                return []

    def parse_inventory(self, item):
        for x in item['inventory']:
            self.calculate_inventory(x)

    def calculate_inventory(self, product):
        for x in order[product]:
            print(x)
    
    def check_inventory_have_item(self, item):
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

   