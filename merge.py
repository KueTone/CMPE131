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
          return listFinal