from threading import Thread
from queue import Queue
from tkinter import PhotoImage, Canvas, Tk, NW
from math import sin, cos, radians
from new_recorder import recorder

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry('1920x1080')
        self.__root.attributes('-fullscreen', True)
        self.__root.resizable(width= False, height= False)    
        
        self.__tune = recorder()
        
        # color for background
        self.__start_color = "#fc00ff" 
        self.__end_color = "#00dbde"

    def start_normal_mode(self):
        try:
            self.__frame.destroy()
        except:
            pass
        
        thread1 = Thread(target= run.create_background_4_normal_mode())
        thread2 = Thread(target= run.normal_mode())
        
        thread1.start()
        thread2.start()
        
    def start_advance_mode(self):
        try:
            self.__frame.destroy()
        except:
            pass
    
    def create_main_frame(self):
        self.__main_frame = Canvas(self.__root, 
                            width= 1920,
                            height= 200,
                            bg= 'black',
                            borderwidth= 0,
                            highlightthickness= 0)
        self.__main_frame.pack()
        
        self.__exit_canvas = Canvas(self.__main_frame,
                             width= 70, 
                             height= 70, 
                             borderwidth= 0, 
                             highlightthickness= 0)
        self.__exit_canvas.place(x= 1850, y= 0) 
        
        extra_dirs = ['_clicked', '_moused', '']
        
        advance_dirs, normal_dirs = [], []
        
        for i in extra_dirs:
            advance_dirs.append('GUI/Advance' + i + '.png')
            normal_dirs.append('GUI/Normal' + i + '.png')
         
        advance_pics, normal_pics = [], []
        for i in range(3):  
            advance_pics.append(PhotoImage(file= advance_dirs[i]))
            normal_pics.append(PhotoImage(file= normal_dirs[i]))
        
        advance_canvas = Canvas(self.__main_frame, 
                                width= 250, 
                                height= 70,
                                borderwidth= 0,
                                highlightthickness= 0)
        advance_canvas.place(x= 1024, y= 87)
        
        normal_canvas = Canvas(self.__main_frame, 
                                width= 250, 
                                height= 70,
                                borderwidth= 0,
                                highlightthickness= 0)
        normal_canvas.place(x= 645, y= 87)
        
        for i in range(200):
            r = int(self.__start_color[1:3], 16) + (int(self.__end_color[1:3], 16) - int(self.__start_color[1:3], 16)) * i // 1080
            g = int(self.__start_color[3:5], 16) + (int(self.__end_color[3:5], 16) - int(self.__start_color[3:5], 16)) * i // 1080
            b = int(self.__start_color[5:7], 16) + (int(self.__end_color[5:7], 16) - int(self.__start_color[5:7], 16)) * i // 1080
            color = "#" + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

            if i <= 69:
                self.__main_frame.create_rectangle(0, i, 1850, i + 1, fill=color, outline="")
                self.__exit_canvas.create_rectangle(0, i, 70, i + 1, fill=color, outline="")
            elif i >= 87 and i <= 70 + 86:
                self.__main_frame.create_rectangle(0, i, 645, i + 1, fill=color, outline="")
                self.__main_frame.create_rectangle(895, i, 1024, i + 1, fill=color, outline="")
                self.__main_frame.create_rectangle(1274, i, 1920, i + 1, fill=color, outline="")
                
                advance_canvas.create_rectangle(0, i - 87, 250, i - 86, fill=color, outline="")
                normal_canvas.create_rectangle(0, i - 87, 250, i - 86, fill=color, outline="")
            else:
                self.__main_frame.create_rectangle(0, i, 1920, i + 1, fill=color, outline="") 
        
        self.__exit_pic = PhotoImage(file= 'GUI/exit.png')
        
        def exit_click(event):
            self.__tune.stop_record = True
            
            self.__root.destroy()
        
        exit_button = self.__exit_canvas.create_image(0, 
                                               0, 
                                               anchor= NW, 
                                               image= self.__exit_pic) 
        
        self.__exit_canvas.tag_bind(exit_button, '<Button-1>', exit_click) 
        
        
        advance_button = advance_canvas.create_image(125, 
                                               35, 
                                               image= advance_pics[2]) 
        advance_canvas.image = advance_pics[2]
        
        normal_button = normal_canvas.create_image(125, 
                                               35, 
                                               image= normal_pics[0])  
        normal_canvas.image = normal_pics[0]
        
        def advance_mouse(event):
            if not self.__tune.advanceMode:
                advance_canvas.itemconfig(advance_button, image= advance_pics[1])
                advance_canvas.image = advance_pics[1]
        def advance_click(event):
            if not self.__tune.advanceMode:
                advance_canvas.itemconfig(advance_button, image= advance_pics[0])
                advance_canvas.image = advance_pics[0]
                
                normal_canvas.itemconfig(normal_button, image= normal_pics[2])
                normal_canvas.image = normal_pics[2]
                
                self.__tune.advanceMode = True
                
                self.start_advance_mode()
        def advance_leave(event):
            if not self.__tune.advanceMode:
                advance_canvas.itemconfig(advance_button, image= advance_pics[2])
                advance_canvas.image = advance_pics[2]
        
        advance_canvas.tag_bind(advance_button, '<Enter>', advance_mouse) 
        advance_canvas.tag_bind(advance_button, '<Button-1>', advance_click) 
        advance_canvas.tag_bind(advance_button, '<Leave>', advance_leave)
        
        
        def normal_mouse(event):
            if self.__tune.advanceMode:
                normal_canvas.itemconfig(normal_button, image= normal_pics[1])
                normal_canvas.image = normal_pics[1]
        def normal_click(event):
            if self.__tune.advanceMode:
                normal_canvas.itemconfig(normal_button, image= normal_pics[0])
                normal_canvas.image = normal_pics[0]
                
                advance_canvas.itemconfig(advance_button, image= advance_pics[2])
                advance_canvas.image = advance_pics[2]
                
                self.__tune.advanceMode = False
                self.start_normal_mode()
        def normal_leave(event):
            if self.__tune.advanceMode:
                normal_canvas.itemconfig(normal_button, image= normal_pics[2])
                normal_canvas.image = normal_pics[2]
        
        normal_canvas.tag_bind(normal_button, '<Button-1>', normal_click) 
        normal_canvas.tag_bind(normal_button, '<Enter>', normal_mouse) 
        normal_canvas.tag_bind(normal_button, '<Leave>', normal_leave)
               
        
    
    def animate_bar_thread(self, target):
        Thread(target= lambda: self.animate_bar(target)).start()
        Thread(target= lambda: self.animate_bar(target)).start()
        Thread(target= lambda: self.animate_bar(target)).start()
        Thread(target= lambda: self.animate_bar(target)).start()

    def animate_bar(self, target):
            if self.__angle != target:    
                x2 = self.__center_x + cos(radians(self.__angle)) * self.__bar_length
                y2 = self.__center_y - sin(radians(self.__angle)) * self.__bar_length
                
                self.__speedometor_frame.coords(self.__bar, self.__center_x, self.__center_y, x2, y2)
                if self.__angle < target:
                    self.__angle += 1
                    self.__root.after(1, lambda: self.animate_bar(target))
                if self.__angle > target:
                    self.__angle -= 1
                    self.__root.after(1, lambda: self.animate_bar(target))
            return
     
    def create_background_4_normal_mode(self):
        self.__root.title('Normal mode')
        
        self.__isClicked = False
        
        dirs = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']
        moused_dirs = []
        for i in dirs:
            moused_dirs.append('GUI/normal_mode/' + i + '_moused.png')
        clicked_dirs = []
        for i in dirs:
            clicked_dirs.append('GUI/normal_mode/' + i + '_clicked.png')
        
        self.__pic_moused = (PhotoImage(file= moused_dirs[0]),
                             PhotoImage(file= moused_dirs[1]),
                             PhotoImage(file= moused_dirs[2]),
                             PhotoImage(file= moused_dirs[3]),
                             PhotoImage(file= moused_dirs[4]),
                             PhotoImage(file= moused_dirs[5]))
                
        self.__pic_clicked = (PhotoImage(file= clicked_dirs[0]),
                              PhotoImage(file= clicked_dirs[1]),
                              PhotoImage(file= clicked_dirs[2]),
                              PhotoImage(file= clicked_dirs[3]),
                              PhotoImage(file= clicked_dirs[4]),
                              PhotoImage(file= clicked_dirs[5]))
        
        self.__frame = Canvas(self.__root, 
                       width= 1920, 
                       height= 880, 
                       bg= 'black', 
                       borderwidth= 0, 
                       highlightthickness= 0)
        self.__frame.pack() 
        
        self.__speedometer = PhotoImage(file= 'GUI/normal_mode/speedometer.png')
        
        self.__speedometor_frame = Canvas(self.__frame, 
                                   width= 1470, 
                                   height= 1470, 
                                   borderwidth= 0, 
                                   highlightthickness= 0,
                                   bg = 'white')
        self.__speedometor_frame.place(x= 225, y= 140)
                
        for i in range(200, 1080):
            r = int(self.__start_color[1:3], 16) + (int(self.__end_color[1:3], 16) - int(self.__start_color[1:3], 16)) * i // 1080
            g = int(self.__start_color[3:5], 16) + (int(self.__end_color[3:5], 16) - int(self.__start_color[3:5], 16)) * i // 1080
            b = int(self.__start_color[5:7], 16) + (int(self.__end_color[5:7], 16) - int(self.__start_color[5:7], 16)) * i // 1080
            color = "#" + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

            if i >= 340:
                self.__frame.create_rectangle(0, i - 200, 225, i - 199, fill=color, outline="")
                self.__frame.create_rectangle(225 + 1470, i - 200, 1920, i - 199, fill=color, outline="")
                self.__speedometor_frame.create_rectangle(0, i - 340, 1470, i - 339, fill=color, outline="")
            else:
                self.__frame.create_rectangle(0, i - 200, 1920, i - 199, fill=color, outline="")    
                
        self.__speedometer_pic = self.__speedometor_frame.create_image(0, 
                                                         0, 
                                                         anchor= NW, 
                                                         image= self.__speedometer)
     
     
    def normal_mode(self):        
                                
        Note = [82.41, 110, 146.83, 196, 246.94, 329.63]
        
        shared_queue = Queue()
        
        def chooseNote(note):
            def animatee():
                target = round(self.__tune.difference * (-2) + 90)  
                                         
                shared_queue.put(target)
                
                target = shared_queue.get(timeout=1)  # Wait for a target value for up to 1 second
                if target <= 290 and target >= 0 and self.__angle != target:
                    if target > 180:
                        target = 180
                    
                    print(self.__tune.freq, target)
                    
                    self.animate_bar_thread(target)
                
                if not self.__tune.stop_record:
                    self.__root.after(200, animatee)
                else:
                    self.animate_bar_thread(90)

                    
            
            def run_record():                    
                self.__tune.record(note)
                            
            thread1 = Thread(target=run_record)
            thread2 = Thread(target=animatee)
            
            thread1.start()
            thread2.start()
           
            
                       
        def E2_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_moused[0])
                self.__speedometor_frame.image = self.__pic_moused[0]

        def A2_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_moused[1])
                self.__speedometor_frame.image = self.__pic_moused[1]

        def D3_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_moused[2])
                self.__speedometor_frame.image = self.__pic_moused[2]

        def G3_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_moused[3])
                self.__speedometor_frame.image = self.__pic_moused[3]

        def B3_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_moused[4])
                self.__speedometor_frame.image = self.__pic_moused[4]

        def E4_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_moused[5])
                self.__speedometor_frame.image = self.__pic_moused[5]
        
        def Leave(event):
            if not self.__isClicked:
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__speedometer)
                self.__speedometor_frame.image = self.__speedometer
         
                    
        def E2_click(event):
            if not self.__isClicked:
                self.__tune.stop_record = False
                self.__isClicked = True
                chooseNote(Note[0])
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_clicked[0])
                self.__speedometor_frame.image = self.__pic_clicked[0]

        def A2_click(event):
            if not self.__isClicked:
                self.__tune.stop_record = False
                self.__isClicked = True
                chooseNote(Note[1])
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_clicked[1])
                self.__speedometor_frame.image = self.__pic_clicked[1]

        def D3_click(event):
            if not self.__isClicked:
                self.__tune.stop_record = False
                self.__isClicked = True
                chooseNote(Note[2])
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_clicked[2])
                self.__speedometor_frame.image = self.__pic_clicked[2]

        def G3_click(event):
            if not self.__isClicked:
                self.__tune.stop_record = False
                self.__isClicked = True
                chooseNote(Note[3])
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_clicked[3])
                self.__speedometor_frame.image = self.__pic_clicked[3]

        def B3_click(event):
            if not self.__isClicked:
                self.__tune.stop_record = False
                self.__isClicked = True
                chooseNote(Note[4])
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_clicked[4])
                self.__speedometor_frame.image = self.__pic_clicked[4]

        def E4_click(event):
            if not self.__isClicked:
                self.__tune.stop_record = False
                self.__isClicked = True
                chooseNote(Note[5])
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__pic_clicked[5])
                self.__speedometor_frame.image = self.__pic_clicked[5]
        
        def Unclick(event):
            if self.__isClicked:
                self.__tune.stop_record = True
                self.__isClicked = False
                self.__speedometor_frame.itemconfig(self.__speedometer_pic, image= self.__speedometer)
                self.__speedometor_frame.image = self.__speedometer
        
        rect1 = self.__speedometor_frame.create_rectangle(73, 478, 73+204, 478+240, fill= '', outline= '')
        rect2 = self.__speedometor_frame.create_rectangle(212, 257, 212+242, 257+167, fill= '', outline= '')
        rect3 = self.__speedometor_frame.create_rectangle(468, 84, 468+266, 84+181, fill= '', outline= '')
        rect4 = self.__speedometor_frame.create_rectangle(740, 84, 740+266, 84+181, fill= '', outline= '')
        rect5 = self.__speedometor_frame.create_rectangle(1023, 257, 1023+242, 257+167, fill= '', outline= '')
        rect6 = self.__speedometor_frame.create_rectangle(1181, 478, 1181+204, 478+240, fill= '', outline= '')
        
        # Bind the mouse events to the rectangles
        self.__speedometor_frame.tag_bind(rect1, '<Enter>', E2_enter)
        self.__speedometor_frame.tag_bind(rect2, '<Enter>', A2_enter)
        self.__speedometor_frame.tag_bind(rect3, '<Enter>', D3_enter)
        self.__speedometor_frame.tag_bind(rect4, '<Enter>', G3_enter)
        self.__speedometor_frame.tag_bind(rect5, '<Enter>', B3_enter)
        self.__speedometor_frame.tag_bind(rect6, '<Enter>', E4_enter)
        
        self.__speedometor_frame.tag_bind(rect1, '<Leave>', Leave)
        self.__speedometor_frame.tag_bind(rect2, '<Leave>', Leave)
        self.__speedometor_frame.tag_bind(rect3, '<Leave>', Leave)
        self.__speedometor_frame.tag_bind(rect4, '<Leave>', Leave)
        self.__speedometor_frame.tag_bind(rect5, '<Leave>', Leave)
        self.__speedometor_frame.tag_bind(rect6, '<Leave>', Leave)
                
        self.__speedometor_frame.tag_bind(rect1, '<Button-3>', Unclick)
        self.__speedometor_frame.tag_bind(rect2, '<Button-3>', Unclick)
        self.__speedometor_frame.tag_bind(rect3, '<Button-3>', Unclick)
        self.__speedometor_frame.tag_bind(rect4, '<Button-3>', Unclick)
        self.__speedometor_frame.tag_bind(rect5, '<Button-3>', Unclick)
        self.__speedometor_frame.tag_bind(rect6, '<Button-3>', Unclick)
        
        self.__speedometor_frame.tag_bind(rect1, '<Button-1>', E2_click)
        self.__speedometor_frame.tag_bind(rect2, '<Button-1>', A2_click)
        self.__speedometor_frame.tag_bind(rect3, '<Button-1>', D3_click)
        self.__speedometor_frame.tag_bind(rect4, '<Button-1>', G3_click)
        self.__speedometor_frame.tag_bind(rect5, '<Button-1>', B3_click)
        self.__speedometor_frame.tag_bind(rect6, '<Button-1>', E4_click)

        self.__center_x = 735
        self.__center_y = 735

        self.__bar_length = 300

        self.__angle = 90
        
        initial_x = self.__center_x + cos(radians(self.__angle)) * self.__bar_length
        initial_y = self.__center_y - sin(radians(self.__angle)) * self.__bar_length

        self.__bar = self.__speedometor_frame.create_line(self.__center_x, 
                                            self.__center_y, 
                                            initial_x, 
                                            initial_y, 
                                            width=10, 
                                            fill="white")
        
        self.__root.mainloop()
        
        def create_background_4_advance_mode(self):
            pass
        
run = GUI()
thread1 = Thread(target= run.create_main_frame())
thread1.start()

run.start_normal_mode()
