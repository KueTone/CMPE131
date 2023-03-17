def double(func):
          def wrapper_func():
                    func()
                    print("Let’s try that again!")
                    func()
          return wrapper_func
@double 
def greet():
          print('Hello World!')
def main():
          greet()
main()