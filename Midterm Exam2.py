from tkinter import *
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")
btn = Button(window, text="Click to Change color", bg="White", activebackground="Yellow")
btn.place(relx=.5, y=200, anchor="center")

window.mainloop()
