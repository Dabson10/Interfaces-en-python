import tkinter as tk

def multiplica():
    try:
        base=int(entrada1.get())
        limite=int(entrada2.get())
        resultado=""
        for i in range(1,limite+1):
            resultado +=f"{base} x {i} = {base*i}\n"
            
        result.configure(text=resultado)
        
        pass
    except ValueError: 
        result.config(text="Porfavor ingrese un numero correcto")
        pass
    
    pass

interfaz=tk.Tk()
interfaz.title("Tabla de multiplicar")

caja1=tk.Label(interfaz,text="Ingrese el numero base: ")
caja1.grid(row=0,column=0,padx=10,pady=10)

entrada1=tk.Entry(interfaz)
entrada1.grid(row=0,column=1,padx=10,pady=10)

caja2=tk.Label(interfaz,text="Ingrese el limite: ")
caja2.grid(row=1,column=0,padx=10,pady=10)

entrada2=tk.Entry(interfaz)
entrada2.grid(row=1,column=1,padx=10,pady=10)

boton=tk.Button(interfaz,text="Resultado",command=multiplica)
boton.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

result=tk.Label(interfaz)
result.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

interfaz.mainloop()