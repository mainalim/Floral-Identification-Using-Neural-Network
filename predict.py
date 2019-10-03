import os
from Tkinter import *
from Tkinter import Tk
from PIL import Image,ImageTk
import webbrowser

from tensorflow.contrib import predictor
from preprocessing import load_data

predict_fn = predictor.from_saved_model('./model_saved/1532943539')
ROOT_PATH = "." #Denotes the current working directory
PREDICT_DATA_DIRECTORY = os.path.join(ROOT_PATH, "/home/srijana/Downloads/latest/flower_photos/predict")

predict_data, predict_label = load_data(PREDICT_DATA_DIRECTORY)
#print(predict_label)
predictions = predict_fn(
    {'x': predict_data}
)
a=(predictions['classes'])
b= a[0]

root = Tk()
root.geometry("450x700")
root.title("Leaves Recognition")
root.configure(bg= 'blue')

var = b
if var==5: # for rose
      # for main image
      path = "/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg"
      img = ImageTk.PhotoImage(Image.open(path)) # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
      panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
      panel.config(bg='black')
      panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

      # for details image
      path1 = "rosea.jpg"
      img1 = ImageTk.PhotoImage(Image.open(path1))
      panel1 = Label(root, image=img1)
      panel1.config(bg='black')
      #panel1.place(x=200, y= 900)
      panel1.pack(side="bottom", fill="both", expand="yes")

      def web(event):
       webbrowser.open_new(r"https://en.wikipedia.org/wiki/Rose")

      a = Label(root, text=" click beside link for further information ", anchor="w")
      a.config(bg='lightgreen', font=('times', 12, 'italic'))
      a.pack()
      a.place(x=40, y=645)
      link = Label(root, text="\t Hyperlink \t ", fg="blue", cursor="hand2")
      link.config(bg='black', font=(14))
      link.pack()
      link.place(x=100, y=670)
      link.bind("<Button-1>", web)

elif var == 4:  # for pine

      # for main image
      path = "/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg"
      img = ImageTk.PhotoImage(Image.open(
          path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
      panel = Label(root,
                    image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
      panel.config(bg='black')
      panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

      # for details image
      path1 = "pinea.jpg"
      img1 = ImageTk.PhotoImage(Image.open(path1))
      panel1 = Label(root, image=img1)
      panel1.config(bg='black')
      # panel.place(x=200, y= 900)
      panel1.pack(side="bottom", fill="both", expand="yes")


      def web(event):
          webbrowser.open_new(r"https://en.wikipedia.org/wiki/Pine")


      a = Label(root, text="click beside link for further information", anchor="w")
      a.config(bg='lightgreen', font=('times', 12, 'bold'))
      a.pack()
      a.place(x=40, y=650)
      link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
      link.config(bg='black', font=(14))
      link.pack()
      link.place(x=150, y=675)
      link.bind("<Button-1>", web)




elif var==0: # for mango

     # for main image
     path = "/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "mangoa.jpg"
     img1 = ImageTk.PhotoImage(Image.open(path1))
     panel1 = Label(root, image=img1)
     panel1.config(bg='black')
     # panel.place(x=200, y= 900)
     panel1.pack(side="bottom", fill="both", expand="yes")

     def web(event):
      webbrowser.open_new(r"https://en.wikipedia.org/wiki/Mango")


     a = Label(root, text="click beside link for further information", anchor="w")
     a.config(bg='lightgreen', font=('times', 12, 'bold'))
     a.pack()
     a.place(x=53, y=645)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=150, y=670)
     link.bind("<Button-1>", web)

elif var==3: # for peepal

     # for main image
     path = "/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "peepala.jpg"
     img1 = ImageTk.PhotoImage(Image.open(path1))
     panel1 = Label(root, image=img1)
     panel1.config(bg='black')
     # panel.place(x=200, y= 900)
     panel1.pack(side="bottom", fill="both", expand="yes")


     def web(event):
      webbrowser.open_new(r"https://en.wikipedia.org/wiki/Ficus_religiosa")


     a = Label(root, text="click beside link for further information", anchor="w")
     a.config(bg='lightgreen', font=('times', 12, 'bold'))
     a.pack()
     a.place(x=40, y=665)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=150, y=682)
     link.bind("<Button-1>", web)

elif var==2: # for  money plant

     # for main image
     path = "/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "moneyaa.jpg"
     img1 = ImageTk.PhotoImage(Image.open(path1))
     panel1 = Label(root, image=img1)
     panel1.config(bg='black')
     # panel.place(x=200, y= 900)
     panel1.pack(side="bottom", fill="both", expand="yes")


     def web(event):
      webbrowser.open_new(r"https://en.wikipedia.org/wiki/Epipremnum_aureum")


     a = Label(root, text="click beside link for further information", anchor="w")
     a.config(bg='lightgreen', font=('times', 12, 'bold'))
     a.pack()
     a.place(x=40, y=640)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=150, y=655)
     link.bind("<Button-1>", web)

elif var==1: # for marigold

     # for main image
     path = "/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "marigoldaa.jpg"
     img1 = ImageTk.PhotoImage(Image.open(path1))
     panel1 = Label(root, image=img1)
     panel1.config(bg='black')
     #panel1.place(x=0, y= 0)
     panel1.pack(side="bottom", fill="both", expand="no")


     def web(event):
      webbrowser.open_new(r"https://en.wikipedia.org/wiki/Tagetes")


     a = Label(root, text="click beside link for further information", anchor="w")
     a.config(bg='white', font=('times', 12, 'bold'))
     a.pack()
     a.place(x=40, y=645)
     link = Label(root, text=" Hyperlink ", fg="white", cursor="hand2")
     link.config(bg='blue', font=(14))
     link.pack()
     link.place(x=150, y=670)
     link.bind("<Button-1>", web)



root.mainloop()
