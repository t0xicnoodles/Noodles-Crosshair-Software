from tkinter import *
from PIL import ImageTk, Image

app = Tk()
app.attributes('-transparentcolor','red')
app.config(bg='red')
app.geometry("150x150")
app.overrideredirect(True)
app.attributes('-topmost', True)
app.resizable(False, False)

############################################
DefaultCrosshair = PhotoImage(file = "./DefaultCrosshair.png")
############################################

window_height = 2560
window_width = 1440

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

def center():
    newWindow.destroy()
    app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    AppLogo = Label(app, borderwidth=0, bg="red" ,image=DefaultCrosshair)
    AppLogo.place(anchor = CENTER, relx = .5, rely = .5)

newWindow = Toplevel(app)
newWindow.geometry("300x300")
newWindow.title("Noodle's Crosshair (v0.1)")
newWindow.resizable(False, False)
Button(newWindow, text="Enable Crosshair", command=center).place(anchor = CENTER, relx = .5, rely = .5)
Label(newWindow, text="Close The Program From \nTask Manager When Finished With It.\n(You have to close Python down)").place(anchor = CENTER, relx = .5, rely = .7)



app.mainloop()