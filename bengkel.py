#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Apr 08, 2021 09:09:45 PM +07  platform: Windows NT

#Saya Muhammad Rayhan Fadillah mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin. *

import sys
from tkinter import messagebox
from tkinter import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import bengkel_support
from motor import Motor

data = []

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    bengkel_support.set_Tk_var()
    top = Toplevel1 (root)
    bengkel_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    bengkel_support.set_Tk_var()
    top = Toplevel1 (w)
    bengkel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def exit():
    confirm = messagebox.askyesno("Confirm exit", "Apakah kamu ingin keluar aplikasi ?")
    if confirm == True:
        root.quit()

def clear():
    confirm = messagebox.askyesno("Confirm exit", "Apakah kamu ingin menghapus semua data ?")
    if confirm == True:
        data.clear()

#windows about me
def aboutMe():
    top = Toplevel()
    top.title("About Me")

    d_frame = LabelFrame(top, text="Biodata", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_namaAplikasi = Label(d_frame, text="Nama Aplikasi: Bengkel Motor", anchor="w").grid(row=0, column=0, sticky="w")
    d_deskripsiAplikasi = Label(d_frame, text="Deskrisi : One Stop App untuk mendata kebutuhan pelanggan saat servis motor", anchor="w").grid(row=1, column=0, sticky="w")
    d_pembuat = Label(d_frame, text="Pembuat Aplikasi",   font = 'Helvetica 11 bold', anchor="w").grid(row=3, column=0, sticky="w")
    d_nama = Label(d_frame, text="Nama : Muhammad Rayhan Fadillah", anchor="w").grid(row=4, column=0, sticky="w")
    d_nim = Label(d_frame, text="NIM : 1907998", anchor="w").grid(row=5, column=0, sticky="w")
    d_kelas = Label(d_frame, text="Kelas : Ilmu Komputer C1", anchor="w").grid(row=6, column=0, sticky="w")

#windows menampilkan data
def dataList():
    top = Toplevel()
    top.title("data")

    for index, m in enumerate(data):
        idx = Label(top, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(top, text=m.get_pemilik(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)
        type = Label(top, text=m.get_jenis_transmisi(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=2)
        type = Label(top, text=m.get_bahan_bakar(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=3)
        type = Label(top, text=listToString(m.get_layanan()), width=30, borderwidth=1, relief="solid")
        type.grid(row=index, column=4)


# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = ", " 
    
    # return string  
    return (str1.join(s))
        
#window utama
class Toplevel1:

    # set input
    def getInput(self):
            pemilik = self.Entry1.get()
            transmisi = bengkel_support.radio.get()
            bahan_bakar = self.TCombobox1.get()
            layanan = []

            if (bengkel_support.che49.get() == 1):
                layanan.append("servis")
            
            if (bengkel_support.che50.get() == 1):
                layanan.append("ganti oli")
            
            if (bengkel_support.che51.get() == 1):
                layanan.append("isi angin")

            if (pemilik != "" and transmisi != "" and bahan_bakar != "" and len(layanan) >= 1):
                data.append(Motor(pemilik, layanan, transmisi, bahan_bakar))
                messagebox.showinfo(title="Sukses", message="Data berhasil ditambah")
                self.Entry1.delete(0, 'end')
                self.TCombobox1.set('')
                bengkel_support.radio.set("Matic")
                bengkel_support.che49.set(0)
                bengkel_support.che50.set(0)
                bengkel_support.che51.set(0)
            else:
                messagebox.showerror(title="data tidak lengkap", message="semua input harus diisi")
            
    ## init komponen di window utama
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+348+119")
        top.minsize(120, 1)
        top.maxsize(1370, 1517)
        top.resizable(1,  1)
        top.title("Bengkel Motor")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.483, rely=0.089,  relheight=0.8)
        self.TSeparator1.configure(orient="vertical")

        self.btn_see = tk.Button(top)
        self.btn_see.place(relx=0.65, rely=0.356, height=24, width=127)
        self.btn_see.configure(activebackground="#ececec")
        self.btn_see.configure(activeforeground="#000000")
        self.btn_see.configure(background="#d9d9d9")
        self.btn_see.configure(disabledforeground="#a3a3a3")
        self.btn_see.configure(foreground="#000000")
        self.btn_see.configure(highlightbackground="#d9d9d9")
        self.btn_see.configure(highlightcolor="black")
        self.btn_see.configure(pady="0")
        self.btn_see.configure(text='''See All Submission''')
        self.btn_see.configure(command=dataList)

        self.btn_clear = tk.Button(top)
        self.btn_clear.place(relx=0.65, rely=0.422, height=24, width=127)
        self.btn_clear.configure(activebackground="#ececec")
        self.btn_clear.configure(activeforeground="#000000")
        self.btn_clear.configure(background="#d9d9d9")
        self.btn_clear.configure(disabledforeground="#a3a3a3")
        self.btn_clear.configure(foreground="#000000")
        self.btn_clear.configure(highlightbackground="#d9d9d9")
        self.btn_clear.configure(highlightcolor="black")
        self.btn_clear.configure(pady="0")
        self.btn_clear.configure(text='''Clear All Submissions''')
        self.btn_clear.configure(command = clear)

        self.btn_about = tk.Button(top)
        self.btn_about.place(relx=0.65, rely=0.489, height=24, width=127)
        self.btn_about.configure(activebackground="#ececec")
        self.btn_about.configure(activeforeground="#000000")
        self.btn_about.configure(background="#d9d9d9")
        self.btn_about.configure(disabledforeground="#a3a3a3")
        self.btn_about.configure(foreground="#000000")
        self.btn_about.configure(highlightbackground="#d9d9d9")
        self.btn_about.configure(highlightcolor="black")
        self.btn_about.configure(pady="0")
        self.btn_about.configure(text='''About''')
        self.btn_about.configure(command = aboutMe)

        self.btn_exit = tk.Button(top)
        self.btn_exit.place(relx=0.65, rely=0.556, height=24, width=127)
        self.btn_exit.configure(activebackground="#ececec")
        self.btn_exit.configure(activeforeground="#000000")
        self.btn_exit.configure(background="#d9d9d9")
        self.btn_exit.configure(disabledforeground="#a3a3a3")
        self.btn_exit.configure(foreground="#000000")
        self.btn_exit.configure(highlightbackground="#d9d9d9")
        self.btn_exit.configure(highlightcolor="black")
        self.btn_exit.configure(pady="0")
        self.btn_exit.configure(text='''Exit''')
        self.btn_exit.configure(command=exit)

        self.lbl_judul = tk.Label(top)
        self.lbl_judul.place(relx=0.583, rely=0.111, height=51, width=194)
        self.lbl_judul.configure(activebackground="#f9f9f9")
        self.lbl_judul.configure(activeforeground="black")
        self.lbl_judul.configure(background="#d9d9d9")
        self.lbl_judul.configure(disabledforeground="#a3a3a3")
        self.lbl_judul.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.lbl_judul.configure(foreground="#000000")
        self.lbl_judul.configure(highlightbackground="#d9d9d9")
        self.lbl_judul.configure(highlightcolor="black")
        self.lbl_judul.configure(text='''Bengkel Motor''')

        self.lbl_deskripsi_home = tk.Label(top)
        self.lbl_deskripsi_home.place(relx=0.60, rely=0.244, height=30
                , width=200)
        self.lbl_deskripsi_home.configure(activebackground="#f9f9f9")
        self.lbl_deskripsi_home.configure(activeforeground="black")
        self.lbl_deskripsi_home.configure(background="#d9d9d9")
        self.lbl_deskripsi_home.configure(disabledforeground="#a3a3a3")
        self.lbl_deskripsi_home.configure(foreground="#000000")
        self.lbl_deskripsi_home.configure(highlightbackground="#d9d9d9")
        self.lbl_deskripsi_home.configure(highlightcolor="black")
        self.lbl_deskripsi_home.configure(text='''Menyediakan berbagai pelayanan\n untuk kendaraan anda''')

        self.lbl_form = tk.LabelFrame(top)
        self.lbl_form.place(relx=0.033, rely=0.111, relheight=0.767
                , relwidth=0.417)
        self.lbl_form.configure(relief='groove')
        self.lbl_form.configure(foreground="black")
        self.lbl_form.configure(text='''Form''')
        self.lbl_form.configure(background="#d9d9d9")
        self.lbl_form.configure(highlightbackground="#d9d9d9")
        self.lbl_form.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.lbl_form)
        self.Entry1.place(relx=0.44, rely=0.087, height=20, relwidth=0.496
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(textvariable=bengkel_support.nama_pemilik)

        self.lbl_input1 = tk.Label(self.lbl_form)
        self.lbl_input1.place(relx=0.08, rely=0.087, height=21, width=74
                , bordermode='ignore')
        self.lbl_input1.configure(activebackground="#f9f9f9")
        self.lbl_input1.configure(activeforeground="black")
        self.lbl_input1.configure(background="#d9d9d9")
        self.lbl_input1.configure(disabledforeground="#a3a3a3")
        self.lbl_input1.configure(foreground="#000000")
        self.lbl_input1.configure(highlightbackground="#d9d9d9")
        self.lbl_input1.configure(highlightcolor="black")
        self.lbl_input1.configure(text='''Nama Pemilik''')

        self.lbl_input2 = tk.Label(self.lbl_form)
        self.lbl_input2.place(relx=0.08, rely=0.203, height=21, width=84
                , bordermode='ignore')
        self.lbl_input2.configure(activebackground="#f9f9f9")
        self.lbl_input2.configure(activeforeground="black")
        self.lbl_input2.configure(background="#d9d9d9")
        self.lbl_input2.configure(disabledforeground="#a3a3a3")
        self.lbl_input2.configure(foreground="#000000")
        self.lbl_input2.configure(highlightbackground="#d9d9d9")
        self.lbl_input2.configure(highlightcolor="black")
        self.lbl_input2.configure(text='''Jenis Transmisi''')

        self.Radiobutton1 = tk.Radiobutton(self.lbl_form)
        self.Radiobutton1.place(relx=0.44, rely=0.203, relheight=0.072
                , relwidth=0.232, bordermode='ignore')
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Matic''')
        self.Radiobutton1.configure(value="Matic")
        self.Radiobutton1.configure(variable=bengkel_support.radio)

        self.Radiobutton2 = tk.Radiobutton(self.lbl_form)
        self.Radiobutton2.place(relx=0.68, rely=0.203, relheight=0.072
                , relwidth=0.232, bordermode='ignore')
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Manual''')
        self.Radiobutton2.configure(value="manual")
        self.Radiobutton2.configure(variable=bengkel_support.radio)

        self.TCombobox1 = ttk.Combobox(self.lbl_form)
        self.TCombobox1.place(relx=0.44, rely=0.29, relheight=0.061
                , relwidth=0.492, bordermode='ignore')
        self.value_list = ['Pertamax','Pertalite','Premium',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(takefocus="")

        self.lbl_input3 = tk.Label(self.lbl_form)
        self.lbl_input3.place(relx=0.08, rely=0.29, height=21, width=74
                , bordermode='ignore')
        self.lbl_input3.configure(activebackground="#f9f9f9")
        self.lbl_input3.configure(activeforeground="black")
        self.lbl_input3.configure(background="#d9d9d9")
        self.lbl_input3.configure(disabledforeground="#a3a3a3")
        self.lbl_input3.configure(foreground="#000000")
        self.lbl_input3.configure(highlightbackground="#d9d9d9")
        self.lbl_input3.configure(highlightcolor="black")
        self.lbl_input3.configure(text='''Bahan Bakar''')

        self.lbl_layanan = tk.Label(self.lbl_form)
        self.lbl_layanan.place(relx=0.04, rely=0.406, height=21, width=84
                , bordermode='ignore')
        self.lbl_layanan.configure(background="#d9d9d9")
        self.lbl_layanan.configure(disabledforeground="#a3a3a3")
        self.lbl_layanan.configure(foreground="#000000")
        self.lbl_layanan.configure(text='''Pilih Layanan''')

        self.Checkbutton2 = tk.Checkbutton(self.lbl_form)
        self.Checkbutton2.place(relx=0.08, rely=0.493, relheight=0.072
                , relwidth=0.244, bordermode='ignore')
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Servis''')
        self.Checkbutton2.configure(variable=bengkel_support.che49)

        self.Checkbutton3 = tk.Checkbutton(self.lbl_form)
        self.Checkbutton3.place(relx=0.32, rely=0.493, relheight=0.072
                , relwidth=0.284, bordermode='ignore')
        self.Checkbutton3.configure(activebackground="#ececec")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify='left')
        self.Checkbutton3.configure(text='''Ganti Oli''')
        self.Checkbutton3.configure(variable=bengkel_support.che50)

        self.Checkbutton4 = tk.Checkbutton(self.lbl_form)
        self.Checkbutton4.place(relx=0.64, rely=0.493, relheight=0.072
                , relwidth=0.284, bordermode='ignore')
        self.Checkbutton4.configure(activebackground="#ececec")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify='left')
        self.Checkbutton4.configure(text='''Isi Angin''')
        self.Checkbutton4.configure(variable=bengkel_support.che51)

        self.btn_submit = tk.Button(self.lbl_form)
        self.btn_submit.place(relx=0.28, rely=0.667, height=24, width=87
                , bordermode='ignore')
        self.btn_submit.configure(activebackground="#ececec")
        self.btn_submit.configure(activeforeground="#000000")
        self.btn_submit.configure(background="#d9d9d9")
        self.btn_submit.configure(disabledforeground="#a3a3a3")
        self.btn_submit.configure(foreground="#000000")
        self.btn_submit.configure(highlightbackground="#d9d9d9")
        self.btn_submit.configure(highlightcolor="black")
        self.btn_submit.configure(pady="0")
        self.btn_submit.configure(text='''Submit''')
        self.btn_submit.configure(command=self.getInput)
    
    

if __name__ == '__main__':
    vp_start_gui()





