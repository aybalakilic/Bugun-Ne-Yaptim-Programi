from tkinter import *
from tkinter import messagebox

arayuz= Tk()

arayuz.title("Bugün Ne Yaptım?")
arayuz.resizable(False,False)

canva = Canvas(arayuz, height=600 , width=1000)
canva.pack()

alt_frame=Frame(arayuz,bg="light green")
alt_frame.place(relx=0.01,rely=0.78,relheight=0.2,relwidth=0.98)
#relx=sayfanın verilen yuzdesinden ıtıbaren frami çizmeye başlar
#relhight=sayfaya oranla boyunu ayarlar

sol_frame =Frame(arayuz,bg ="light blue")
sol_frame.place(relx=0.01,rely=0.01, relheight=0.75, relwidth=0.48)

sag_frame =Frame(arayuz,bg ="light blue")
sag_frame.place(relx=0.51,rely=0.01, relheight=0.75, relwidth=0.48)

yapilacaklar_yazisi=Label(sol_frame,font=("Times-20",25,"bold"),bg="light blue",fg="white",text="YAPILACAKLAR")
yapilacaklar_yazisi.place(x=10,y=10)

v1 = IntVar()
cb1 = Checkbutton(sol_frame,bg="light blue",text="20 sayfa kitap okudum.", font=("Times-20",20,"italic"),variable=v1,onvalue=1,offvalue=0)
cb1.place(x=10,y=60)
# v1 değişkeni cb1 butonuna atanan bir değişkendir ve butonun durumu değiştikçe değeri değişir.
# onvalue ve offvalue cb1'in sırasıyla seçili ve seçili olmadığı zamanlardaki değerini atamak için kullanılır.

v2=IntVar()
cb2 = Checkbutton(sol_frame,bg="light blue",text="30 dk yürüyüş yaptım.", font=("Times-20",20,"italic"),variable=v2,onvalue=1,offvalue=0)
cb2.place(x=10,y=110)

v3=IntVar()
cb3 = Checkbutton(sol_frame,bg="light blue",text="İşlediğimiz konulara çalıştım.", font=("Times-20",20,"italic"),variable=v3,onvalue=1,offvalue=0)
cb3.place(x=10,y=160)

v4=IntVar()
cb4=Checkbutton(sol_frame,bg="light blue",text="Projem için araştırma yaptım.", font=("Times-20",20,"italic"),variable=v4,onvalue=1,offvalue=0)
cb4.place(x=10,y=210)

def yazdir():
    
    if v1.get()==1 and v2.get()==0 and v3.get()==0 and v4.get()==0:
        yazdirma_labeli.config(text="Kitap okudum.")
    elif v1.get()==0 and v2.get()==1 and v3.get()==0 and v4.get()==0:
        yazdirma_labeli.config(text="Yürüyüş yaptım.")
    elif v1.get()==0 and v2.get()==0 and v3.get()==1 and v4.get()==0:
        yazdirma_labeli.config(text="Konu çalıştım.")
    elif v1.get()==0 and v2.get()==0 and v3.get()==0 and v4.get()==1:
        yazdirma_labeli.config(text="Projemin üzerine çalıştım.")
    elif v1.get()==1 and v2.get()==1 and v3.get()==0 and v4.get()==0:
        yazdirma_labeli.config(text="Kitap okudum ve yürüyüş yaptım.")
    elif v1.get()==1 and v2.get()==0 and v3.get()==1 and v4.get()==0:
        yazdirma_labeli.config(text="Kitap okudum ve konu çalıştım.")
    elif v1.get()==1 and v2.get()==0 and v3.get()==0 and v4.get()==1:
        yazdirma_labeli.config(text="Kitap okudum ve projemin üzerine çalıştım.")
    elif v1.get()==0 and v2.get()==1 and v3.get()==1 and v4.get()==0:
        yazdirma_labeli.config(text="Yürüyüş yaptım ve konu çalıştım.")
    elif v1.get()==0 and v2.get()==1 and v3.get()==0 and v4.get()==1:
        yazdirma_labeli.config(text="Yürüyüş yaptım ve projemin üzerine çalıştım.")
    elif v1.get()==0 and v2.get()==0 and v3.get()==1 and v4.get()==1:
        yazdirma_labeli.config(text="Konu çalıştım ve projemin üzerine çalıştım.")
    elif v1.get()==1 and v2.get()==1 and v3.get()==1 and v4.get()==0:
        yazdirma_labeli.config(text="Kitap okudum, yürüyüş yaptım ve konu çalıştım.")
    elif v1.get()==1 and v2.get()==1 and v3.get()==0 and v4.get()==1:
        yazdirma_labeli.config(text="Kitap okudum, yürüyüş yaptım ve projemin üzerine çalıştım.")
    elif v1.get()==0 and v2.get()==1 and v3.get()==1 and v4.get()==1:
        yazdirma_labeli.config(text="Yürüyüş yaptım, konu çalıştım ve projemin üzerine çalıştım.")
    elif v1.get()==1 and v2.get()==0 and v3.get()==1 and v4.get()==1:
        yazdirma_labeli.config(text="Kitap okudum, konu çalıştım ve projemin üzerine çalıştım.")
    elif v1.get()==1 and v2.get()==1 and v3.get()==1 and v4.get()==1:
        yazdirma_labeli.config(text="Kitap okudum, yürüyüş yaptım, konu çalıştım ve projemin üzerine çalıştım.")
    else:
        mesaj1="Lütfen listeden en az 1 tane görev seçin!"
        messagebox.showinfo("Bilgi",mesaj1)

yazdir_butonu =Button(sol_frame,text="Yazdır", font=("Times-20",20,"bold"),bg="blue",fg="white",command=yazdir)
yazdir_butonu.place(x=170,y=380)

yazdirma_labeli = Label(alt_frame,text="...",font =("Times-20",17,"italic"),bg="light green",fg="black")
yazdirma_labeli.place(x=200,y=15)

yemekler_yazisi =Label(sag_frame, font=("Times-20",25,"bold"),bg="light blue",fg="white",text="YAZILIM")
yemekler_yazisi.place(x=30 ,y= 10)

def iki_secenek():

    try:
        
        if radio.get()==0 and radioYeni.get()==3:
            sag_yazdirma_labeli.config(text="Python ve matematik çalıştım.")
            label_texti=yazdirma_labeli.cget("text")
        elif radio.get()==0 and radioYeni.get()==4: 
            sag_yazdirma_labeli.config(text="Python ve fizik çalıştım.") 
        elif radio.get()==0 and radioYeni.get()==5:   
            sag_yazdirma_labeli.config(text="Python ve ingilizce çalıştım.") 
        elif radio.get()==1 and radioYeni.get()==3:  
            sag_yazdirma_labeli.config(text="C# ve matematik çalıştım.") 
        elif radio.get()==1 and radioYeni.get()==4:       
            sag_yazdirma_labeli.config(text="C# ve fizik çalıştım.")
        elif radio.get()==1 and radioYeni.get()==5:           
            sag_yazdirma_labeli.config(text="C# ve ingilizce çalıştım.") 
        elif radio.get()==2 and radioYeni.get()==3:           
            sag_yazdirma_labeli.config(text="HTML5 ve matematik çalıştım.") 
        elif radio.get()==2 and radioYeni.get()==4:           
            sag_yazdirma_labeli.config(text="HTML5 ve fizik çalıştım.")
        elif radio.get()==2 and radioYeni.get()==5:           
            sag_yazdirma_labeli.config(text="HTML5 ve ingilizce çalıştım.")
        elif radioYeni.get() == 0:
            message = "Lütfen bir dersi seçiniz."
            messagebox.showerror("Hatalı işlem!",message)

     
    except:
        
        message = "Başarısız."
        messagebox.showerror("Hatalı işlem!",message)
        
radio = IntVar()

r1 = Radiobutton(sag_frame,text="Python", bg="light blue",font=("Times-20",20,"italic"),fg="black", variable=radio,value=0)
r1.place(x=20,y=50)

r2 =Radiobutton(sag_frame,text="C#",font=("Times-20",20,"italic"), bg="light blue",fg="black",variable=radio,value=1)
r2.place(x=20 , y=100)

r3 =Radiobutton(sag_frame,text="HTML5",font=("Times-20",20,"italic"), bg="light blue",fg="black",variable=radio,value=2)
r3.place(x=20 , y=150)


dersler_yazisi=Label(sag_frame,font=("Times-20",25,"bold"),bg="light blue",fg="white",text="DERSLER")
dersler_yazisi.place(x=20,y=200)


radioYeni=IntVar()

r4 = Radiobutton(sag_frame,text="Matematik",font=("Times-20",20,"italic"), bg="light blue",fg="black", variable=radioYeni,value=3)
r4.place(x=20,y=240)

r5 =Radiobutton(sag_frame,text="Fizik",font=("Times-20",20,"italic"), bg="light blue",fg="black",variable=radioYeni,value=4)
r5.place(x=20 , y=280)

r6 =Radiobutton(sag_frame,text="İngilizce",font=("Times-20",20,"italic"), bg="light blue",fg="black",variable=radioYeni,value=5)
r6.place(x=20 , y=320)


sag_yazdirma_labeli = Label(alt_frame,text="...",font =("Times-20",17,"italic"),bg="light green",fg="black")
sag_yazdirma_labeli.place(x=200,y=60)

sag_buton=Button(sag_frame,text="Yazdır",font=("Times-20",20,"bold"),bg="blue",fg="white",command=iki_secenek)
sag_buton.place(x=190,y=380)

bugun_ne_yaptim_yazisi=Label(alt_frame,text="Bugün Ne\n Yaptım?",font=("Times-20",20,"bold"),fg="black",bg="light green")
bugun_ne_yaptim_yazisi.place(x=10,y=30)

arayuz.mainloop()