
def minizinc(values):
    cat = int(values['cantidad'])
    maxp = values['PagsArticulo']
    pagMin = []
    pagMax = []
    rdrs = []
    for i in range(0,cat):
        pagMin.append(values['min'+str(i)])
    for i in range(0,cat):
        print(i)
        pagMax.append(values['max'+str(i)])
    for i in range(0,cat):
        rdrs.append(values['readers'+str(i)])

    dzn = 'cat = %s; \nmaxp = %s; \npagMin = %s; \npagMax = %s; \nrdrs = %s; \n'%(str(cat),maxp,str(pagMin),str(pagMax),str(rdrs))
    return(dzn)


instancia = {'cantidad': '2', 
'tipo0': 'ewq', 'min0': '1', 'max0': '3', 'readers0': '1', 
'tipo1': 'ewq', 'min1': '2', 'max1': '3', 'readers1': '2',
'PagsArticulo': '12'}

print(minizinc(instancia))