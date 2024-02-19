# PROGRAM : Kalkulator Sederhana
# NIM     : 2103840
# NAMA    : Syifa Fatmawati

# GUI Python
import customtkinter
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("Kalkulator Sederhana (Syifa Fatmawati)")
root.geometry("500x350")

# INPUT x
label1 = customtkinter.CTkLabel(master=root, text='x = ', font=("montserrat",12))       
label1.place(x=170, y=50)
entry1 = customtkinter.CTkEntry(root)                          
entry1.place(x=200, y=50)

# INPUT y
label2 = customtkinter.CTkLabel(master=root, text='y = ', font=("montserrat",12))
label2.place(x=170, y=100)   
entry2 = customtkinter.CTkEntry(root)
entry2.place(x=200, y=100)

# HASIL
label3 = customtkinter.CTkLabel(master=root, text='Hasil = ', font=("montserrat",12))
label3.place(x=150, y=150)   

# variabel global untuk label4(HASIL)
label4 = None

# HAPUS label4(HASIL) SEBELUMNYA
def hapus():
    if label4:
        label4.destroy()

# OPERASI PERHITUNGAN
def tambah():
    hapus()
    x = entry1.get()
    y = entry2.get()
    global label4
    label4 = customtkinter.CTkLabel(master=root, text=str(int(x)+int(y)))
    label4.place(x=200, y=150)
def kurang():
    hapus()
    x = entry1.get()
    y = entry2.get()
    global label4
    label4 = customtkinter.CTkLabel(master=root, text=str(int(x)-int(y)))
    label4.place(x=200, y=150)
def kali():
    hapus()
    x = entry1.get()
    y = entry2.get()
    global label4
    label4 = customtkinter.CTkLabel(master=root, text=str(int(x)*int(y)))
    label4.place(x=200, y=150)
def bagi():
    hapus()
    x = entry1.get()
    y = entry2.get()
    global label4
    label4 = customtkinter.CTkLabel(master=root, text=str(int(x)/int(y)))
    label4.place(x=200, y=150)


# PROGRAM UTAMA
button1 = customtkinter.CTkButton(master=root, width=50, height=50, text='+', font=("montserrat",20), command=tambah)  
button1.place(x=110, y=210)
button2 = customtkinter.CTkButton(master=root, width=50, height=50, text='-', font=("montserrat",20), command=kurang)  
button2.place(x=190, y=210)
button3 = customtkinter.CTkButton(master=root, width=50, height=50, text='×', font=("montserrat",20), command=kali)  
button3.place(x=270, y=210)
button4 = customtkinter.CTkButton(master=root, width=50, height=50, text='÷', font=("montserrat",20), command=bagi)  
button4.place(x=350, y=210)

root.mainloop()  

                              




