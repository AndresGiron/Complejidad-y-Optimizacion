import minizinc
from minizinc import Driver, Instance, Solver, default_driver
import pymzn

def minizinzFunction(values):
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

    #Creando el diccionario con los parametros 
    dict = {}
    dict['cat'] = cat
    dict['maxp'] = maxp
    dict['pagMin'] = pagMin
    dict['pagMax'] = pagMax
    dict['rdrs'] = rdrs

    #Convirtiendolo a dzn
    pymzn.dict2dzn(dict, fout="../datos.dzn")

    #Ubicacion del modelo y ubicacion de parametros
    folder = minizinc.Model("../ModeloProyecto.mzn")
    folder.add_file("../datos.dzn")
    
    v26: Driver = Driver.find(["../MiniZincIDE 2.6.4/bin"])
    chuffed = Solver.lookup("chuffed", driver=v26)
    v26.make_default()

    chuffed = minizinc.Solver.lookup("chuffed")
    instance = minizinc.Instance(chuffed, folder)

    result = instance.solve()
    print(result['typeNews'],result['utility'])

    return (result['typeNews'],result['utility'])

values = {'cantidad': '5', 'tipo0': '1', 'min0': '5', 'max0': '9', 'readers0': '1500', 'tipo1': '23', 'min1': '4', 'max1': '7', 'readers1': '2000', 'tipo2': '3', 'min2': '2', 'max2': '5', 'readers2': '1000', 'tipo3': '4', 'min3': '2', 'max3': '4', 'readers3': '1500', 'tipo4': '5', 'min4': '1', 'max4': '3', 'readers4': '750', 'PagsArticulo': '10'}
minizinzFunction(values)