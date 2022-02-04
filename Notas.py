import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
ventana.title("Liquidos")

# funciones
def _salir():
    ventana.quit()
    ventana.destroy()
    exit()

def _mensaje():
    msg.showinfo('Acerca de','Creado por JALR para comunicacion jalr980@gmail.com')

tab = ttk.Notebook(ventana)
tab1 = ttk.Frame(tab)
tab.add(tab1, text="Historia Clinica")
tab.pack(expand=1, fill="both")
tab2 = ttk.Frame(tab)
tab.add(tab2, text="Nota Medica")
tab.pack(expand=1, fill="both")

#Menu
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Comunicacion", command= _mensaje)
archivo_menu.add_command(label="Salir", command= _salir)
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)

#FRAME DE IDENTIFICACION
frame_identificacion = ttk.LabelFrame(tab1, text="Datos del paciente")
frame_identificacion.grid(column=0, row=0, padx=4, pady=2)

ttk.Label(frame_identificacion, text="Apellido paterno").grid(column=0, row=0, padx=4, pady=2)
paterno= tk.StringVar()
a_paterno= ttk.Entry(frame_identificacion, width=20, textvariable=paterno)
a_paterno.grid(column=1, row=0, padx=8, pady=4)

ttk.Label(frame_identificacion, text="Apellido materno").grid(column=2, row=0, padx=4, pady=2)
paterno= tk.StringVar()
a_paterno= ttk.Entry(frame_identificacion, width=20, textvariable=paterno)
a_paterno.grid(column=3, row=0, padx=8, pady=4)

ttk.Label(frame_identificacion, text="Nombre").grid(column=4, row=0, padx=4, pady=2)
paterno= tk.StringVar()
a_paterno= ttk.Entry(frame_identificacion, width=20, textvariable=paterno)
a_paterno.grid(column=5, row=0, padx=4, pady=2)

ttk.Label(frame_identificacion, text="sexo").grid(column=0, row=1, padx=4, pady=2)
sx = tk.StringVar()
elec_sx= ttk.Combobox(frame_identificacion, width=12, textvariable=sx, state="readonly")
elec_sx['values'] = ("Femenino", "Masculino")
elec_sx.grid(column=1,row=1, padx=4, pady=2)
elec_sx.current(0)

ttk.Label(frame_identificacion, text="Fecha de nacimiento").grid(column=0, row=2, padx=4, pady=2)
ttk.Label(frame_identificacion, text="Dia").grid(column=1, row=2, padx=4, pady=2)
dia = tk.StringVar()
elec_dia = ttk.Entry(frame_identificacion, width=20, textvariable=dia)
elec_dia.grid(column=2,row=2, padx=4, pady=2)

ttk.Label(frame_identificacion, text="Mes").grid(column=3, row=2, padx=4, pady=2)
mes = tk.StringVar()
elec_mes = ttk.Entry(frame_identificacion, width=20, textvariable=dia)
elec_mes.grid(column=4,row=2, padx=4, pady=2)

ttk.Label(frame_identificacion, text="Ano").grid(column=5, row=2, padx=4, pady=2)
ano = tk.StringVar()
elec_ano = ttk.Entry(frame_identificacion, width=20, textvariable=dia)
elec_ano.grid(column=6,row=2, padx=4, pady=2)

#frame interrogatorio
frame_interrogatorio = ttk.LabelFrame(tab1, text="Interrogatorio")
frame_interrogatorio.grid(column=0, row=2, padx=4, pady=2)

ttk.Label(frame_interrogatorio, text="Antecedentes heredofamiliares").grid(column=0, row=0, padx=4, pady=2)
heredofamiliar=tk.StringVar()
esc_heredofamiliar = ScrolledText(frame_interrogatorio, font=("Arial", 12),width=40, height=10)
esc_heredofamiliar.insert("end","Interrogados y negados")
esc_heredofamiliar.grid(column=1, row=0, padx=4, pady=2)

ttk.Label(frame_interrogatorio, text="Antecedentes personales patologico").grid(column=0, row=1, padx=4, pady=2)
personalpat=tk.StringVar()
esc_personalpat = ScrolledText(frame_interrogatorio, font=("Arial", 12), width=40, height=10)
esc_personalpat.insert("end","Alergias a medicamentos, Enfermedades cronicodegenerativos, hospitalizaciones, cirugias,  transfuciones, traumatismos negados")
esc_personalpat.grid(column=1, row=1, padx=4, pady=2)

ttk.Label(frame_interrogatorio, text="Antecedentes personales no patologicos").grid(column=0, row=2, padx=4, pady=2)
personalnot=tk.StringVar()
esc_personalno = ScrolledText(frame_interrogatorio, font=("Arial", 12),width=40, height=10)
esc_personalno.insert("end","Interrogado y negados")
esc_personalno.grid(column=1, row=2, padx=4, pady=2)

#Frame signos vitales
frame_vitales = ttk.LabelFrame(tab1, text="Signos Vitales")
frame_vitales.grid(column=0, row=1, padx=4, pady=2)

ttk.Label(frame_vitales, text="Frecuencia cardiaca").grid(column=0, row=0, padx=4, pady=2)
fc= tk.StringVar()
elec_fc= ttk.Entry(frame_vitales, width=20, textvariable=fc)
elec_fc.grid(column=1, row=0, padx=4, pady=2)

ttk.Label(frame_vitales, text="Frecuencia respiratoria").grid(column=2, row=0, padx=4, pady=2)
fr= tk.StringVar()
elec_fr= ttk.Entry(frame_vitales, width=20, textvariable=fr)
elec_fr.grid(column=3, row=0, padx=4, pady=2)

ttk.Label(frame_vitales, text="Tension arterial").grid(column=4, row=0, padx=4, pady=2)
ta= tk.StringVar()
elec_ta= ttk.Entry(frame_vitales, width=20, textvariable=ta)
elec_ta.grid(column=5, row=0, padx=4, pady=2)

ttk.Label(frame_vitales, text="Saturacion O2").grid(column=6, row=0, padx=4, pady=2)
sat= tk.StringVar()
elec_sat= ttk.Entry(frame_vitales, width=20, textvariable=sat)
elec_sat.grid(column=7, row=0, padx=4, pady=2)

ttk.Label(frame_vitales, text="Temperatura").grid(column=8, row=0, padx=4, pady=2)
temp= tk.StringVar()
elec_temp= ttk.Entry(frame_vitales, width=20, textvariable=temp)
elec_temp.grid(column=9, row=0, padx=4, pady=2)

ttk.Label(frame_vitales, text="Peso").grid(column=0, row=1, padx=4, pady=2)
peso= tk.StringVar()
elec_peso= ttk.Entry(frame_vitales, width=20, textvariable=peso)
elec_peso.grid(column=1, row=1, padx=4, pady=2)

ttk.Label(frame_vitales, text="Talla").grid(column=2, row=1, padx=4, pady=2)
talla= tk.StringVar()
elec_tall= ttk.Entry(frame_vitales, width=20, textvariable=talla)
elec_tall.grid(column=3, row=1, padx=4, pady=2)

ttk.Label(frame_vitales, text="IMC").grid(column=4, row=1, padx=4, pady=2)
imc= tk.StringVar()
elec_imc= ttk.Entry(frame_vitales, width=20, textvariable=imc)
elec_imc.grid(column=5, row=1, padx=4, pady=2)

ventana.mainloop()
