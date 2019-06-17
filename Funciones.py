from tkinter import *
def sumar(num1,num2):
    return num1+num2
def restar(num1,num2):
    return num1-num2
def multiplicar(num1,num2):
    return num1*num2
def dividir(num1,num2):
    return num1/num2

def operaciones(num,txt):
    if(operacion=="+"):
        txt.insert(0,str(sumar(float(num[0]),float(num[1]))))
    elif(operacion=="-"):
        txt.insert(0,str(restar(float(num[0]),float(num[1]))))
    elif(operacion=="*"):
        txt.insert(0,str(multiplicar(float(num[0]),float(num[1]))))
    elif(operacion=="/"):
        txt.insert(0,str(dividir(float(num[0]),float(num[1]))))
    cast=txt.get().split(".")
    if(cast[1]=="0"):
        to_int=int(float(txt.get()))
        txt.delete(0,END)
        txt.insert(0,str(to_int))
aux=""
operacion=""
def clicked(tecla,txt):
    global operacion
    txt.config(state="normal")
    aux=txt.get()
    txt.delete(0,END)
    if(tecla!="+" and tecla!="-" and tecla!="*" and tecla!="/" and tecla!="="):
        txt.insert(0,aux+tecla)
    if(tecla=="+" or tecla=="-" or tecla=="*" or tecla=="/"):
        if(operacion==""):
            txt.insert(0,aux+tecla)
            operacion=tecla
        else:
            txt.insert(0,aux+tecla)
    if(tecla=="=" and operacion!=""):
        num=aux.split(operacion)
        operaciones(num,txt)
        operacion=""
    if(tecla=="+" or tecla=="-" or tecla=="*" or tecla=="/"):
        if(operacion!=""):
            num=aux.split(operacion)
            if(len(num)==2):
                txt.delete(0,END)
                operaciones(num,txt)
                resultado=txt.get()
                txt.delete(0,END)
                txt.insert(0,str(resultado)+tecla)
                operacion=tecla
    txt.config(state="disabled")