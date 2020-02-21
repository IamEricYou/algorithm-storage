class  InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory

    def tempcase(self):
        print(self)

    

if __name__ == '__main__':
    print("Check")
    # d = dict()
    # var = input("input? ")
    # key, value = var.split()
    # d[key] = int(value)

    ia = InventoryAllocator("hi","hello")
    print(ia.tempcase())