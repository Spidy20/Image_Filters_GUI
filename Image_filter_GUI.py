from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import cv2
import numpy as np
import datetime

windo = Tk()
windo.configure(background='white')
windo.title("Image Filters")
width  = windo.winfo_screenwidth()
height = windo.winfo_screenheight()
print(width,height)
windo.geometry(f'{width}x{height}')
windo.iconbitmap('./images/app.ico')
windo.resizable(0,0)

#Size for displaying Image
w = 400;h = 280
size = (w, h)

def upload_im():
    try:
        global im,resized
        imageFrame = tk.Frame(windo)
        imageFrame.place(x=415, y=60)
        path = filedialog.askopenfilename()
        im = Image.open(path)
        resized = im.resize(size, Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        display = tk.Label(imageFrame)
        display.imgtk = tkimage
        display.configure(image=tkimage)
        display.grid()
        dn1 = tk.Label(windo, text='Original\ud83d\ude80 Image ', width=20, height=1, fg="white", bg="maroon1",
                       font=('times', 22, ' bold '))
        dn1.place(x=444, y=20)
    except:
        del im
        noti = tk.Label(windo, text = 'Please upload an Image\ud83d\ude80 File', width=33, height=1, fg="black", bg="dodgerblue2",
                            font=('times', 15, ' bold '))
        noti.place(x=844, y=370)
        windo.after(5000, destroy_widget, noti)

def cam_cap():
    try:
        global display4,imageFrame4,cp,dn4,cap
        cap = cv2.VideoCapture(0)
        imageFrame4 = tk.Frame(windo)
        imageFrame4.place(x=415, y=60)
        dn4 = tk.Label(windo, text='Camera\ud83d\ude80 Capture', width=20, height=1, fg="white", bg="black",
                       font=('times', 22, ' bold '))
        dn4.place(x=444, y=20)
        display4 = tk.Label(imageFrame4)
        display4.grid()
        cp = tk.Button(windo, text='Capture\ud83d\ude80 Image', bg="blue", fg="white", width=20,
                       height=1, font=('times', 22, 'italic bold '),command = cam_click,activebackground = 'yellow')
        cp.place(x=440, y=370)
        def show_frame():
            global  img
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            # frame = imutils.resize(frame, width=400,height=280)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            rgb = cv2.cvtColor(cv2image, cv2.COLOR_RGBA2RGB)
            img = Image.fromarray(rgb)
            img = img.resize(size, Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=img)
            display4.imgtk = imgtk
            display4.configure(image=imgtk)
            display4.after(10, show_frame)
        show_frame()
    except:
        cp.destroy()
        dn4.destroy()
        nti = tk.Label(windo, text = 'Camera\ud83d\ude80 is not Opening!!', width=33, height=1, fg="white", bg="red",
                            font=('times', 15, ' bold '))
        nti.place(x=844, y=370)
        windo.after(5000, destroy_widget, nti)

def cam_click():
    global im,resized
    display4.destroy()
    imageFrame4.destroy()
    cv2.destroyAllWindows()
    im = img.copy()
    resized = im.resize(size, Image.ANTIALIAS)
    imageFrame5 = tk.Frame(windo)
    imageFrame5.place(x=415, y=60)
    tkimage5 = ImageTk.PhotoImage(im)
    display5 = tk.Label(imageFrame5)
    display5.imgtk = tkimage5
    display5.configure(image=tkimage5)
    display5.grid()
    windo.after(2000, destroy_widget, cp)
    cam_break()

def cam_break():
    cap.release()

def gray_filter():
    try:
        global op,noti
        #Orignal Image
        op = im.convert('L')
        #Resized Image
        gray =resized.convert('L')
        resi = gray.resize(size, Image.ANTIALIAS)
        tkimage1 = ImageTk.PhotoImage(resi)
        imageFrame1 = tk.Frame(windo)
        imageFrame1.place(x=845, y=60)
        dn1 = tk.Label(windo, text='Gray\ud83d\ude80 Image ', width=20, height=1, fg="white", bg="black",font=('times', 22, ' bold '))
        dn1.place(x=874, y=20)
        display1 = tk.Label(imageFrame1)
        display1.imgtk = tkimage1
        display1.configure(image=tkimage1)
        display1.grid()
    except Exception as e :
        print(e)
        noti = tk.Label(windo, text = 'Please upload an Image\ud83d\ude80', width=33, height=1, fg="black", bg="violet red1",
                            font=('times', 15, ' bold '))
        noti.place(x=844, y=370)
        windo.after(5000, destroy_widget, noti)

def cartoon_filter():
    try:
        global op,noti
        img1 = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.medianBlur(gray1, 5)
        edges1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color1 = cv2.bilateralFilter(img1, 9, 300, 300)
        cartoon1 = cv2.bitwise_and(color1, color1, mask=edges1)
        op = Image.fromarray(cv2.cvtColor(cartoon1, cv2.COLOR_BGR2RGB)    )
        img = cv2.cvtColor(np.asarray(resized), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        pil_image = Image.fromarray(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)    )
        resi = pil_image.resize(size, Image.ANTIALIAS)
        tkimage2 = ImageTk.PhotoImage(resi)
        imageFrame2 = tk.Frame(windo)
        imageFrame2.place(x=845, y=60)
        dn2 = tk.Label(windo, text='Cartoon\ud83d\ude80 Image ', width=20, height=1, fg="black", bg="deep sky blue",
                       font=('times', 22, ' bold '))
        dn2.place(x=874, y=20)
        display2 = tk.Label(imageFrame2)
        display2.imgtk = tkimage2
        display2.configure(image=tkimage2)
        display2.grid()
    except Exception as e :
        print(e)
        noti = tk.Label(windo, text = 'Please upload an Image\ud83d\ude80', width=33, height=1, fg="black", bg="gold",
                            font=('times', 15, ' bold '))
        noti.place(x=844, y=370)
        windo.after(5000, destroy_widget, noti)

def sketch_filter():
    try:
        global op
        img = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
        output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output = cv2.GaussianBlur(output, (3, 3), 0)
        output = cv2.Laplacian(output, -1, ksize=5)
        output = 255 - output
        ret, output = cv2.threshold(output, 150, 255, cv2.THRESH_BINARY)
        op = Image.fromarray(output)
        resi = op.resize(size, Image.ANTIALIAS)
        tkimage3 = ImageTk.PhotoImage(resi)
        imageFrame3 = tk.Frame(windo)
        imageFrame3.place(x=845, y=60)
        dn3 = tk.Label(windo, text='Sketch\ud83d\ude80 Image ', width=20, height=1, fg="black", bg="gray80",
                       font=('times', 22, ' bold '))
        dn3.place(x=874, y=20)
        display3 = tk.Label(imageFrame3)
        display3.imgtk = tkimage3
        display3.configure(image=tkimage3)
        display3.grid()
    except:
        noti = tk.Label(windo, text = 'Please upload an Image\ud83d\ude80', width=33, height=1, fg="white", bg="black",
                            font=('times', 15, ' bold '))
        noti.place(x=844, y=370)
        windo.after(5000, destroy_widget, noti)

def face_eye_det_filter():
    try:
        global op,tkimage4
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        img = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 4)
            break
        else:
            notip1 = tk.Label(windo, text='Face\ud83d\ude00 not found in Image\ud83d\ude80!!', width=33, height=1,
                             fg="white", bg="midnightblue",
                             font=('times', 15, ' bold '))
            notip1.place(x=844, y=370)
            windo.after(5000, destroy_widget, notip1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        op = Image.fromarray(img)
        resi = op.resize(size, Image.ANTIALIAS)
        tkimage4 = ImageTk.PhotoImage(resi)
        imageFrame4 = tk.Frame(windo)
        imageFrame4.place(x=845, y=60)
        dn4 = tk.Label(windo, text='Face\ud83d\ude00 & Eye Image ', width=20, height=1, fg="white", bg="navy",
                           font=('times', 22, ' bold '))
        dn4.place(x=874, y=20)
        display4 = tk.Label(imageFrame4)
        display4.imgtk = tkimage4
        display4.configure(image=tkimage4)
        display4.grid()
    except Exception as e:
        notip = tk.Label(windo, text = 'Face\ud83d\ude00 not found in Image\ud83d\ude80!!', width=33, height=1, fg="white", bg="midnightblue",
                            font=('times', 15, ' bold '))
        notip.place(x=844, y=370)
        windo.after(5000, destroy_widget, notip)
        print(e)

def save_img():
    try:
        global noti,dna
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        op.save('./Captures/'+filename)
        dna = tk.Label(windo, text=filename+' Captured\ud83d\ude80', width=33, height=1, fg="black", bg="spring green",
                            font=('times', 15, ' bold '))
        dna.place(x=844, y=370)
        windo.after(5000, destroy_widget, dna)
    except Exception as e:
        print(e)
        noti = tk.Label(windo, text='Please upload an Image\ud83d\ude80', width=33, height=1, fg="black", bg="cyan2",
                        font=('times', 15, ' bold '))
        noti.place(x=844, y=370)
        windo.after(5000, destroy_widget, noti)

def leave():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        windo.destroy()
windo.protocol("WM_DELETE_WINDOW", leave)

def destroy_widget(widget):
    widget.destroy()

dn = tk.Label(windo, text='Image \ud83d\ude80 Filters', width=20, height=1, fg="white", bg="blue2",
              font=('times', 22, ' bold '))
dn.place(x=24, y=20)


my_name = tk.Label(windo, text="©Developed by Kushal Bhavsar", bg="blue", fg="white", width=58,
                   height=1, font=('times', 30, 'italic bold '))
my_name.place(x=00, y=640)

sad_img = ImageTk.PhotoImage(Image.open("./images/logo.png"))
panel4 = Label(windo, image=sad_img)
panel4.pack()
panel4.place(x=20, y=60)

up = tk.Button(windo,text = 'Upload\ud83d\ude80 Image',bg="spring green", fg="black", width=20,
                   height=1, font=('times', 22, 'italic bold '),command = upload_im, activebackground = 'yellow')
up.place(x=20, y=340)

up1 = tk.Button(windo,text = 'Camera\ud83d\ude80 Capture',bg="midnightblue", fg="white", width=20,
                   height=1, font=('times', 22, 'italic bold '),command = cam_cap, activebackground = 'yellow')
up1.place(x=20, y=410)

hat1 = PhotoImage(file = "./images/sketch.png")
hat_f = tk.Button(windo,borderwidth=0,bg = 'white', image = hat1 ,command = sketch_filter)
hat_f.place(x=50, y=480)

sk = tk.Label(windo, text="Sketch", bg="violet red1", fg="black", width=11,
                   height=1, font=('times', 16, 'italic bold '))
sk.place(x=48, y=587)

sg = PhotoImage(file = "./images/cartoon.png")
sg_f = tk.Button(windo,borderwidth=0,bg = 'white', image = sg,command = cartoon_filter )
sg_f.place(x=250, y=480)

ca = tk.Label(windo, text="Cartoon", bg="violet red1", fg="black", width=11,
                   height=1, font=('times', 16, 'italic bold '))
ca.place(x=248, y=587)

dog_p = PhotoImage(file = "./images/bw.png")
dog_f = tk.Button(windo,borderwidth=0,bg = 'white', image = dog_p ,command = gray_filter)
dog_f.place(x=450, y=480)

bw = tk.Label(windo, text="Black & White", bg="violet red1", fg="black", width=11,
                   height=1, font=('times', 16, 'italic bold '))
bw.place(x=448, y=587)

snap_p = PhotoImage(file = "./images/save.png")
snap = tk.Button(windo,borderwidth=0,bg = 'white', image = snap_p ,command = save_img)
snap.place(x=850, y=480)

fd_p = PhotoImage(file = "./images/fd.png")
fd = tk.Button(windo,borderwidth=0,bg = 'white', image = fd_p,command = face_eye_det_filter )
fd.place(x=650, y=480)

f = tk.Label(windo, text="Face Detection", bg="violet red1", fg="black", width=11,
                   height=1, font=('times', 16, 'italic bold '))
f.place(x=648, y=587)

sv = tk.Label(windo, text="Save\ud83d\ude80 Image", bg="violet red1", fg="black", width=11,
                   height=1, font=('times', 16, 'italic bold '))
sv.place(x=848, y=587)

quit_p = PhotoImage(file = "./images/quit.png")
q = tk.Button(windo, borderwidth=0,bg = 'white', image = quit_p,command = leave )
q.place(x=1050, y=480)
windo.mainloop()