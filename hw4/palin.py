def palindrone(lst): 
#     lst = [1,2,3,4]
          palin = True
          length = len(lst)
          for i in range(int(len(lst)/2)):
                    print(i, " & ", length-i-1)
                    if (lst[i] != lst[length-i-1]):
                              palin = False
                    # print(lst[i])
          
                    
          
#     for i in (range(len(lst)))/2:
#         if (lst[i] != lst[length-i]):
#             palin = False
 
          return palin
    
list1 = [1, 2, "Espresso", "Madeline", 2, 1]
list2 = ['a', True, False, False, True, 'a']
list3 = [3]

print(palindrone(list1))
print(palindrone(list2))
print(palindrone(list3))

