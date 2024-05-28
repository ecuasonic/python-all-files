dict = {}

def Food(tup):
    name = tup[0]
    price = tup[1]
    cal = tup[2]
    ratio = cal/price
    dict[name] = f'{ratio:.0f} cal per dol'

lst = [('10 Pc Nug', 6.29, 410),
       ('6 Pc Nug',4.29,250),
       ('20 Pc Nug',11.29,830),
       ('4 Pc Nug',3.69,170),
       ('Med Fries', 3.99, 320),
       ('Cheese Pack', 21.99, 2070),
       ('Big Mac Pack', 27.99, 2650),
       ('6 pc Nug Hap', 7.80, 530),
       ('Ham Hap', 6.09, 510),
       ('4 pc Nug Hap', 6.29, 430),
       ('Big Mac Meal', 11.29, 1150),
       ('Two Cheese', 9.99, 1160),
       ('Double CB', 3.89, 450),
       ('McDoub', 3.09, 400),
       ('Double QB w C', 12.39, 1300),
       ('Comb', 20.39, 4280)]

for i in lst:
    Food(i)
for key in dict:
    print(f'{key} || {dict[key]}')
