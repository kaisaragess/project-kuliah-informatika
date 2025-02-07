#impor library
from tkinter import *

#buat variabel
bmi = 0

#Fungsi Menghitung BMI atau IMT dan dieksekusi ketika menekan tombol 'Hitung'
def calculate_bmi(): 
    
    try: #Fungsi calculate akan menjalankan block try terlebih dahulu
        name = str(ent_nama.get()) #menyimpan data nama ke variabel name
        weight = float(ent_brt.get()) #menyimpan data berat ke variabel wight
        height = float(ent_tinggi.get()) / 100  #menyimpan data tinggi ke heigt dan dikonversi dari cm ke m
        bmi = weight / (height ** 2) #menghitung bmi

        #pengondisian
        bmi_category = ""
        if bmi < 18.5:
            bmi_category = "Kurus"
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal"
        elif 25 <= bmi < 30:
            bmi_category = "Gemuk"
        else:
            bmi_category = "Obesitas"

        #meletakkan hasil ke label 'lbl_skor_bmi'
        lbl_skor_bmi.config(text=f"{name} \n {bmi:.2f}\n {bmi_category} ")
    except ValueError: #akan dieksekusi jika input yang dimasukkan tidak sesuai format 
        lbl_skor_bmi.config(text="Input Salah. Tolong Masukkan dengan Benar!")

#Fungsi untuk menghapus atau mereset semua input dan hasil
def clear_fields(): 
    ent_nama.delete(0, END)
    ent_brt.delete(0, END)
    ent_tinggi.delete(0, END)
    lbl_skor_bmi.config(text="")

#inisalisasi Tkinter
window = Tk()
window.title('Body Mass Index (BMI)') #Judul
window.configure(bg="#ECF7E5")


#Mengatur Panjang dan Lebar Window
lebar = 500
tinggi = 600

window.minsize(lebar,tinggi)
window.maxsize(lebar,tinggi)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx = int((screenwidth/2) - (lebar/2))
newy = int((screenheight/2) - (tinggi/2))

window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

#Isi Konten
frm_jdl = Frame(window, height=50,bg='#ECF7E5')
frm_data = Frame(window,height=150,bg='#ECF7E5', width=200)
frm_subjdl = Frame(window, height=50, bg='#ECF7E5')
frm_hsl = Frame(window,height=250, bg='#ECF7E5')

lbl_title1 = Label(frm_jdl, text="Yuk Cek Kondisi Badan Kamu!", font=("Helvetica",20,"bold"),bg="#D6FFB3", fg="#007243")

lbl_jdl_data = Label(frm_data, text="Isi data di bawah ini dengan benar", font=("Arial",15,"bold"), bg='#BEDEA4', fg="#FBF0DE")
lbl_nama = Label(frm_data, text="Nama :", bg='#BEDEA4', fg="#007243", font=("Arial",15, "bold"),)
ent_nama = Entry(frm_data, bg="#E1FFC7")
lbl_brt  = Label(frm_data, text="Berat (Kg) :", bg='#BEDEA4', fg="#007243",font=("Arial",15, "bold"))
ent_brt  = Entry(frm_data, bg="#E1FFC7")
lbl_tinggi = Label(frm_data, text="Tinggi (cm) :", bg='#BEDEA4', fg="#007243", font=("Arial",15, "bold"))
ent_tinggi = Entry(frm_data, bg="#E1FFC7")

btn_reset = Button(frm_data, text="Ulangi", bg="#FFFFFF")
btn_submit = Button(frm_data, text="Hitung", bg="#007243", fg="#E1FEC7")

lbl_title2 = Label(frm_subjdl, text="Hasil Kamu Saat Ini :", font=("jebtains mono", 22, "bold"), bg='#ECF7E5', fg="#007243")

lbl_skor_bmi = Label(frm_hsl, text=bmi, font=("Arial",20, "bold"), fg="#007243", bg="#ECF7E5")


#Layout
frm_jdl.pack(expand=True,fill=BOTH)
frm_data.pack()
frm_subjdl.pack(expand=True,fill=BOTH)
frm_hsl.pack(expand=True,fill=BOTH)

lbl_title1.pack(pady=20)

lbl_jdl_data.pack()
lbl_nama.pack(fill=X, pady=5)
ent_nama.pack(fill=X,pady=5)
lbl_brt.pack(fill=X, pady=5)
ent_brt.pack(fill=X,pady=5)
lbl_tinggi.pack(fill=X, pady=5)
ent_tinggi.pack(fill=X,pady=5)


btn_submit.pack(side=RIGHT, padx=2, pady=3)
btn_reset.pack(side=RIGHT, padx=2, pady=3)


lbl_title2.pack()

lbl_skor_bmi.pack()

btn_submit.config(command=calculate_bmi)
btn_reset.config(command=clear_fields)

window.mainloop()