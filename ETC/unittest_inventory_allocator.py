import unittest
from inventory_allocator import InventoryAllocator as ia

class Unit_test(unittest.TestCase):
    def test_with_empty_order(self):
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10 } }]
        test_output = []
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)

    def test_with_good_case_with_one_warehouse(self):
        order = {'apple' : 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10 } }]
        test_output = [{'owd': {'apple': 10}}]
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)

    def test_with_not_enough_inventory_with_one_warehouse(self):
        order = {'apple' : 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5 } }]
        test_output = []
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)

    def test_with_good_case_with_many_warehouses(self):
        order = {'apple' : 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5 } }, {'name': 'dm', 'inventory': {'apple': 5 } }]
        test_output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)

    def test_with_not_enough_inventory_with_many_warehouses(self):
        order = {'apple' : 10, 'banana': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 7} }]
        test_output = []
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)

    def test_warehouse_not_have_item(self):
        order = {'apple' : 10, 'melon': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 10} }]
        test_output = []
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)
    
    def test_with_many_order_with_many_warehouses(self):
        order = {'apple' : 10, 'melon': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 10, 'melon': 5} }, {'name': 'dm', 'inventory': {'apple': 5, 'melon': 5, 'orange': 10} }]
        test_output = [{'owd': {'apple': 10, 'melon': 5}}, {'dm': {'melon': 5}}]
        inventory_allocator = ia(order, inventory)
        print(inventory_allocator.run_allocation())
        self.assertEqual(inventory_allocator.run_allocation(), test_output)


if __name__ == '__main__':
    unittest.main()