class PhoneBook:

    def __init__(self):
        self._numbers = {}


    def add(self, name, number):
        self._numbers[name] = number


    def lookup(self, name):
        # return self._numbers.get(name, None)
        return self._numbers[name]


    def is_consistent(self):
        numbers = self._numbers.values()
        if len(numbers) == 0: 
            return True
        for number in numbers:
            if sum(1 if num.startswith(number) else 0 for num in self._numbers.values()) > 1:
                return False
        return True


    def get_names(self):
        return set(self._numbers.keys())


    def get_numbers(self):
        return set(self._numbers.values())