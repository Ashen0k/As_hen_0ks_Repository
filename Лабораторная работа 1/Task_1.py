numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

nums2 = list(numbers)
nums2.remove(None)
# print(numbers)
# print(nums2)

summary = sum(nums2)
length = len(numbers)
to_replace = summary / length
#print(to_replace)

for i in range(len(numbers)):
    if numbers[i] == None :
        numbers[i] = to_replace

    # TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:",numbers)
