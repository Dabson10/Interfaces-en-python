import tkinter as tk 

def suma():
    try: 
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_result.config(text=f"Resultado: {result}")
    except ValueError:
        label_result.config(text="Los números no son válidos")

ventana = tk.Tk()
ventana.title("Suma de dos números")

label1 = tk.Label(ventana, text="Número 1: ")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(ventana, text="Número 2: ")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1, padx=10, pady=10)

boton_sumar = tk.Button(ventana, text="Sumar", command=suma)
boton_sumar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(ventana, text="Resultado: ")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
