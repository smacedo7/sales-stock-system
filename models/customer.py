import re

class Customer:
    _next_id = 1

    _EMAIL_REGEX = re.compile(r'''(
                            [a-zA-Z0-9._-]+
                            @
                            [a-zA-Z0-9._-]+
                            (\.[a-zA-Z]{2,4})
                            )''', re.VERBOSE)

    def __init__(
            self,
            name: str,
            cpf: str,
            address: str,
            email: str,
            balance: int | float = 0,
    ) -> None:
        
        self._validate_balance(balance)

        self.name = name
        self.address = address
        self.cpf = cpf
        self.email = email
        self._balance = balance

        self._id = type(self)._next_id
        type(self)._next_id += 1

    def _validate_not_empty(
            self,
            value: str,
            field_name: str
    ) -> None:
        if not isinstance(value, str):
            raise TypeError(f'{field_name} must be a string.')
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty.") 

    def _validate_email(
            self,
            email: str
    ) -> None:

        if not self._EMAIL_REGEX.fullmatch(email):
            raise ValueError('Email address is invalid.')

    def _validate_cpf(
            self,
            cpf: str
    ) -> None:
        if not isinstance(cpf, str):
            raise TypeError('CPF must be a string.')
        if len(cpf.strip()) != 11 or not cpf.isdigit():
            raise ValueError('CPF is invalid.')

    def _validate_balance(
            self,
            balance: float
    ) -> None:
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise TypeError('Balance must be an integer or float.')

        if balance < 0:
            raise ValueError('Balance must be greater than or equal to zero.')

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._validate_not_empty(name, 'Name')  
        self._name = name.strip()

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._validate_not_empty(address, 'Address')
        self._address = address.strip()

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._validate_not_empty(email, 'Email')
        self._validate_email(email)
        self._email = email.strip()

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._validate_not_empty(cpf, 'CPF')
        self._validate_cpf(cpf)
        self._cpf = cpf.strip()
    
    @property
    def balance(self):
        return self._balance

    def deposit(
            self,
            value: int | float
    ) -> None:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError('Deposit must be an integer or float.')

        if value <= 0:
            raise ValueError('Deposit must be greater than zero.')

        self._balance += value

    def charge(
            self,
            value: int | float
    ) -> None:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError('Charge must be an integer or float.')

        if value <= 0:
            raise ValueError('Charge must be greater than zero.')

        if value > self._balance:
            raise ValueError('Insufficient balance.')

        self._balance -= value