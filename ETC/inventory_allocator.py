from collections import Counter


class InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        self.return_dict = {}

    # Main function to run
    def run_allocation(self):
        total_inventory = self.merge_inventories()
        if not self.check_inventory_have_item(total_inventory):
            return []

        self.process_order(total_inventory)

        return_list = []
        for x in self.return_dict:
            return_list.append({x: self.return_dict[x]})

        return return_list

    # Merge dictionaries (map) into one
    def merge_inventories(self):
        temp_inventory = {}
        swap = {}
        for x in self.inventory:
            temp_inventory = Counter(temp_inventory) + Counter(x['inventory'])

        for item in temp_inventory:
            if item in self.order:
                swap[item] = temp_inventory[item]

        return dict(swap)

    # Parse dictionaries to be processed
    def process_order(self, inv):
        for item in inv:
            for x in self.inventory:
                if item in x['inventory']:
                    self.calculate_order(item, x)

    # Calculate the order

    def calculate_order(self, item, each_warehouse):
        if(self.order.get(item) == 0):
            return

        temp_value = each_warehouse['inventory'].get(
            item) - self.order.get(item)
        swap_value = self.order.get(item)

        # If Inventory doesn't have enough stock
        if(temp_value <= 0):
            self.order[item] = self.order.get(
                item) - each_warehouse['inventory'].get(item)
            if each_warehouse['name'] in self.return_dict:
                if item in self.return_dict[each_warehouse['name']]:
                    self.return_dict[each_warehouse['name']] = {item: (
                        self.return_dict[each_warehouse['inventory']].get(item) + each_warehouse['inventory'].get(item))}
                else:
                    self.return_dict[each_warehouse['name']
                                     ][item] = each_warehouse['inventory'].get(item)
            else:
                self.return_dict[each_warehouse['name']] = {
                    item: each_warehouse['inventory'].get(item)}
        # If Inventory has enough stock
        else:
            self.order[item] = 0
            if each_warehouse['name'] in self.return_dict:
                if item in self.return_dict[each_warehouse['name']]:
                    self.return_dict[each_warehouse['name']] = {
                        item: self.return_dict[each_warehouse['inventory']].get(item) + temp_value}
                else:
                    self.return_dict[each_warehouse['name']][item] = swap_value
            else:
                self.return_dict[each_warehouse['name']] = {item: swap_value}

    # Check the order is valid to be made

    def check_inventory_have_item(self, inv):
        for order_item in self.order:
            if order_item not in inv:
                #print("Inventory doesn't have the item in the order")
                return False

            if self.order[order_item] > inv[order_item]:
                #print("Inventory doesn't have enough item to order.")
                return False
        return True


if __name__ == '__main__':
    order = {'banana': 5, 'orange': 10}
    inventory = [{'name': 'owd', 'inventory': {'banana': 1, 'orange': 10}}, {
        'name': 'dm', 'inventory': {'banana': 5, 'orange': 5}}]
    ia = InventoryAllocator(order, inventory)

    # Print this line to test
    ia.run_allocation()
