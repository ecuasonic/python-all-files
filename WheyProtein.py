#amn_lst = [al, arg, as_ac, cy, glu_ac, gly, hist, iso, leu, lys, meth, phen, pro, ser, ther, tryp, tyr, val]
#nut_lst = [serv, cal, cho, pro]

amn_d = dict(al=0, arg=0, as_ac=0, cy=0, glu_ac=0, gly=0, hist=0 , iso=0, leu=0, lys=0, meth=0, phen=0, pro=0, ser=0, ther=0, tryp=0, tyr=0, val=0)
nut_d = dict(serv=0, cal=0, cho=0, pro=0)

class protein:
    global amn_d
    global nut_d
    def __init__(self, name, amn_t, nut_t):

        self.name = name

        amn_dc = dict(amn_d)
        count = 0
        for k in amn_dc:
            amn_dc[k] = amn_t[count]
            count += 1
        self.amn_d = amn_dc

        nut_dc = dict(nut_d)
        count = 0
        for k in nut_dc:
            nut_dc[k] = nut_t[count]
            count += 1
        self.nut_d = nut_dc

w = 81.647 #body weight (kg)       
base = dict(hist = 10, lys = 12, phen = 14, meth = 12, leu = 16, iso = 12, val = 16, ther = 8, glu_ac = 10, cy = 300) #mg amino acid / kg body weight
for k in base: #scaling
    base[k] = int(base[k]*w) 

p1 = protein('Levels Grass Fed Whey Protein', 
             (1160, 690, 2540, 490, 4010, 470, 460, 1430, 2490, 2090, 490, 800, 1340, 1190, 1640, 430, 710, 1440), 
             (71, 130, 95, 24))

p2 = protein('Nutricost Isolate',
             (4235, 2347, 8903, 1782, 15075, 1554, 1509, 4860, 9158, 8037, 1942, 2657, 4909, 4303, 5890, 1417, 2466, 4951),
             (60,130, 15, 30))

p3 = protein('Nutricost Concentrate',
             (3762, 2086, 7909, 1584, 13392, 1381, 1340, 4317, 8136, 7140, 1725, 2361, 4362, 3823, 5232, 1260, 2191, 4398),
             (63, 140, 75, 25))

for k in amn_d: #rescaling
    p2.amn_d[k] = int(p2.amn_d[k]*(38/100))
    p3.amn_d[k] = int(p3.amn_d[k]*(36/100))

for k in base: #comparision
    print(f'{k} || base: {base[k]}  ||  p1: {p1.amn_d[k]}  |  p2: {p2.amn_d[k]}  |  p3: {p3.amn_d[k]}')
print('')
print(f'Total Protein || p1: {71*24}  |  p2: {60*30}  |  p3: {63*25}')
print(f'grams per $ || p1: {71*24/80}  |  p2: {60*30/70}  |  p3: {63*25/57}')