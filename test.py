__author__ = 'far'

print("Hallo Welt")

print("xxx")


def method_name():
    global str, i
    str = "Hallo meine geliebte Welt"
    i = 0
    while i < len(str):
        print(str[i])

        i = i + 1
    print("Ende")
    print("mercury test")


print("Mercury Test2")
print("Mercury Test2")
method_name()