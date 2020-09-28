from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import process
import api_interactions


class WeatherForcast:
    """Graphic user interface for weather forcast."""
    
    def __init__(self, master):
        
        self.master = master
        self.master.title('5 Day Weather Forcast')
        self.master.iconbitmap('icons/top_icon.ico')
        self.toplabel = Label(master, text='5 day forcast')
        self.toplabel.grid(row=0, column=0, columnspan=2)
        self.notebook()
        self.user_input = Entry(master, width=50)
        self.user_input.grid(row=1, column=0, sticky='E')
        self.search = Button(master, text='search', command=self.click)
        self.search.grid(row=1, column=1, sticky='W')
     
    def images(self, code):
        """return image object of icon corresponding to code
        code(int): Number that correspondes to filename of icons.
        """
        
        return ImageTk.PhotoImage(Image.open(f'icons/{code}.ico'))
    
    def notebook(self):
        """Display notebook with five frames for tabs."""
        notebook = ttk.Notebook(self.master)
        notebook.grid(row=3, column=0, columnspan=2)
    
        w=400
        h=100
            
        global frame1
        global frame2
        global frame3
        global frame4
        global frame5
        
        frame1 = Frame(notebook, width=w, height=h)
        frame2 = Frame(notebook, width=w, height=h)
        frame3 = Frame(notebook, width=w, height=h)
        frame4 = Frame(notebook, width=w, height=h)
        frame5 = Frame(notebook, width=w, height=h)
        
        frame1.grid(row=3, column=0)
        frame2.grid(row=3, column=0)
        frame3.grid(row=3, column=0)
        frame4.grid(row=3, column=0)
        frame5.grid(row=3, column=0)
            
        notebook.add(frame1, text=process.tabs()[0])
        notebook.add(frame2, text=process.tabs()[1])
        notebook.add(frame3, text=process.tabs()[2])
        notebook.add(frame4, text=process.tabs()[3])
        notebook.add(frame5, text=process.tabs()[4])
        
    def template(self, icon, temp, time, frame): 
        """Template for inserting time, temperature and weather labels into a 
        frame. 
        icon(list): List of PIL.ImageTk.PhotoImage objects. 
        temp(list): List of temperatures.
        time(list) List of timeslots to be displayed.
        frame(TK object) Frame in which to insert data into
        """

        time_lab1 = Label(frame, text=time[0])
        time_lab2 = Label(frame, text=time[1])
        time_lab3 = Label(frame, text=time[2])
        time_lab4 = Label(frame, text=time[3])
        time_lab5 = Label(frame, text=time[4])
        time_lab6 = Label(frame, text=time[5])
        time_lab7 = Label(frame, text=time[6])
        time_lab8 = Label(frame, text=time[7])
        
        temp_lab1 = Label(frame, text=temp[0]+'°')
        temp_lab2 = Label(frame, text=temp[1]+'°')
        temp_lab3 = Label(frame, text=temp[2]+'°')
        temp_lab4 = Label(frame, text=temp[3]+'°')
        temp_lab5 = Label(frame, text=temp[4]+'°')
        temp_lab6 = Label(frame, text=temp[5]+'°')
        temp_lab7 = Label(frame, text=temp[6]+'°')
        temp_lab8 = Label(frame, text=temp[7]+'°')
            
        weath_lab1 = Label(frame, image=icon[0])
        weath_lab2 = Label(frame, image=icon[1])
        weath_lab3 = Label(frame, image=icon[2])
        weath_lab4 = Label(frame, image=icon[3])
        weath_lab5 = Label(frame, image=icon[4])
        weath_lab6 = Label(frame, image=icon[5])
        weath_lab7 = Label(frame, image=icon[6])
        weath_lab8 = Label(frame, image=icon[7])
        # Refrence to image in Tkinter object.
        weath_lab1.image = icon[0]
        weath_lab2.image = icon[1]
        weath_lab3.image = icon[2]
        weath_lab4.image = icon[3]
        weath_lab5.image = icon[4]
        weath_lab6.image = icon[5]
        weath_lab7.image = icon[6]
        weath_lab8.image = icon[7]
    
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
            
    def day1(self, data, timeslots):
        """Function for inserting time, temperature and weather labels into
        frame1
        data(list): API data with weather and time and temperature information.
        timeslots(list): timeslots to be displayed
        """
    
        time = timeslots[8-len(data[1]):]
        day1_time = Label(frame1, text=process.time_intervals(len(data[1])))
        img_lst = [self.images(data[2][i]) for i in range(len(data[1]))]
        temp_list = data[1]
        
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
            temp_lab1 = Label(frame1, text=temp_list[0]+'°')
            temp_lab2 = Label(frame1, text=temp_list[1]+'°')
            temp_lab3 = Label(frame1, text=temp_list[2]+'°')
            temp_lab4 = Label(frame1, text=temp_list[3]+'°')
            temp_lab5 = Label(frame1, text=temp_list[4]+'°')
            temp_lab6 = Label(frame1, text=temp_list[5]+'°')
            temp_lab7 = Label(frame1, text=temp_list[6]+'°')
            temp_lab8 = Label(frame1, text=temp_list[7]+'°')
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
            
    def user_inp(self):
        """Capatalizes input and dispays an error message if input doesn't
        match any of the API locations.
        """        
        
        inp_label = Label(self.master, text='', bg='#f0f0f0', width=45)
        inp_label.grid(row=2, column=0, columnspan=2)

        user_input = self.user_input.get().title()
        
        try:
            data = api_interactions.api_data(user_input)

            return data

        except:
            inp_label.config(text=f'{user_input} could not be found', 
                             bg='red', width=45)
            
    def click(self):
        """Split data into catagories and days and run template function"""
        
        data = self.user_inp()
        
        if data is not None:
            
            timeslots = 8
            time = process.time_intervals(timeslots)
        
            day5_image = [self.images(data[14][i]) for i in range(timeslots)] 
            day5_temp = data[13]
            day4_image = [self.images(data[11][i]) for i in range(timeslots)]
            day4_temp = data[10]
            day3_image = [self.images(data[8][i]) for i in range(timeslots)]
            day3_temp = data[7]
            day2_image = [self.images(data[5][i]) for i in range(timeslots)]
            day2_temp = data[4]
            
            self.template(day5_image, day5_temp, time, frame5)
            self.template(day4_image, day4_temp, time, frame4)
            self.template(day3_image, day3_temp, time, frame3)
            self.template(day2_image, day2_temp, time, frame2)
        
            self.day1(data, time)    
        
        
root = Tk()
weather = WeatherForcast(root)
root.mainloop()
