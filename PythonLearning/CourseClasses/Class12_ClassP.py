class Builder():
    def __init__(self,size,area,inventory,builder):
        self.flatsize=size
        self.area=area
        self.inventory=inventory
        self.builder=builder

    def customer(self,custname):
        print('Welcome ',custname,' for purchasing flat at ',self.area,' of size ',self.flatsize,'from builder : ',self.builder)
        self.inventory-=1
        print('Inventory left is : ',self.inventory)

B1=Builder('2000sqft','Gurugram',200,'DLF')
B2=Builder('1700sqft','Noida',200,'Gaur')

B1.customer('Tanya')
B1.customer('irwin')

B2.customer('Rohit')
B2.customer('Neha')


