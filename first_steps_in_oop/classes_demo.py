class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size


android = Phone("blue", 4.7)
print(android.size)

ios = Phone("black", 5.7)
print(ios.color)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


toni = Person("Toni", 19)

print(toni.name, toni.age)


class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

