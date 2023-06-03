from tkinter import *
import math
from Note_detection import note_detection

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry('1920x1080')
        self.__root.attributes('-fullscreen', True)
        self.__root.resizable(width= False, height= False)    
        
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
      
        
    def normal_mode(self):       
        self.__root.title('Normal mode')
        
        frame = Canvas(self.__root, 
                       width= 1920, 
                       height= 1080, 
                       bg= 'black', 
                       borderwidth= 0, 
                       highlightthickness= 0)
        frame.pack() 
                
        exit_pic = PhotoImage(file= 'GUI/exit.png')
        
        exit_canvas = Canvas(frame,
                             width= 70, 
                             height= 70, 
                             borderwidth= 0, 
                             highlightthickness= 0)
        exit_canvas.place(x= 1850, y= 0) 
                                
        Note = [82.41, 110, 146.83, 196, 246.94, 329.63]
        
        tune = note_detection()
        
        def chooseNote(note):
            self.__differenceFreq = tune.tunning(note)
            
            target = round(self.__differenceFreq * (-3) + 90)
            
            if target > 180: 
                target = 180
            if target < 0: 
                target = 0
            
            # print(self.__differenceFreq, target)
            
            if self.__differenceFreq >= 0:
                animate_bar(target)
            else:
                animate_bar(target)
                     
        speedometer = PhotoImage(file= 'GUI/normal_mode/speedometer.png')
        
        speedometer_frame = Canvas(frame, 
                                   width= 1470, 
                                   height= 1470, 
                                   borderwidth= 0, 
                                   highlightthickness= 0,
                                   bg = 'white')
        speedometer_frame.place(x= 225, y= 340)
        
        start_color = "#12c2e9" 
        end_color = "#c471ed"
        
        for i in range(1080):
            r = int(start_color[1:3], 16) + (int(end_color[1:3], 16) - int(start_color[1:3], 16)) * i // 1080
            g = int(start_color[3:5], 16) + (int(end_color[3:5], 16) - int(start_color[3:5], 16)) * i // 1080
            b = int(start_color[5:7], 16) + (int(end_color[5:7], 16) - int(start_color[5:7], 16)) * i // 1080
            color = "#" + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

            if i < 70:
                frame.create_rectangle(0, i, 1850, i + 1, fill=color, outline="")
                exit_canvas.create_rectangle(0, i, 70, i + 1, fill=color, outline="")
            elif i >= 340:
                frame.create_rectangle(0, i, 225, i + 1, fill=color, outline="")
                frame.create_rectangle(225 + 1470, i, 1920, i + 1, fill=color, outline="")
                speedometer_frame.create_rectangle(0, i - 340, 1470, i - 339, fill=color, outline="")
            else:
                frame.create_rectangle(0, i, 1920, i + 1, fill=color, outline="")    
        
        def exit_click(event):
            self.__root.destroy()
        
        exit_button = exit_canvas.create_image(0, 
                                               0, 
                                               anchor= NW, 
                                               image= exit_pic) 
        
        exit_canvas.tag_bind(exit_button, '<Button-1>', exit_click)  
        
        speedometer_pic = speedometer_frame.create_image(0, 
                                                         0, 
                                                         anchor= NW, 
                                                         image= speedometer)
                
        def E2_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[0])
                speedometer_frame.image = self.__pic_moused[0]

        def A2_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[1])
                speedometer_frame.image = self.__pic_moused[1]

        def D3_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[2])
                speedometer_frame.image = self.__pic_moused[2]

        def G3_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[3])
                speedometer_frame.image = self.__pic_moused[3]

        def B3_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[4])
                speedometer_frame.image = self.__pic_moused[4]

        def E4_enter(event):
            if not self.__isClicked:
                self.__isClicked = False
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[5])
                speedometer_frame.image = self.__pic_moused[5]
        
        def Leave(event):
            if not self.__isClicked:
                speedometer_frame.itemconfig(speedometer_pic, image= speedometer)
                speedometer_frame.image = speedometer
         
                    
        def E2_click(event):
            if not self.__isClicked:
                self.__isClicked = True
                chooseNote(Note[0])
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_moused[0])
                speedometer_frame.image = self.__pic_moused[0]

        def A2_click(event):
            if not self.__isClicked:
                self.__isClicked = True
                chooseNote(Note[1])
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_clicked[1])
                speedometer_frame.image = self.__pic_clicked[1]

        def D3_click(event):
            if not self.__isClicked:
                chooseNote(Note[2])
                self.__isClicked = True
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_clicked[2])
                speedometer_frame.image = self.__pic_clicked[2]

        def G3_click(event):
            if not self.__isClicked:
                chooseNote(Note[3])
                self.__isClicked = True
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_clicked[3])
                speedometer_frame.image = self.__pic_clicked[3]

        def B3_click(event):
            if not self.__isClicked:
                chooseNote(Note[4])
                self.__isClicked = True
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_clicked[4])
                speedometer_frame.image = self.__pic_clicked[4]

        def E4_click(event):
            if not self.__isClicked:
                chooseNote(Note[5])
                self.__isClicked = True
                speedometer_frame.itemconfig(speedometer_pic, image= self.__pic_clicked[5])
                speedometer_frame.image = self.__pic_clicked[5]
        
        def Unclick(event):
            if self.__isClicked:
                self.__isClicked = False
                animate_bar(90)
        
        rect1 = speedometer_frame.create_rectangle(73, 478, 73+204, 478+240, fill= '', outline= '')
        rect2 = speedometer_frame.create_rectangle(212, 257, 212+242, 257+167, fill= '', outline= '')
        rect3 = speedometer_frame.create_rectangle(468, 84, 468+266, 84+181, fill= '', outline= '')
        rect4 = speedometer_frame.create_rectangle(740, 84, 740+266, 84+181, fill= '', outline= '')
        rect5 = speedometer_frame.create_rectangle(1023, 257, 1023+242, 257+167, fill= '', outline= '')
        rect6 = speedometer_frame.create_rectangle(1181, 478, 1181+204, 478+240, fill= '', outline= '')
        
        # Bind the mouse events to the rectangles
        speedometer_frame.tag_bind(rect1, '<Enter>', E2_enter)
        speedometer_frame.tag_bind(rect2, '<Enter>', A2_enter)
        speedometer_frame.tag_bind(rect3, '<Enter>', D3_enter)
        speedometer_frame.tag_bind(rect4, '<Enter>', G3_enter)
        speedometer_frame.tag_bind(rect5, '<Enter>', B3_enter)
        speedometer_frame.tag_bind(rect6, '<Enter>', E4_enter)
        
        speedometer_frame.tag_bind(rect1, '<Leave>', Leave)
        speedometer_frame.tag_bind(rect2, '<Leave>', Leave)
        speedometer_frame.tag_bind(rect3, '<Leave>', Leave)
        speedometer_frame.tag_bind(rect4, '<Leave>', Leave)
        speedometer_frame.tag_bind(rect5, '<Leave>', Leave)
        speedometer_frame.tag_bind(rect6, '<Leave>', Leave)
                
        speedometer_frame.tag_bind(rect1, '<Button-3>', Unclick)
        speedometer_frame.tag_bind(rect2, '<Button-3>', Unclick)
        speedometer_frame.tag_bind(rect3, '<Button-3>', Unclick)
        speedometer_frame.tag_bind(rect4, '<Button-3>', Unclick)
        speedometer_frame.tag_bind(rect5, '<Button-3>', Unclick)
        speedometer_frame.tag_bind(rect6, '<Button-3>', Unclick)
        
        speedometer_frame.tag_bind(rect1, '<Button-1>', E2_click)
        speedometer_frame.tag_bind(rect2, '<Button-1>', A2_click)
        speedometer_frame.tag_bind(rect3, '<Button-1>', D3_click)
        speedometer_frame.tag_bind(rect4, '<Button-1>', G3_click)
        speedometer_frame.tag_bind(rect5, '<Button-1>', B3_click)
        speedometer_frame.tag_bind(rect6, '<Button-1>', E4_click)
    
        def animate_bar(target):
            
            if self.__angle == target:
                return
            elif self.__angle < target:    
                self.__angle += 1   
                x2 = center_x + math.cos(math.radians(self.__angle)) * bar_length
                y2 = center_y - math.sin(math.radians(self.__angle)) * bar_length
                
                speedometer_frame.coords(bar, center_x, center_y, x2, y2)
                self.__root.after(1, lambda: animate_bar(target))
            else:
                self.__angle -= 1
                x2 = center_x + math.cos(math.radians(self.__angle)) * bar_length
                y2 = center_y - math.sin(math.radians(self.__angle)) * bar_length
                
                speedometer_frame.coords(bar, center_x, center_y, x2, y2)
                self.__root.after(1, lambda: animate_bar(target))
        

        center_x = 735
        center_y = 735

        bar_length = 380

        self.__angle = 90
        
        initial_x = center_x + math.cos(math.radians(self.__angle)) * bar_length
        initial_y = center_y - math.sin(math.radians(self.__angle)) * bar_length

        bar = speedometer_frame.create_line(center_x, 
                                            center_y, 
                                            initial_x, 
                                            initial_y, 
                                            width=10, 
                                            fill="white")
        
        self.__root.mainloop()
        
run = GUI()
run.normal_mode()