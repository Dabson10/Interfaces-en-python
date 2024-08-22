#INterfaz de derivadas e integrales
import tkinter as tk

class operacion:
    
    def integral(num1,num2):
        #num2/num1+num1\
            operacion=num2+num1
            return f"({num1} / {operacion})x^({operacion} /{num1})"
    
    def derivada(num1,num2):
        operacion=num2-num1
        
        return f"({num2} / {num1} )x^ ({operacion}/ {num1})"
        pass

def operaciones():
    try:
        exRaiz=int(entrada1.get())
        expoX=int(entradax.get())
        objeto1=operacion.integral(exRaiz,expoX)
        
        resultadoInt.configure(text=f"{objeto1}")
        
        objeto2=operacion.derivada(exRaiz,expoX)
        resultadoDer.configure(text=f"{objeto2}")
        
        pass
    except ValueError:
        
        pass
    

ventana=tk.Tk()
ventana.title("Integrales y derivadas")

label1=tk.Label(ventana, text="Ingrese el exponente de la raiz:")
label1.grid(row=0,column=0,padx=10,pady=10)

entrada1=tk.Entry(ventana)
entrada1.grid(row=0,column=1,padx=10,pady=10)


label2=tk.Label(ventana,text="Ingrese el exponente de x: ")
label2.grid(row=1,column=0,padx=10,pady=10)

entradax=tk.Entry(ventana)
entradax.grid(row=1,column=1,padx=10,pady=10)

integral=tk.Button(ventana,text="Resultado",command=operaciones)
integral.grid(row=2,column=0,columnspan=1,padx=10,pady=10)


label3=tk.Label(ventana,text="Integal: ")
label3.grid(row=3,column=0,padx=10,pady=10)

resultadoInt=tk.Label(ventana)
resultadoInt.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

label4=tk.Label(ventana,text="Derivada")
label4.grid(row=4,column=0,padx=10,pady=10)

resultadoDer=tk.Label(ventana)
resultadoDer.grid(row=4,column=0,columnspan=2,padx=10,pady=10)



ventana.mainloop()