#Exercise2
import numpy as np
#task1
#[Фамилия, ГодПоступления, НаправлениеПодготовки]
list = [
    ["Ivanov", 2025, "Прикладная информатика"],
    ["Petrov", 2024, "Компьютерная лингвистика"],
    ["Sidorov", 2023, "Прикладная информатика"]
]

list_appl_inf = [item[0] for item in list if item[-1] == "Прикладная информатика"]
print(list_appl_inf)

list.append(["Kuznetsov", 2021, "Прикладная информатика"])

print(list)

# task2
temperature = {
    "day1": [23, 24, 25],
    "day2": [20, 20, 20],
    "day3": [23, 22, 21],
    "day4": [18, 24, 25],
    "day5": [19, 21, 30],
 }
list_sum_of_samples = [sum(x) for x in temperature.values()]
print(temperature.values())
print(sum(list_sum_of_samples))

list_number_of_samples = [len(x) for x in temperature.values()]
print(list_number_of_samples)
print(sum(list_number_of_samples))

average = sum(list_sum_of_samples) / sum(list_number_of_samples)
print(average)

in_list = list(temperature.values())
print("in_list: ", in_list)
ndarray = np.array(list(temperature.values()))
print("ndarray: ", ndarray)
# print("type_ndarray: ", type(ndarray))
# diff_from_average = ndarray - 20
# print("diff_from_average: ", diff_from_average)

