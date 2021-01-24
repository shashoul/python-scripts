class ShippingContainer:

    next_serial = 1337       # << class Attribute

    # @staticmethod
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result


    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result


    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, [])


    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        #self._serial = ShippingContainer.next_serial
        #ShippingContainer.next_serial += 1
        #self._serial = self._generate_serial()
        self._serial = ShippingContainer._generate_serial()


    @property
    def serial(self):
        return self._serial


    @serial.setter
    def serial(self, serial):
        self._serial = serial
