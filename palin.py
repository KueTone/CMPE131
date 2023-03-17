def palindrome(lst): 
          palin = True
          length = len(lst)
          for i in range(int(len(lst)/2)):
                    if (lst[i] != lst[length-i-1]):
                              palin = False


