def delete(list_, index=None):
    if index is not None:
        a = list_[:index]
        b = list_[index + 1:]
        list_ = a + b
        return list_
    else:
        index = -1
        list_ = list_[:index]
        return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
