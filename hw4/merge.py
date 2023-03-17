def merge(list1, list2):
          listFinal = []
          list2Count = 0
          for i in list1:
                    while(list2Count < len(list2)):
                              if list2[list2Count] < i:
                                        listFinal.append(list2[list2Count])
                                        list2Count += 1
                              else:
                                        break
                    listFinal.append(i)
                    
          while(list2Count < len(list2)):
                    listFinal.append(list2[list2Count])
                    list2Count += 1
          print(listFinal)
          return listFinal

list1= [1, 3, 5, 7]
list2= [2, 4, 6]
merge(list1, list2)
                             
list1 =  [1, 2, 3, 5]
list2 = [1, 2, 4, 5, 6]
merge(list1, list2)

list1 =  [1, 5, 9]
list2 = []
merge(list1, list2)