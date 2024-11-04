# TODO Напишите функцию find_common_participants

def f_c_p(gr1, gr2):
    list_of_gr1 = set(gr1.split("|"))
    list_of_gr2 = set(gr2.split("|"))
    c_p = list_of_gr1.intersection(list_of_gr2)
    return c_p


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(" ", f_c_p(participants_first_group, participants_second_group))