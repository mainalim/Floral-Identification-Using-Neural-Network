from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk
import webbrowser

root = Tk()
root.geometry("700x960")
root.title("Leaves Recognition")
root.configure(bg= 'blue')


var = int(input("enter a number between 0 to 4"))

if var==4: # for rose


      # for main image
      path = "rose.jpeg"
      img = ImageTk.PhotoImage(Image.open(path)) # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
      panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
      panel.config(bg='black')
      panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

      # for details image
      path1 = "rosecl.png"
      img1 = ImageTk.PhotoImage(Image.open(path1))
      panel1 = Label(root, image=img1)
      panel1.config(bg='black')
     # panel.place(x=200, y= 900)
      panel1.pack(side="bottom", fill="both", expand="yes")

      def web(event):
       webbrowser.open_new(r"https://en.wikipedia.org/wiki/Rose")

      a = Label(root, text=" click beside link for further information ", anchor="w")
      a.config(bg='lightgreen', font=('times', 12, 'bold'))
      a.pack()
      a.place(x=40, y=925)
      link = Label(root, text="\t Hyperlink \t ", fg="blue", cursor="hand2")
      link.config(bg='black', font=(14))
      link.pack()
      link.place(x=400, y=925)
      link.bind("<Button-1>", web)




elif var==3: # for pine

     # for main image
     path = "pine.jpeg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "pinecl.jpg"
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
     a.place(x=40, y=925)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=400, y=925)
     link.bind("<Button-1>", web)

elif var==2: # for peepal

     # for main image
     path = "peepal.jpeg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "peepalcl.jpg"
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
     a.place(x=40, y=925)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=400, y=925)
     link.bind("<Button-1>", web)

elif var==1: # for  money plant

     # for main image
     path = "money.jpeg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "moneycl.jpg"
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
     a.place(x=40, y=940)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=400, y=940)
     link.bind("<Button-1>", web)

elif var==0: # for marigold

     # for main image
     path = "marigold.jpeg"
     img = ImageTk.PhotoImage(Image.open(path))  # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
     panel = Label(root, image=img)  # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
     panel.config(bg='black')
     panel.pack(side="top", fill="both", expand="yes")  # The Pack geometry manager packs widgets in rows or columns.

     # for details image
     path1 = "marigoldcl.jpg"
     img1 = ImageTk.PhotoImage(Image.open(path1))
     panel1 = Label(root, image=img1)
     panel1.config(bg='black')
     # panel.place(x=200, y= 900)
     panel1.pack(side="bottom", fill="both", expand="yes")


     def web(event):
      webbrowser.open_new(r"https://en.wikipedia.org/wiki/Tagetes")


     a = Label(root, text="click beside link for further information", anchor="w")
     a.config(bg='lightgreen', font=('times', 12, 'bold'))
     a.pack()
     a.place(x=40, y=925)
     link = Label(root, text=" Hyperlink ", fg="blue", cursor="hand2")
     link.config(bg='black', font=(14))
     link.pack()
     link.place(x=400, y=925)
     link.bind("<Button-1>", web)

root.mainloop()