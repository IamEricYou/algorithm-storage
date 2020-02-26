from collections import Counter

class InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        self.return_dict = {}

    def run_allocation(self):
        print(order, inventory)
        total_inventory = self.merge_inventories()
        if self.check_inventory_have_item(total_inventory):
            self.is_order_valid = False;
            print("Here")
            return []
            
        #print(total_inventory)
        output_inventory = self.process_order(total_inventory)
        print(self.return_dict)

    def merge_inventories(self):
        temp_inventory = {}
        swap = {}
        for x in self.inventory:
            temp_inventory = Counter(temp_inventory) + Counter(x['inventory'])

        for item in temp_inventory:
            if item in self.order:
                swap[item] = temp_inventory[item]

        return dict(swap)

    def process_order(self, inv):
        temp_inventory = {}
        for item in inv:
            for x in self.inventory:
                if item in x['inventory']:
                    swap_inv = self.calculate_order(item, x)
                    if swap_inv is not None:
                        temp_inventory = {**temp_inventory, **swap_inv}

        return temp_inventory

    def calculate_order(self, item, each_warehouse):
        #{x.get('name'): {item: (self.order.get(item) - x['inventory'].get(item))} }
        if(self.order.get(item) == 0):
            return
            
        temp_value = each_warehouse['inventory'].get(item) - self.order.get(item) #4
        swap_value = self.order.get(item)
        print("Return",self.return_dict)
        if(temp_value <= 0):
            self.order[item] = self.order.get(item) - each_warehouse['inventory'].get(item)
            if each_warehouse['name'] in self.return_dict:
                if item in self.return_dict[each_warehouse['name']]:
                    self.return_dict[each_warehouse['name']] = {item : (self.return_dict[each_warehouse['inventory']].get(item) + each_warehouse['inventory'].get(item))}
                else:
                    self.return_dict[each_warehouse['name']] = {item : each_warehouse['inventory'].get(item) }
            else:
                self.return_dict[each_warehouse['name']] = {item : each_warehouse['inventory'].get(item) }
        else:
            self.order[item] = 0
            if each_warehouse['name'] in self.return_dict:
                if item in self.return_dict[each_warehouse['name']]:
                    self.return_dict[each_warehouse['name']] = {item : self.return_dict[each_warehouse['inventory']].get(item) + temp_value}
                else:
                    self.return_dict[each_warehouse['name']] = {item : swap_value}
            else:
                self.return_dict[each_warehouse['name']] = {item : swap_value}
       

    #Call
    def check_inventory_have_item(self, inv):
        for order_item in self.order:
            if order_item not in inv:
                print("Inventory doesn't have the item in the order")
                return False
            
            if self.order[order_item] > inv[order_item]:
                print("Inventory doesn't have enough item to order.")
                return False

if __name__ == '__main__':
    order = {'banana': 5, 'orange': 10}
    inventory = [{'name': 'owd', 'inventory': {'banana': 1, 'orange': 10}}, {
        'name': 'dm', 'inventory': {'banana': 5, 'orange': 5}}]
    ia = InventoryAllocator(order, inventory)
    
    ia.run_allocation()
