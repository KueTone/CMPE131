"""
set minimum to first element
compare all elements to minItem
once minItem found, place item into dictionary with age as key
repeat
"""
def sort_dictionary(dict):
          dict2 = []
          while (len(dict) != 0):
                    minItem = list(dict.items())[0]
                    for i in dict.items():
                              if i[1][1] < minItem[1][1]:
                                        minItem = i
                    dict2.append(tuple([minItem[0], minItem[1][0]]))
                    dict.pop(minItem[0])
                              
          return dict2