from collections import namedtuple

Person = namedtuple("Person", "name surname age gender")
jake=Person(name='Jake', surname='Smith', age=19, gender='male')
jim=Person(name='Jim', surname='Blade', age=23, gender='male' )
jane=Person(name='Jane', surname='Morrison', age=20, gender='female' )


print(jake.name)
print(jake.surname)
print(jane)
jane=jane._replace(surname='Blade')
print(jane)