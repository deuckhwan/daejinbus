import tkinter
import tkinter.font

window = tkinter.Tk()
window.geometry("400x400")

window.title("로또 번호 만들기")
label = tkinter.Label(window, text="로또 번호 만들기", font=20)
label.pack()

window.mainloop()