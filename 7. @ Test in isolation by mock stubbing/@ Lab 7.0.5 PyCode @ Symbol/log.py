def log(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper

@log
def f():
    print('hello')
    
f();
