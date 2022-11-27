import PySimpleGUI as sg
from Minizinc import minizinzFunction

cantidad = 0

layout = [
    [sg.Text("Cantidad de noticias"),sg.InputText(key="cantidad"),sg.Button("Agregar")]
    ]
window = sg.Window("Periodico", layout)


while True: 
    event, values = window.read()
    print(event,values)

    if event in (sg.WINDOW_CLOSED,"Exit"):
        break
    if event == "Agregar":
        #cantidad = int (values['cantidad'])
        for i in range(0,int(values['cantidad'])):
            print(i)
            
            window.extend_layout(window,[[sg.Text("Noticia"),sg.InputText(key="tipo"+str(i),size=(20,10)),
            sg.Text("Paginas minimas"),sg.InputText(key="min"+str(i),size=(5,10)),
            sg.Text("Paginas maximas"),sg.InputText(key="max"+str(i),size=(5,10)),
            sg.Text("Lectores potenciales"),sg.InputText(key="readers"+str(i),size=(10,10))]])

        window.extend_layout(window,[[sg.Text("Cantidad Maxima de paginas de la publicacion"),sg.InputText(key="PagsArticulo",size=(20,10))]])
        window.extend_layout(window,[[sg.Button("Optimizar")]])
        window["Agregar"].update(disabled=True)
        window.refresh()
    if event == "Optimizar":
        result = minizinzFunction(values)
        texto = []
        for i in range(0,len(result[0])):
            texto.append(sg.Text(values['tipo'+str(i)] + ' = ' +str(result[0][i])))
        window.extend_layout(window,[[sg.Text("Paginas por tipo de noticia")]])
        window.extend_layout(window, [texto])
        window.extend_layout(window,[[sg.Text("Lectores potenciales totales")]])
        window.extend_layout(window,[[sg.Text(str(result[1]))]])


window.close()