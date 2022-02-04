import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
ventana.title("Liquidos")
tab = ttk.Notebook(ventana)
tab1 = ttk.Frame(tab)
tab.add(tab1, text="Nota")
tab.pack(expand=1, fill="both")
tab2 = ttk.Frame(tab)
tab.add(tab2, text="Calculadora")
tab.pack(expand=1, fill="both")
tab3 = ttk.Frame(tab)
tab.add(tab3, text="Indicaciones")
tab.pack(expand=1, fill="both")

#FUNCIONES

def liquidos():
    a=peso.get()
    l=mililitros.get()
    h=hrs.get()
    #convierte las hrs a veces al dia.
    if h == str(6):
        h=4
    if h == str(8):
        h=3
    if h == str(12):
        h=2

    if a <= 10:
        superficie = (((a * 4) + 9) / 100)
        superficie = round(superficie, 2)
        resultado2 = (superficie * l) / float(h)
        resultado2 = round(resultado2, 2)
        print (h)
        resultado_scp.configure(text=" superficie corporal:" +str(superficie))
        resultado_liquidos.configure(text=" Mililitros:" +str(resultado2))


    if a >= 10:
        superficie = ((a * 4) + 7) / (a + 90)
        superficie = round(superficie, 2)
        resultado2 = (superficie * l) / float(h)
        resultado2 = round(resultado2, 2)
        resultado_scp.configure(text=" superficie corporal:" +str(superficie))
        resultado_liquidos.configure(text=" Mililitros:" +str(resultado2))

def generar():
    indicacion = "Liquidos calculados a " +str(mililitros.get())
    escribe_indicaciones.pack(expand= True)
    escribe_indicaciones.config(state="normal")
    escribe_indicaciones.delete("0", "end")
    escribe_indicaciones.insert('end', indicacion )

def generar2():
    nota = neuro.get()+ ", " +piel.get() + ", " + cabeza.get() + ", " + cuello.get() + ", " + torax.get() + ", " + abdomen.get() + ", " + extremidades.get()
    generar_nota.pack(expand= True)
    generar_nota.config(state="normal")
    generar_nota.insert('end', nota )

def calculadora():
    a = paracetamol.get()
    paracetamol = 


def _salir():
    ventana.quit()
    ventana.destroy()
    exit()

def _mensaje():
    msg.showinfo('Acerca de','Creado por JALR para comunicacion jalr980@gmail.com')

#Menu
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Comunicacion", command= _mensaje)
archivo_menu.add_command(label="Salir", command= _salir)
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)


#========================================================================================================


#Frame de DATOS
frame_Datos = ttk.LabelFrame(tab2, text="Datos del paciente")
frame_Datos.grid(column=0, row=0, padx=8, pady=4)
#Caja de datos del paciente
ttk.Label(frame_Datos, text="Peso").grid(column=0, row=0)
peso = tk.IntVar()
escribir_peso= ttk.Entry(frame_Datos, width=12, textvariable=peso)
escribir_peso.grid(column=1, row=0)
ttk.Label(frame_Datos, text="Talla").grid(column=0, row=1)
talla = tk.IntVar()
escribir_talla= ttk.Entry(frame_Datos, width=12, textvariable=talla)
escribir_talla.grid(column=1, row=1)
#============================================================================================================
#Frame de liquidos
frame_Liquidos = ttk.LabelFrame(tab2, text="Liquidos")
frame_Liquidos.grid(column=0, row=1)

#caja de texto de liquidos
ttk.Label(frame_Liquidos, text="Liquido").grid(column=0, row=1)
mililitros = tk.IntVar()
escribir_ml= ttk.Entry(frame_Liquidos, width=15, textvariable=mililitros)
escribir_ml.grid(column=1, row=1)
#============================================================================================================

#Frame de horas
frame_tiempo = ttk.LabelFrame(tab2, text="Horas")
frame_tiempo.grid(column=1, row=2)
ttk.Label(frame_Liquidos, text="Horas").grid(column=0, row=0)
#COMBOBOX ELECCION DE TIEMPO
hrs = tk.StringVar()
hrelegida= ttk.Combobox(frame_Liquidos, width=12, textvariable=hrs, state="readonly")
hrelegida['values'] = (6, 8, 12)
hrelegida.grid(column=1,row=0)
hrelegida.current(0)
#========================================================================================
#Frame de resultados
frame_Resultados = ttk.LabelFrame(tab2, text="Resultado")
frame_Resultados.grid(column=1, row=0)

#Indicaciones
indicaciones = tk.StringVar()
escribe_indicaciones = ttk.Entry(tab3, width = 70)
escribe_indicaciones.grid(column=0, row=0)
#etiqueta de superficie corporal
resultado_scp = ttk.Label(frame_Resultados,text="Superficie corporal:")
resultado_scp.grid(column=2, row=0)
#etiqueta de liquidos
resultado_liquidos = ttk.Label(frame_Resultados,text="Mililitros:")
resultado_liquidos.grid(column=2, row=1)
#boton
calculo = ttk.Button(frame_Resultados, text="calcular", command=liquidos)
calculo.grid(column=0, row=0)
boton2 = ttk.Button(frame_Resultados, text="Generar indicaciones", command=generar)
boton2.grid(column=0, row=2)
#=============================================================================================
#frame nota
frame_Nota = ttk.LabelFrame(tab1, text="Exploracion")
frame_Nota.grid(column=0, row=0)
ttk.Label(frame_Nota, text="Neurológico").grid(column=0, row=0)
ttk.Label(frame_Nota, text="Piel").grid(column=0, row=1)
ttk.Label(frame_Nota, text="Cabeza").grid(column=0, row=2)
ttk.Label(frame_Nota, text="cuello").grid(column=0, row=3)
ttk.Label(frame_Nota, text="Tórax").grid(column=0, row=4)
ttk.Label(frame_Nota, text="Abdomen").grid(column=0, row=5)
ttk.Label(frame_Nota, text="Extremidades").grid(column=0, row=6)

frame_Nota2 = ttk.LabelFrame(tab1, text="Nota")
frame_Nota2.grid(column=0, row=2)
#caja de texto
neuro = tk.StringVar()
escribir_neuro= ttk.Entry(frame_Nota, width=200, textvariable=neuro)
escribir_neuro.insert("end","Consciente, alerta, cooperador")
escribir_neuro.grid(column=1, row=0)
piel = tk.StringVar()
escribir_piel= ttk.Entry(frame_Nota, width=200, textvariable=piel)
escribir_piel.grid(column=1, row=1)
escribir_piel.insert("end","buena hidratación de piel y tegumentos")
cabeza = tk.StringVar()
escribir_cabeza= ttk.Entry(frame_Nota, width=200, textvariable=cabeza)
escribir_cabeza.grid(column=1, row=2)
escribir_cabeza.insert("end","cráneo normocéfalo, pupilas isocóricas normorreflécticas, narinas permeables, caes sin alteraciones, mucosa oral hidratada, faringe integra sin presencia de exudados")
cuello = tk.StringVar()
escribir_cuello= ttk.Entry(frame_Nota, width=200, textvariable=cuello)
escribir_cuello.grid(column=1, row=3)
escribir_cuello.insert("end","cuello cilíndrico sin presencia de adenomegalias")
torax = tk.StringVar()
escribir_torax= ttk.Entry(frame_Nota, width=200, textvariable=torax)
escribir_torax.grid(column=1, row=4)
escribir_torax.insert("end","tórax simétrico, campos pulmonares ventilados, murmullo vesicular presente, sin presencia de estertores ni sibilancias, ruidos cardiacos rítmicos de buena intensidad sin ruidos agregados")
abdomen = tk.StringVar()
escribir_abdomen= ttk.Entry(frame_Nota, width=200, textvariable=abdomen)
escribir_abdomen.grid(column=1, row=5)
escribir_abdomen.insert("end","abdomen blando depresible, peristaltismo presente, sin presencia de visceromegalias ni datos de irritación peritoneal")
extremidades = tk.StringVar()
escribir_extremidades= ttk.Entry(frame_Nota, width=200, textvariable=extremidades)
escribir_extremidades.grid(column=1, row=6)
escribir_extremidades.insert("end","extremidades integras, llenado capilar inmediato.")

note=tk.StringVar()
generar_nota = ScrolledText(frame_Nota2, font=("Arial", 12))
generar_nota.grid(column=0, row=1)

boton3 = ttk.Button(frame_Nota, text="Generar exploracion fisica ", command=generar2)
boton3.grid(column=0, row=7)

ventana.mainloop()
