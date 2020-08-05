from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import process
import api

APIkey = '940b74af-8410-4516-9326-e39b07de8cdd'
interface = api.API(APIkey)

root = Tk()

my_label = Label(root, text='5 day forcast')
my_label.grid(row=0, column=0)


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


user_input = Entry(root,width=60)
user_input.grid(row=1, column=0)


def click():
    pass
    siteid = interface.get_site_id_from_user_input(user_input.get())
    data = (interface.get_data_from_api(siteid))
    times = interface.get_timestamp()
    
    day5_temp = Label(frame5, text=data[0][-8:])
    day5_weather = Label(frame5, text=data[1][-8:])
    day5_time = Label(frame5, text=times[-8:])
    day5_temp.grid(row=0, column=0)
    day5_weather.grid(row=1, column=0)
    day5_time.grid(row=2, column=0)
    
    day4_temp = Label(frame4, text=data[0][-16:-8])
    day4_weather = Label(frame4, text=data[1][-16:-8])
    day4_time = Label(frame4, text=times[-16:-8])    
    day4_temp.grid(row=0, column=0)
    day4_weather.grid(row=1, column=0)
    day4_time.grid(row=2, column=0)
    
    day3_temp = Label(frame3, text=data[0][-24:-16])
    day3_weather = Label(frame3, text=data[1][-24:-16])
    day3_time = Label(frame3, text=times[-24:-16])
    day3_temp.grid(row=0, column=0)
    day3_weather.grid(row=1, column=0)
    day3_time.grid(row=2, column=0)
    
    day2_temp = Label(frame2, text=data[0][-32:-24])
    day2_weather = Label(frame2, text=data[1][-32:-24])
    day2_time = Label(frame2, text=times[-32:-24])
    day2_temp.grid(row=0, column=0)
    day2_weather.grid(row=1, column=0)
    day2_time.grid(row=2, column=0)
    
    day1_temp = Label(frame1, text=data[0][0:-32])
    day1_weather = Label(frame1, text=data[1][0:-32])
    day1_time = Label(frame1, text=times[0:-41])
    day1_temp.grid(row=0, column=0)
    day1_weather.grid(row=1, column=0)
    day1_time.grid(row=2, column=0)

search = Button(root, text='search', command=click)
search.grid(row=1, column=1)



# root.iconbitmap('C:\\Users\\johnm\\Documents\\data_science\\coding\\projects'
#                 '\\weather_gui') #change for github
# sun = ImageTk.PhotoImage(Image.open('sun.jpg'))
# rain = ImageTk.PhotoImage(Image.open('rain.png'))
# img_lable1 = Label(image=sun)
# img_lable2 = Label(image=rain)
# #img_lable1.grid(row=0, column=0)
# img_lable2.grid(row=0, column=3)


root.mainloop()

