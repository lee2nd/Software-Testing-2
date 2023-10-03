def extend_behavior(func):
    print('extended')
    return func

@extend_behavior
def some_func():
    print('hello')

print('hello world');