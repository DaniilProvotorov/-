my_dict = {"Dan" : 21, "Nik" : 55, "Frost" : 34}
print(my_dict)
print(my_dict["Dan"])
print(my_dict.get('Loyd', 'такого значения нет '))
my_dict.update({"Frank" : 43, "Mik" : 78})
print(my_dict)
a = my_dict.pop("Mik")
print(a)
print(my_dict)


my_set = {5, 11, 'Damn', "so hot", (1, 6, 3), 6, 5, 18, 11}
print(my_set)
my_set.add(16)
my_set.add("pepsa")
print(my_set)
my_set.discard(11)
print(my_set)