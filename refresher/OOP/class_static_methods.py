# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
#
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#
#     @staticmethod
#     def static_method():
#         print("Called static_method.")
#
#
# ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"



book = Book("Harry Potter", "hardcover", 1500)

print(book)