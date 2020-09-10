from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import process
import api


APIkey = '940b74af-8410-4516-9326-e39b07de8cdd'
interface = api.API(APIkey)

root = Tk()

top_label = Label(root, text='5 day forcast')
top_label.grid(row=0, column=0)

def images(code):

    return ImageTk.PhotoImage(Image.open(f'icons/{code}.ico'))


notebook = ttk.Notebook(root)
notebook.grid(row=2, column=0)

frame1 = Frame(notebook, width=500, height=500)
frame2 = Frame(notebook, width=500, height=500)
frame3 = Frame(notebook, width=500, height=500)
frame4 = Frame(notebook, width=500, height=500)
frame5 = Frame(notebook, width=500, height=500)


frame1.grid(row=2, column=0)
frame2.grid(row=2, column=0)
frame3.grid(row=2, column=0)
frame4.grid(row=2, column=0)
frame5.grid(row=2, column=0)


notebook.add(frame1, text=process.tabs()[0])
notebook.add(frame2, text=process.tabs()[1])
notebook.add(frame3, text=process.tabs()[2])
notebook.add(frame4, text=process.tabs()[3])
notebook.add(frame5, text=process.tabs()[4])



user_input = Entry(root, width=60)
user_input.grid(row=1, column=0)



    

def template(data, time, frame): #make day 5-2 template

        
    img_lst = [images(data[14][i]) for i in range(8)]
        
    temp_list = data[13]
    
    time_lab1 = Label(frame, text=time[0])
    time_lab2 = Label(frame, text=time[1])
    time_lab3 = Label(frame, text=time[2])
    time_lab4 = Label(frame, text=time[3])
    time_lab5 = Label(frame, text=time[4])
    time_lab6 = Label(frame, text=time[5])
    time_lab7 = Label(frame, text=time[6])
    time_lab8 = Label(frame, text=time[7])
    
    temp_lab1 = Label(frame, text=temp_list[0])
    temp_lab2 = Label(frame, text=temp_list[1])
    temp_lab3 = Label(frame, text=temp_list[2])
    temp_lab4 = Label(frame, text=temp_list[3])
    temp_lab5 = Label(frame, text=temp_list[4])
    temp_lab6 = Label(frame, text=temp_list[5])
    temp_lab7 = Label(frame, text=temp_list[6])
    temp_lab8 = Label(frame, text=temp_list[7])
        
    weath_lab1 = Label(frame, image=img_lst[0])
    weath_lab2 = Label(frame, image=img_lst[1])
    weath_lab3 = Label(frame, image=img_lst[2])
    weath_lab4 = Label(frame, image=img_lst[3])
    weath_lab5 = Label(frame, image=img_lst[4])
    weath_lab6 = Label(frame, image=img_lst[5])
    weath_lab7 = Label(frame, image=img_lst[6])
    weath_lab8 = Label(frame, image=img_lst[7])
    # Refrence to image in Tkinter object.
    weath_lab1.image = img_lst[0]
    weath_lab2.image = img_lst[1]
    weath_lab3.image = img_lst[2]
    weath_lab4.image = img_lst[3]
    weath_lab5.image = img_lst[4]
    weath_lab6.image = img_lst[5]
    weath_lab7.image = img_lst[6]
    weath_lab8.image = img_lst[7]


    time_lab1.grid(row=0, column=0)
    time_lab2.grid(row=0, column=1)
    time_lab3.grid(row=0, column=2)
    time_lab4.grid(row=0, column=3)
    time_lab5.grid(row=0, column=4)
    time_lab6.grid(row=0, column=5)
    time_lab7.grid(row=0, column=6)
    time_lab8.grid(row=0, column=7)
    
    weath_lab1.grid(row=1, column=0)
    weath_lab2.grid(row=1, column=1)
    weath_lab3.grid(row=1, column=2)
    weath_lab4.grid(row=1, column=3)
    weath_lab5.grid(row=1, column=4)
    weath_lab6.grid(row=1, column=5)
    weath_lab7.grid(row=1, column=6)
    weath_lab8.grid(row=1, column=7)
    
    temp_lab1.grid(row=2, column=0)
    temp_lab2.grid(row=2, column=1)
    temp_lab3.grid(row=2, column=2)
    temp_lab4.grid(row=2, column=3)
    temp_lab5.grid(row=2, column=4)
    temp_lab6.grid(row=2, column=5)
    temp_lab7.grid(row=2, column=6)
    temp_lab8.grid(row=2, column=7)
    

def day1(data, time):
    
    day1_time = Label(frame1, text=process.time_intervals(len(data[1])))
    img_lst = [images(data[14][i]) for i in range(len(data[1]))]
    temp_list = data[13]
    
    try:
        time_lab1 = Label(frame1, text=time[0])
        time_lab2 = Label(frame1, text=time[1])
        time_lab3 = Label(frame1, text=time[2])
        time_lab4 = Label(frame1, text=time[3])
        time_lab5 = Label(frame1, text=time[4])
        time_lab6 = Label(frame1, text=time[5])
        time_lab7 = Label(frame1, text=time[6])
        time_lab8 = Label(frame1, text=time[7])      
    except:
        pass
    
    try:
        weath_lab1 = Label(frame1, image=img_lst[0])
        weath_lab2 = Label(frame1, image=img_lst[1])
        weath_lab3 = Label(frame1, image=img_lst[2])
        weath_lab4 = Label(frame1, image=img_lst[3])
        weath_lab5 = Label(frame1, image=img_lst[4])
        weath_lab6 = Label(frame1, image=img_lst[5])
        weath_lab7 = Label(frame1, image=img_lst[6])
        weath_lab8 = Label(frame1, image=img_lst[7])    
    except:
        pass
    
    try:
        # Refrence to image in Tkinter object.
        weath_lab1.image = img_lst[0]
        weath_lab2.image = img_lst[1]
        weath_lab3.image = img_lst[2]
        weath_lab4.image = img_lst[3]
        weath_lab5.image = img_lst[4]
        weath_lab6.image = img_lst[5]
        weath_lab7.image = img_lst[6]
        weath_lab8.image = img_lst[7]
    except:
        pass
    
    try:
        temp_lab1 = Label(frame1, text=temp_list[0])
        temp_lab2 = Label(frame1, text=temp_list[1])
        temp_lab3 = Label(frame1, text=temp_list[2])
        temp_lab4 = Label(frame1, text=temp_list[3])
        temp_lab5 = Label(frame1, text=temp_list[4])
        temp_lab6 = Label(frame1, text=temp_list[5])
        temp_lab7 = Label(frame1, text=temp_list[6])
        temp_lab8 = Label(frame1, text=temp_list[7])
    except:
        pass

    try:
        time_lab1.grid(row=0, column=0)
        time_lab2.grid(row=0, column=1)
        time_lab3.grid(row=0, column=2)
        time_lab4.grid(row=0, column=3)
        time_lab5.grid(row=0, column=4)
        time_lab6.grid(row=0, column=5)
        time_lab7.grid(row=0, column=6)
        time_lab8.grid(row=0, column=7)    
    except:
        pass
    
    try:    
        weath_lab1.grid(row=1, column=0)
        weath_lab2.grid(row=1, column=1)
        weath_lab3.grid(row=1, column=2)
        weath_lab4.grid(row=1, column=3)
        weath_lab5.grid(row=1, column=4)
        weath_lab6.grid(row=1, column=5)
        weath_lab7.grid(row=1, column=6)
        weath_lab8.grid(row=1, column=7)
    except:
        pass
    
    try:   
        temp_lab1.grid(row=2, column=0)
        temp_lab2.grid(row=2, column=1)
        temp_lab3.grid(row=2, column=2)
        temp_lab4.grid(row=2, column=3)
        temp_lab5.grid(row=2, column=4)
        temp_lab6.grid(row=2, column=5)
        temp_lab7.grid(row=2, column=6)
        temp_lab8.grid(row=2, column=7)
    except:
        pass
    


def click():
    

    siteid = interface.get_site_id_from_user_input(user_input.get())
    api_data = interface.get_data_from_api(siteid)
    data = process.split_lists(api_data, 5)
    time = process.time_intervals(8)


    template(data, time, frame5)
    template(data, time, frame4)
    template(data, time, frame3)
    template(data, time, frame2)

    day1(data, time)    


search = Button(root, text='search', command=click)
search.grid(row=1, column=1)

root.mainloop()

