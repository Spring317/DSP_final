from tkinter import *
import math
from Note_detection import note_detection

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.attributes('-fullscreen', True)
        self.__root.resizable(width= False, height= False)    
      
        
    def normal_mode(self):
        self.__root.title('Normal mode')
        self.__root.geometry('1920x1080')
        
        frame = Canvas(self.__root, width= 1920, height= 1080, bg= 'white')
        frame.pack()
                
        
        exit_button = Button(frame, text = 'Exit', command= lambda: self.__root.destroy())
        exit_button.place(x= 1850, y= 0)
        
        Note = [82.41, 110, 146.83, 196, 246.94, 329.63]
        
        tune = note_detection()
        
        def chooseNote(note):
            self.__differenceFreq = tune.tunning(note)
            
            target = round(self.__differenceFreq * (-3) + 90)
            
            if target > 180: 
                target = 180
            if target < 0: 
                target = 0
            
            print(self.__differenceFreq, target)
            
            if self.__differenceFreq >= 0:
                animate_bar(target)
            else:
                animate_bar(target)
                    
        E2 = Button(frame, text= 'E2', command= lambda: chooseNote(Note[0]))
        E2.place(x= 400, y= 300)
        
        A2 = Button(frame, text= 'A2', command= lambda: chooseNote(Note[1]))
        A2.place(x= 600, y= 300)
        
        D3 = Button(frame, text= 'D3', command= lambda: chooseNote(Note[2]))
        D3.place(x= 800, y= 300)
        
        G3 = Button(frame, text= 'G3', command= lambda: chooseNote(Note[3]))
        G3.place(x= 1000, y= 300)
        
        B3 = Button(frame, text= 'B3', command= lambda: chooseNote(Note[4]))
        B3.place(x= 1200, y= 300)
        
        E4 = Button(frame, text= 'E4', command= lambda: chooseNote(Note[5]))
        E4.place(x= 1400, y= 300)
        
        speedometer = PhotoImage(file= 'GUI/normal_mode/speedometer.png')
        
        child_frame = Canvas(frame, width= 800, height= 800, borderwidth= 0, highlightthickness= 0)
        child_frame.place(x= 560, y= 600)
        
        child_frame.create_image(0, 0, anchor= NW, image= speedometer)
        
        def animate_bar(target):
            
            if self.__angle == target:
                return
            elif self.__angle < target:    
                self.__angle += 0.5      
                x2 = center_x + math.cos(math.radians(self.__angle)) * bar_length
                y2 = center_y - math.sin(math.radians(self.__angle)) * bar_length
                
                child_frame.coords(bar, center_x, center_y, x2, y2)
                self.__root.after(1, lambda: animate_bar(target))
            else:
                self.__angle -= 0.5 
                x2 = center_x + math.cos(math.radians(self.__angle)) * bar_length
                y2 = center_y - math.sin(math.radians(self.__angle)) * bar_length
                
                child_frame.coords(bar, center_x, center_y, x2, y2)
                self.__root.after(1, lambda: animate_bar(target))
        

        center_x = 400
        center_y = 400

        bar_length = 310

        self.__angle = 90
        
        initial_x = center_x + math.cos(math.radians(self.__angle)) * bar_length
        initial_y = center_y - math.sin(math.radians(self.__angle)) * bar_length

        bar = child_frame.create_line(center_x, center_y, initial_x, initial_y, width=10, fill="white")
        
        self.__root.mainloop()
        
run = GUI()
run.normal_mode()