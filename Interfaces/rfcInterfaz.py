#Interfaz para obtener el rfc de un usuario
import tkinter as tk
class operacion:
    
    def generar(app,apm,nom,di,me,an):
        let1=app[0]
        let2=""
        let3=apm[0]
        let4=nom[0]
        let5=di
        let6=me
        let7=an[2:4]
        vocal=""
        p=app.lower()
        for i in range(len(p)):
            vocal=p[i]
            
            if vocal=="a":
                let2="a"
                i=30
            elif vocal=="e":
                let2="e"
                i=30
            elif vocal=="i":
                let2="i"
                i=30
            elif vocal=="o":
                let2="o"
                i=30
            elif vocal=="u":
                let2="u"
                i=30
        
        return let1.lower()+let2.lower()+let3.lower()+let4.lower()+let5+let6+let7
        
    pass

def rfc():
    try:
        apepa=apellidoP.get()
        apema=apellidoM.get()
        nomb=nombre.get()
        d=dia.get()
        m=mes.get()
        a=año.get()
        genereado=" "
        generado=operacion.generar(apepa,apema,nomb,d,m,a)
        
        result.configure(text=f"Su rfc es: {generado}")
        
        pass
    except ValueError:
        
        pass
    
    pass

ventana=tk.Tk()
ventana.title("________RFC________")

label1=tk.Label(ventana,text="Ingrese su apellido paterno: ")
label1.grid(row=0,column=0,padx=10,pady=10)

apellidoP=tk.Entry(ventana)
apellidoP.grid(row=0,column=1,padx=10,pady=10)

label2=tk.Label(ventana,text="Ingrese su apellido materno: ")
label2.grid(row=1,column=0,padx=10,pady=10)

apellidoM=tk.Entry(ventana)
apellidoM.grid(row=1,column=1,padx=10,pady=10)

label3=tk.Label(ventana,text="Ingrese su nombre: ")
label3.grid(row=2,column=0,padx=10,pady=10)

nombre=tk.Entry(ventana)
nombre.grid(row=2,column=1,padx=10,pady=10)

label4=tk.Label(ventana,text="Ingrese su fecha de (DD|MM|AA): ")
label4.grid(row=3,column=0,padx=10,pady=10)

dia = tk.Entry(ventana, width=5)
dia.grid(row=3, column=1, padx=(0, 5), pady=10, sticky='w')

mes = tk.Entry(ventana, width=5)
mes.grid(row=3, column=1, padx=(65, 5), pady=10, sticky='w')

año = tk.Entry(ventana, width=5)
año.grid(row=3, column=1, padx=(130, 10), pady=10, sticky='w')

boton=tk.Button(ventana,text="Generelo",command=rfc)
boton.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

result=tk.Label(ventana)
result.grid(row=5,column=0,columnspan=2,padx=10,pady=10)


ventana.mainloop()