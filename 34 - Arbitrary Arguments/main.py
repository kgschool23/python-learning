# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))

def display_name(*args):
    # print(type(args)) # args is a tuple
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

def print_address(**kwargs):
    print(type(kwargs)) # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              city="Detroit",
              state="Michigan",
              zip="54321")

def shipping_label(*args, **kwargs): # kwargs must follow args
    for arg in args:
        print(arg, end=" ")
    print()

    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               city="Detroit",
               state="MI",
               zip="54321")