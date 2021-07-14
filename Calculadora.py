from tkinter import *
import Funciones
window=Tk()
window.title("Calculadora")

app_width=293#     dimensiones de ventana
app_height=280
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
app_posx=int(screen_width/2-app_width/2)#   centrar en pantalla
app_posy=int(screen_height/2-app_height/2)
window.geometry(f"{app_width}x{app_height}+{app_posx}+{app_posy}")

entry_color="#B8C9F5"
calc_color="#141E36"
window_color="#293D6E"
btn_color="#5D88F5"
btn_group_color=calc_color
hover_color=entry_color

window.configure(background=window_color)
frame=Frame(window,background=calc_color)
frame.pack(fill=None,expand=False)

txt=Entry(frame,
        disabledbackground=entry_color,
        disabledforeground="black",
        font=("Arial Bold",15),
        width=15,
        state='disabled',
        borderwidth=0,highlightthickness=0)

txt.grid(columnspan=3,row=0,pady=10)
btn=[[0]*4]*4#          crear matriz de botones
frame=LabelFrame(frame,background=btn_group_color,borderwidth=0,highlightthickness=0)
frame.grid(column=1,row=1,pady=10,padx=6)

for x in range(0,4):
    for y in range(0,4):
        tecla=""
        if(x==0 or x==1 or x==2):
            range_={0:str(x+1),1:str(x+4),2:str(x+7)}#  | numeros posibles por columna
            tecla=range_.get(y) or ""
        if(x==3):
            operations={0:"+",1:"-",2:"*",3:"/"}#       | simbolos de la cuarta columna
            tecla=operations.get(y) or ""
        if(y==3):
            special={0:"0",1:".",2:"=",3:"/"}#          | asignar ultima fila
            tecla=special.get(x) or ""
        btn[x][y]=Button(frame,
                background=btn_color,
                text=tecla,#                            | asignar simbolo al boton
                activebackground=hover_color,
                command=lambda tecla=tecla: Funciones.clicked(tecla,txt),
                width=2,height=1,font=("Arial Bold",20),
                borderwidth=0,highlightthickness=0)
        btn[x][y].grid(column=x,row=y,pady=6,padx=6)
window.mainloop()
