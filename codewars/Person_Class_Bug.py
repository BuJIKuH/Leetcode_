class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    def __str__(self):
        return f'{self.full_name}' + '\n' + f'{self.age}'


Person('Yukihiro', 'Matsumoto', 47)