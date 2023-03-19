def cacti_number(arr2d):
        ROWS = len(arr2d)
        COLLS = len(arr2d[0])
        moreCactiCount = 0
        for row in range(len(arr2d)):
                print(arr2d[row])
                for element in range(len(arr2d[row])):
                        print(arr2d[row][element])
                        if (row == 0): #first row
                                        if (element == 0 and arr2d[row][element] == 0): #leftmost element = 0
                                                if (arr2d[row + 1][element] == 0 and arr2d[row][element + 1] == 0): #check surrounding cases (below, right)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                        if (element > 0 and element < COLLS - 1 and arr2d[row][element] == 0): #middle element = 0
                                                if (arr2d[row + 1][element] == 0 and arr2d[row][element + 1] == 0 and arr2d[row][element - 1] == 0): #check surrounding cases (below, right, left)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                        if (element == COLLS - 1 and arr2d[row][element] == 0): #rightmost element = 0
                                                if (arr2d[row + 1][element] == 0 and arr2d[row][element - 1] == 0): #check surrounding cases (below, left)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                                        
                        if (row > 0 and row < ROWS - 1): #middle rows 
                                        if (element == 0 and arr2d[row][element] == 0): #leftmost element = 0
                                                if (arr2d[row + 1][element] == 0 and arr2d[row][element + 1] == 0 and arr2d[row - 1][element] == 0): #check surrounding cases (below, right, top)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                        if (element > 0 and element < COLLS - 1 and arr2d[row][element] == 0): #middle element = 0
                                                if (arr2d[row + 1][element] == 0 and arr2d[row][element + 1] == 0 and arr2d[row][element - 1] == 0 and arr2d[row - 1][element] == 0): #check surrounding cases (below, right, left, top)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                        if (element == COLLS - 1 and arr2d[row][element] == 0): #rightmost element = 0
                                                if (arr2d[row + 1][element] == 0 and arr2d[row][element - 1] == 0 and arr2d[row - 1][element] == 0): #check surrounding cases (below, left, top)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                        if (row == ROWS - 1): #last row
                                        if (element == 0 and arr2d[row][element] == 0): #leftmost element = 0
                                                if (arr2d[row - 1][element] == 0 and arr2d[row][element + 1] == 0): #check surrounding cases (top, right)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                        if (element > 0 and element < COLLS - 1 and arr2d[row][element] == 0): #middle element = 0
                                                if (arr2d[row - 1][element] == 0 and arr2d[row][element + 1] == 0 and arr2d[row][element - 1] == 0): #check surrounding cases (top, right, left)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1
                                        if (element == COLLS - 1 and arr2d[row][element] == 0): #rightmost element = 0
                                                if (arr2d[row - 1][element] == 0 and arr2d[row][element - 1] == 0): #check surrounding cases (top, left)
                                                        arr2d[row][element] = 1
                                                        moreCactiCount += 1                                                              
                                                                      
def main():
        plot = [ [1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0] ]
        print(cacti_number(plot))
        # print(plot)
        # print(plot[0])          

main()