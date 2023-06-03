from tkinter import *
from Note_detection import Note_detection

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.attributes('-fullscreen', True)
        self.__root.resizable(width= False, height= False)    
        
    def normal_mode(self):
        self.__root.title('Normal mode')
        self.__root.geometry('1920x1080')
        
        background = PhotoImage(file= 'background.png')
        
        frame = Canvas(self.__root, width= 1920, height= 1080)
        frame.pack()
                
        background_label = Label(frame, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        exit_button = Button(frame, text = 'Exit', command= lambda: self.__root.destroy())
        exit_button.place(x= 1850, y= 0)
        
        node = [82.41, 110, 146.83, 196, 246.94, 329.63]
        
        def chooseNode(node):
            self.__differenceFreq = Note_detection.tunning(node)
            
            target = self.__differenceFreq * 10 + 400
            
            if target > 820: 
                target = 820
            if target < 0: 
                target = 20
            
            print(self.__differenceFreq, target)
            
            if self.__differenceFreq >= 0:
                animate_bar(target)
            else:
                animate_bar(target)
                    
        E2 = Button(frame, text= 'E2', command= lambda: chooseNode(node[0]))
        E2.place(x= 400, y= 550)
        
        A2 = Button(frame, text= 'A2', command= lambda: chooseNode(node[1]))
        A2.place(x= 600, y= 550)
        
        D3 = Button(frame, text= 'D3', command= lambda: chooseNode(node[2]))
        D3.place(x= 800, y= 550)
        
        G3 = Button(frame, text= 'G3', command= lambda: chooseNode(node[3]))
        G3.place(x= 1000, y= 550)
        
        B3 = Button(frame, text= 'B3', command= lambda: chooseNode(node[4]))
        B3.place(x= 1200, y= 550)
        
        E4 = Button(frame, text= 'E4', command= lambda: chooseNode(node[5]))
        E4.place(x= 1400, y= 550)
        
        child_frame = Canvas(frame, width= 820, height= 100, bg= 'red')
        child_frame.place(x= 560, y= 650)
        
        def animate_bar(target):
            
            if child_frame.coords(bar)[2] == int(target):
                return
            if child_frame.coords(bar)[2] < target:            
                child_frame.move(bar, 1, 0)
                self.__root.after(1, lambda: animate_bar(target))
            else:
                child_frame.move(bar, -1, 0)
                self.__root.after(1, lambda: animate_bar(target))
        
        bar_width = 20
        bar_height = 100
        bar = child_frame.create_rectangle(400, 0, 400 + bar_width, bar_height, fill="green")
        
        self.__root.mainloop()
        
run = GUI()
run.normal_mode()