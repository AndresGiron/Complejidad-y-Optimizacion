import subprocess

def minizinc(values):
    cat = int(values['cantidad'])
    maxp = values['PagsArticulo']
    pagMin = []
    pagMax = []
    rdrs = []
    for i in range(0,cat):
        pagMin.append(int(values['min'+str(i)]))
    for i in range(0,cat):
        pagMax.append(int(values['max'+str(i)]))
    for i in range(0,cat):
        rdrs.append(int(values['readers'+str(i)]))

    dzn = 'cat = %s; \nmaxp = %s; \npagMin = %s; \npagMax = %s; \nrdrs = %s; \n'%(str(cat),maxp,str(pagMin),str(pagMax),str(rdrs))
    
    with open("Mzn&Dzn/datos.dzn","w") as file:
        file.write(dzn)


"""instancia = {'cantidad': '2', 
'tipo0': 'ewq', 'min0': '1', 'max0': '3', 'readers0': '1', 
'tipo1': 'ewq', 'min1': '2', 'max1': '3', 'readers1': '2',
'PagsArticulo': '12'}

print(minizinc(instancia))"""
