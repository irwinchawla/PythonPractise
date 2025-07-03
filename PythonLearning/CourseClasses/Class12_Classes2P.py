class Builder():
    def __init__(self):
        self.flatsize='2800sqft'
        self.area='Camelia'
        self.inventory=100

    def customer(self,custname):
        print('Welcome ',custname,' for purchasing flat at ',self.area,' of size ',self.flatsize)
        self.inventory-=1
        print('Inventory left is : ',self.inventory)



cus=Builder()

cus.customer('Tanya')


