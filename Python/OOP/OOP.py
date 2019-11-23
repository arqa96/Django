class Meta(type):
    invalid_methods = ('__set__', '__get__', '__delete__')

    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 1:
            raise TypeError('Not Valid!')
        if any(key in cls.invalid_methods for key, value in clsdict.items()):
            raise AttributeError
        return super().__new__(cls, clsname, bases, clsdict)


class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Employee(metaclass=Meta):
    def __init__(self, name, lname, salary):
        self.name = name
        self.lname = lname
        self.salary = salary

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lname)

    @classmethod
    def string_to_split(cls, string):
        name, lname, salary = string.split('-')
        return cls(name, lname, salary)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.lname, self.salary)


class Developer(Employee):
    def __init__(self, name, lname, salary, language):
        super().__init__(name, lname, salary)
        self.language = language

    name = Descriptor('name')
    lname = Descriptor('lname')
    salary = Descriptor('salary')
    language = Descriptor('language')


if __name__ == '__main__':
	emp = 'Ivan-Ivanov-40000'

	new_emp = Employee.string_to_split(emp)
	print(new_emp.name)
	print(new_emp.fullname)
	print(new_emp)

	first_dev = Developer('Sergey', 'Sergeev', '50000', 'python')
	print(first_dev.name)

