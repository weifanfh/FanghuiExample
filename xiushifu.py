def a(fun):
    print("修饰符函数入")
    def wrapper(*args, **kwargs):
        value2=2
        result = fun(*args, **kwargs)
        return result
    print(wrapper("修饰符参数"))
    print('修饰符函数中')
    value3=3
    return wrapper

# @a
# def b(name):
#     print(name)

@a
def b(a):
    value1=1
    print(a)
    return a

print('外层函数调用前')
c=b("外层函数参数")
print('外层函数调用后')
print(c)

