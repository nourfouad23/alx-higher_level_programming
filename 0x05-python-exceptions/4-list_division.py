#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    resultList = []
    listIndex = 0
    if list_length <= 0:
        print("out of range")
        return resultList
    while listIndex < list_length:
        try:
            resultList.append(my_list_1[listIndex] / my_list_2[listIndex])
        except ZeroDivisionError:
            print("division by 0")
            resultList.append(0)
        except TypeError:
            print("wrong type")
            resultList.append(0)
        except IndexError:
            print("out of range")
            resultList.append(0)
        finally:
            listIndex += 1
    return resultList
