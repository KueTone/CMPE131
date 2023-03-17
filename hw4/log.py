import time

def timestamp(func):
          def wrapper_func():
                    print(time.ctime())
                    func()
          return wrapper_func
                    
@timestamp
def hi():
          print('hi')
def main():
          hi()
main()