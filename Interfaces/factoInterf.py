#Interfaz que hace el factorial de un numero 
import tkinter as tk

def facto():
    try:
        
        numero=int(entrada.get())
        
        def recursi(num):
            
            if num ==0:
                return 1
            else:
                return num*recursi(num-1)
        resultado=str(recursi(numero))
        lblResult.configure(text=f"El resultado es: {resultado}")
        
        pass
    except ValueError:
        lblResult.configure(text="Los numeros no son validos")
        pass
    
    
    pass


ventana=tk.Tk()
ventana.title("FACTORIAL")

label1=tk.Label(ventana,text="Ingrese el numero para factorizarlo: ")
label1.grid(row=1,column=0,padx=10,pady=10)

entrada=tk.Entry(ventana)
entrada.grid(row=1,column=1,padx=10,pady=10)

boton=tk.Button(ventana,text="Resultado", command=facto)
boton.grid(row=2,columnspan=2,padx=10,pady=10)

lblResult =tk.Label(ventana)
lblResult.grid(row=3,columnspan=2,padx=10,pady=10)


ventana.mainloop()