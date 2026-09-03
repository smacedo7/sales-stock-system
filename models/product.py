class Product:
    _next_id = 1

    def __init__(
            self,
            name: str,
            price: float,
            description: str,
            id: int | None = None,
    ) -> None:

        self.name = name
        self.price = price
        self.description = description

        if id is None:
            self._id = type(self)._next_id
            type(self)._next_id += 1
        else:
            self._validate_id(id)
            self._id = id
            type(self)._next_id = max(type(self)._next_id, id + 1)

    def _validate_id(
            self,
            id: int
    ) -> None:
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError('Id must be an integer.')
        if id <= 0:
            raise ValueError('Id must be greater than zero.')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name.strip()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Insert a valid number!')
        if value < 0:
            raise ValueError("Price must be greater than zero.")
        self._price = value

    @property
    def id(self) -> int:
        return self._id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not description or not description.strip():
            raise ValueError("Description cannot be empty.")
        self._description = description.strip()

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object]
    ) -> Product:

        required_keys = (
            "id",
            "name",
            "price",
            "description",
        )

        for key in required_keys:
            if key not in data:
                raise KeyError(f"Missing field: {key}")

        name = data["name"]
        price = data["price"]
        description = data["description"]
        product_id = data["id"]

        return cls(
            name=name,
            price=price,
            description=description,
            id=product_id,
        )

    def __str__(self):
        return f'''
Product: {self._name},
         {self._description}
         {self._id}
         {self._price:.2f}
'''
