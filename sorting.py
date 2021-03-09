import tkinter as tk
#from tkinter import * 
from tkinter.ttk import *
import random


global sorted_data
algorithm_options = ['Bubble Sort','Insertion Sort']
class Shape:
    def __init__(self,master,canvas,data):
        self.master = master
        self.canvas = canvas
        self.data = data
        self.create()
    def create(self):
        # Creates a rectangle of 50x60 (heightxwidth) 
        C_width = 800
        C_height = 600
        X_width = C_width / (len(data)+1)
        offset = 5
        spacing =10
        for i,height in enumerate(data):
        #topHeight
            x0 = i * X_width + offset + spacing
            y0 = C_height - height
        ##bottom height
            x1 = (i+1) * X_width + offset
            y1 = C_height
            canvas.create_rectangle(x0,y0,x1,y1,fill="green")

        self.canvas.pack(expand=1)


def create_elements():
    list_of_elements = []
    for i in range(0,10):
         i = random.randint(100,200)
         list_of_elements.append(i)
    return list_of_elements


def bubbleSort_algorithm(data):
    temp = 0
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i] < data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

def insertion_sort(data):
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

def sort_handler():
    top = tk.Toplevel()
    top.title("Sorted Array!")
    canvas = tk.Canvas(top,width=800,height=600,bg="white")
    C_width = 800
    C_height = 600
    X_width = C_width / (len(sorted_data)+1)
    offset = 5
    spacing =10
    for i,height in enumerate(sorted_data):
        x0 = i * X_width + offset + spacing
        y0 = C_height - height
        ##bottom height
        x1 = (i+1) * X_width + offset
        y1 = C_height
        canvas.create_rectangle(x0,y0,x1,y1,fill="red")
    canvas.pack(expand=1)


    


if __name__ == "__main__": 
    root = tk.Tk()
    canvas = tk.Canvas(root,width=800,height=500,bg="white")
    #canvas1 = tk.Canvas(root,width=800,height=400,bg="white")
    data = create_elements()
    #print(data)
    frame = tk.Frame(root)
    label= Label(frame,text="Unsorted Array",justify=tk.LEFT)
    label.pack(side=tk.LEFT)
    ####Dropdown Menu
    variable = tk.StringVar(root)
    variable.set(algorithm_options[0])
    w = OptionMenu(frame,variable,*algorithm_options)
    w.pack()
    frame.pack(padx=1,pady=1)
    shape = Shape(root,canvas,data)
    sorted_data = bubbleSort_algorithm(data)
    button = tk.Button(text="Click to Sort",command=sort_handler)
    button.pack(side=tk.BOTTOM)
    #print(sorted_data)
    #shape1 = Shape(root,canvas1,sorted_data)
    root.title('Sorting visualizer')
    root.geometry('1000x600')
    root.mainloop()