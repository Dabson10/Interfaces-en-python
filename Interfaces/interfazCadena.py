#Interfaz de usuario para las cadenas de texto 
import tkinter as tk
class operacion:
    def contador(palabra,letra):
        frase=palabra
        let=letra
        i=0
        cont=0
        for i in range(len(frase)):
            llet=frase[i]
            if let==llet:
                cont+=1
        return f"{cont}"
    
    def invertida(palabra):
        frase=palabra
        cont=len(frase)-1
        completa=""
        for cont in range (cont,-1,-1):
            llet=frase[cont]
            completa=completa+llet
        return f"{completa}"
    def mayusculas(palabra):
        letra=palabra
        return f"{letra.upper()}"
    
    def minusculas(palabra):
        letra=palabra
        return f"{letra.lower()}"


def limpiar():
    try:
        print
        repetido.configure(text=f"")
        inverso.configure(text=f"")
        mayuscula.configure(text=f"")
        minuscu.configure(text=f"")
    except ValueError:
        print()

def funcion_Cadenas():
    try:
        cadena=str(entrada1.get())
        letra=str(entrada2.get())

        resultado1=operacion.contador(cadena,letra)
        invert=operacion.invertida(cadena)
        mayus=operacion.mayusculas(cadena)
        minus=operacion.minusculas(cadena)
        
        repetido.configure(text=f"{resultado1}")
        inverso.configure(text=f"{invert}")
        mayuscula.configure(text=f"{mayus}")
        minuscu.configure(text=f"{minus}")
        
    except ValueError:
        print()
    pass

interfaz=tk.Tk()
interfaz.title("Cadenas de texto")

caja1=tk.Label(interfaz,text="Ingrese una cadena de texto: ")
caja1.grid(row=0,column=0,padx=10,pady=10)

# Esta primera caja recibe el valor de la cadena de texto
entrada1=tk.Entry(interfaz)
entrada1.grid(row=0,column=1,padx=10,pady=10)

caja2=tk.Label(interfaz,text="Ingrese una letra para buscar: ")
caja2.grid(row=1,column=0,padx=10,pady=10)
# Esta caja recibe una letra 
entrada2=tk.Entry(interfaz)
entrada2.grid(row=1,column=1,padx=10,pady=10)

caja3=tk.Label(interfaz,text="Cantidad de veces repetidas: ")
caja3.grid(row=2,column=0,padx=10,pady=10)
# En este bloque se muestra el resultado de las veces que se repitio una letra 
repetido=tk.Label(interfaz)
repetido.grid(row=2,column=1,padx=10,pady=10)

caja4=tk.Label(interfaz,text="Palabra invertida: ")
caja4.grid(row=3,column=0,padx=10,pady=10)
# En esta se muestra la palabra invertida
inverso=tk.Label(interfaz)
inverso.grid(row=3,column=1,padx=10,pady=10)

caja5=tk.Label(interfaz,text="En mayusculas: ")
caja5.grid(row=4,column=0,padx=10,pady=10)
# Convierte en mayuscula la palabra ingresada al inicio
mayuscula=tk.Label(interfaz)
mayuscula.grid(row=4,column=1,padx=10,pady=10)

caja6=tk.Label(interfaz,text="En minusculas: ")
caja6.grid(row=5,column=0,padx=10,pady=10)
# Convierte en mayuscula la palabra ingresada al inicio
minuscu=tk.Label(interfaz)
minuscu.grid(row=5,column=1,padx=10,pady=10)

btnLimpiar=tk.Button(interfaz,text="Limpiar",command=limpiar)
btnLimpiar.grid(row=6,columnspan=1,padx=10,pady=10)

boton=tk.Button(interfaz,text="Generar",command=funcion_Cadenas)
boton.grid(row=6,columnspan=3,padx=10,pady=10)
interfaz.mainloop()

