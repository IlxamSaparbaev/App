import webbrowser
from tkinter import PhotoImage
from tkinter import ttk
import tkinter
window = tkinter.Tk()
window.geometry('640x480')
window.resizable(False, False)
window.title('Search')

#icon = tkinter.PhotoImage(file='.idea/search.png')
#window.iconphoto(False, icon)

photo = tkinter.PhotoImage(file='./.idea/ba.png')
photo = tkinter.Label(image=photo)
photo.place(x=0, y=0)

#поиск
search_label = ttk.Label(window, text='Поиск')
search_label.place(x=5, y=41)
search_label['font'] = ('Impact 15')

#Поле для ввода
text_field = ttk.Entry(window)
text_field.place(x=66, y=40, width=510, )
text_field['font'] = ('Impact 15')
text_field.focus()

def search():
    webbrowser.open('https://' + text_field.get())


btn_search = tkinter.Button(window, text='Найти', command=search)
btn_search.place(x=580, y=40)
btn_search['font'] = ('Impact 10')

if __name__ == '__main__':
    window.wm_attributes('-topmost', True)
    window.mainloop()