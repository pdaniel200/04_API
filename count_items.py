"""
creare lista si numaram de cate ori se gaseste fiecare element in ea
"""


def counter(fruits):
    my_dict = {}
    for item in fruits:
        item = item.lower()
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    return my_dict

# todo minim 5 noi teste care prima oara sa dea fail iar pe urma sa dea pass modificand functia de mai sus
# todo sa cautam pachetul coverage si sa vedem ce putem sa il folosim (sa vedem cat la suta e testata)
