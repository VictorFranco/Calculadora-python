from tkinter import *
import Funciones
window=Tk()
window.title("Calculadora")

app_width=293
app_height=300
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
app_posx=int(screen_width/2-app_width/2)
app_posy=int(screen_height/2-app_height/2)
window.geometry(f"{app_width}x{app_height}+{app_posx}+{app_posy}")# dimensiones de ventana

calc_color="#141E36"
btn_color="#5D88F5"
btn_group_color="#2E437A"

window.configure(background=calc_color)
txt=Entry(window,text="Escribe un numero",font=("Arial Bold", 15),width=15,state='disabled')
txt.grid(columnspan=3,row=0,pady=10)
btn=[[0]*4]*4
frame=LabelFrame(window,background=btn_group_color,borderwidth=0,highlightthickness=0)
frame.grid(column=1,row=1,pady=10,padx=6)
for x in range(0,4):
    for y in range(0,4):
        tecla=""
        if(x==0 or x==1 or x==2):
            if(y==0):
                tecla=str(x+1)
            if(y==1):
                tecla=str(x+4)
            if(y==2):
                tecla=str(x+7)
        if(x==3):
            if(y==0):
                tecla="+"
            if(y==1):
                tecla="-"
            if(y==2):
                tecla="*"
            if(y==3):
                tecla="/"
        if(y==3):
            if(x==0):
                tecla="0"
            if(x==1):
                tecla="."
            if(x==2):
                tecla="="
        btn[x][y]=Button(frame,background=btn_color,borderwidth=0,highlightthickness=0,text=tecla,command=lambda tecla=tecla: Funciones.clicked(tecla,txt),width=2,height=1, font=("Arial Bold", 20))
        btn[x][y].grid(column=x,row=y,pady=6,padx=6)
window.mainloop()
