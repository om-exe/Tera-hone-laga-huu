from tkinter import*
class Event(Frame):
    def __init__(self,master):
        Frame.__init__(self,master);
        self.grid();
        self.button_clicks=0;
        self.create_widget();
    def create_widget(self):
        self.button=Button(self,text="Total button clicks=0");
        self.button["command"]=self.update_click_count;
        self.button.grid();
    def update_click_count(self):
        self.button_clicks+=1;
        self.button["text"]="Total button clicks = "+str(self.button_clicks);
mainWindow=Tk();
mainWindow.title("Event Handler : GUI");
mainWindow.geometry("300x200")
app=Event(mainWindow);
mainWindow.mainloop();

        