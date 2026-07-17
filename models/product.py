class Product:
    _next_id = 1

    def __init__(self, name, description, price):
        self.name = name
        self.price = price
        self.description = description

        self._id = type(self)._next_id
        type(self)._next_id += 1

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")   
        self._name = name.strip()


    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, value):
        if value < 0:
             raise ValueError("Price must be greater than zero.")
        if not isinstance(value, (int, float)):
            raise TypeError('Insert a valid number! ')
        self._price = value


    @property
    def id(self):
        return self._id
        
    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, description):
        if not description or not description.strip():
            raise ValueError("Description cannot be empty.")   
        self._description = description.strip()

    def __str__(self):
        return f'''
Product: {self._name},
         {self._description}
         {self._id}
         {self._price:.2f}
'''