def double(func):
          def wrapper_func():
                    func()
                    print("Let's try that again!")
                    func()
          return wrapper_func
