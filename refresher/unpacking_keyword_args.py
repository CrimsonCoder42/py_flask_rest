# def named(**kwargs):
#     print(kwargs)
#
#
# named(name="Bob", age=25)

def named(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}

named(**details)