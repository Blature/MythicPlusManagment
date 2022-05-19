from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


def adv_root():

    adv_root = Tk()
    adv_root.configure(bg='#f0f0f0')
    # adv_root.set_theme('classic')
    adv_root.title('Advertiser Config')
    adv_root.iconbitmap('ico/icon.ico')
    adv_root.geometry('260x570')
    adv_root.resizable(0, 0)

    style = ttk.Style()
    style.theme_use('vista')
    

    data_frame = LabelFrame(adv_root, text= 'Advertisers')
    data_frame.pack(fill='x', expand='yes', padx=20)
    data_frame.configure(bg='#f0f0f0')  

    adv_label_1 = ttk.Label(data_frame, text = 'Advertiser 1')
    adv_label_1.grid(row=0, column=0, padx=10, pady= 10)

    var_adv_enr_1 = StringVar()
    adv_etr_1 = ttk.Entry(data_frame, textvariable=var_adv_enr_1, width=15)
    adv_etr_1.grid(row=0, column=1, padx=10, pady=10)

    adv_label_2 = ttk.Label(data_frame, text = 'Advertiser 2')
    adv_label_2.grid(row=1, column=0, padx=10, pady= 10)

    var_adv_enr_2 = StringVar()
    adv_etr_2 = ttk.Entry(data_frame, textvariable=var_adv_enr_2, width=15)
    adv_etr_2.grid(row=1, column=1, padx=10, pady=10)

    adv_label_3 = ttk.Label(data_frame, text = 'Advertiser 3')
    adv_label_3.grid(row=2, column=0, padx=10, pady= 10)

    var_adv_enr_3 = StringVar()
    adv_etr_3 = ttk.Entry(data_frame, textvariable=var_adv_enr_3, width=15)
    adv_etr_3.grid(row=2, column=1, padx=10, pady=10)

    adv_label_4 = ttk.Label(data_frame, text = 'Advertiser 4')
    adv_label_4.grid(row=3, column=0, padx=10, pady= 10)

    var_adv_enr_4 = StringVar()
    adv_etr_4 = ttk.Entry(data_frame, textvariable=var_adv_enr_4, width=15)
    adv_etr_4.grid(row=3, column=1, padx=10, pady=10)

    adv_label_5 = ttk.Label(data_frame, text = 'Advertiser 5')
    adv_label_5.grid(row=4, column=0, padx=10, pady= 10)

    var_adv_enr_5 = StringVar()
    adv_etr_5 = ttk.Entry(data_frame, textvariable=var_adv_enr_5, width=15)
    adv_etr_5.grid(row=4, column=1, padx=10, pady=10)

    adv_label_6 = ttk.Label(data_frame, text = 'Advertiser 6')
    adv_label_6.grid(row=5, column=0, padx=10, pady= 10)

    var_adv_enr_6 = StringVar()
    adv_etr_6 = ttk.Entry(data_frame, textvariable=var_adv_enr_6, width=15)
    adv_etr_6.grid(row=5, column=1, padx=10, pady=10)

    adv_label_7 = ttk.Label(data_frame, text = 'Advertiser 7')
    adv_label_7.grid(row=6, column=0, padx=10, pady= 10)

    var_adv_enr_7 = StringVar()
    adv_etr_7 = ttk.Entry(data_frame, textvariable=var_adv_enr_7, width=15)
    adv_etr_7.grid(row=6, column=1, padx=10, pady=10)

    adv_label_8 = ttk.Label(data_frame, text = 'Advertiser 8')
    adv_label_8.grid(row=7, column=0, padx=10, pady= 10)

    var_adv_enr_8 = StringVar()
    adv_etr_8 = ttk.Entry(data_frame, textvariable=var_adv_enr_8, width=15)
    adv_etr_8.grid(row=7, column=1, padx=10, pady=10)

    adv_label_9 = ttk.Label(data_frame, text = 'Advertiser 9')
    adv_label_9.grid(row=8, column=0, padx=10, pady= 10)

    var_adv_enr_9 = StringVar()
    adv_etr_9 = ttk.Entry(data_frame, textvariable=var_adv_enr_9, width=15)
    adv_etr_9.grid(row=8, column=1, padx=10, pady=10)

    adv_label_10 = ttk.Label(data_frame, text = 'Advertiser 10')
    adv_label_10.grid(row=9, column=0, padx=10, pady= 10)

    var_adv_enr_10 = StringVar()
    adv_etr_10 = ttk.Entry(data_frame, textvariable=var_adv_enr_10, width=15)
    adv_etr_10.grid(row=9, column=1, padx=10, pady=10) 

    
    btn_frame = LabelFrame(adv_root, text= 'Options')
    btn_frame.pack(fill='x', expand='yes', padx=20)
    btn_frame.configure(bg='#f0f0f0')  
    #---------------------------

    def save():
        #-------------------
        conn = sqlite3.connect('M+DataBase.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists advertisers (
        adv_1 text,
        adv_2 text,
        adv_3 text,
        adv_4 text,
        adv_5 text,
        adv_6 text,
        adv_7 text,
        adv_8 text,
        adv_9 text,
        adv_10 text)''')
        import_list = ['', '', '', '', '', '', '', '', '', '']  
        c.execute('INSERT INTO advertisers (adv_1, adv_2, adv_3, adv_4, adv_5, adv_6, adv_7, adv_8, adv_9, adv_10) VALUES(?,?,?,?,?,?,?,?,?,?)' , import_list)
        update = "UPDATE advertisers SET adv_1 = ? , adv_2 = ? , adv_3 = ? , adv_4 = ? , adv_5 = ?, adv_6 = ?, adv_7 = ?, adv_8 = ?, adv_9 = ?, adv_10 = ? WHERE rowid = ?"
        if adv_etr_1.get().isspace():
            adv_etr_1.delete(0, END)
        elif adv_etr_2.get().isspace():
            adv_etr_2.delete(0, END)
        elif adv_etr_3.get().isspace():
            adv_etr_3.delete(0, END)
        elif adv_etr_4.get().isspace():
            adv_etr_4.delete(0, END)
        elif adv_etr_5.get().isspace():
            adv_etr_5.delete(0, END)
        elif adv_etr_6.get().isspace():
            adv_etr_6.delete(0, END)
        elif adv_etr_7.get().isspace():
            adv_etr_7.delete(0, END)
        elif adv_etr_8.get().isspace():
            adv_etr_8.delete(0, END)
        elif adv_etr_9.get().isspace():
            adv_etr_9.delete(0, END)
        elif adv_etr_10.get().isspace():
            adv_etr_10.delete(0, END)   
        
        data = [adv_etr_1.get(), adv_etr_2.get(), adv_etr_3.get(), adv_etr_4.get(), adv_etr_5.get(), adv_etr_6.get(), adv_etr_7.get(), adv_etr_8.get(), adv_etr_9.get(), adv_etr_10.get(), 1]  
        c.execute(update, data)
        c.execute('DELETE from advertisers WHERE rowid ='+ '2')
        conn.commit()
        
        a = messagebox.showinfo('Done', 'Your request has been successfully submitted')
        c.close()
        adv_root.destroy()

        
            
    def insert(self):
        adv_etr_1.insert(0, self[0][0])
        adv_etr_2.insert(0, self[0][1])
        adv_etr_3.insert(0, self[0][2])
        adv_etr_4.insert(0, self[0][3])
        adv_etr_5.insert(0, self[0][4])
        adv_etr_6.insert(0, self[0][5])
        adv_etr_7.insert(0, self[0][6])
        adv_etr_8.insert(0, self[0][7])
        adv_etr_9.insert(0, self[0][8])
        adv_etr_10.insert(0, self[0][9])


    def delete():
        adv_etr_1.delete(0, END)
        adv_etr_2.delete(0, END)
        adv_etr_3.delete(0, END)
        adv_etr_4.delete(0, END)
        adv_etr_5.delete(0, END)
        adv_etr_6.delete(0, END)
        adv_etr_7.delete(0, END)
        adv_etr_8.delete(0, END)
        adv_etr_9.delete(0, END)
        adv_etr_10.delete(0, END)
    #-------------------
    def get():
        conn = sqlite3.connect('M+DataBase.db')
        c = conn.cursor()
        c.execute('SELECT * FROM advertisers WHERE rowid =' + '1')
        records = c.fetchall()
        # print(records[0],records[1],records[2],records[3],records[4],records[5],records[6],records[7],records[8],records[9])
        delete()
        insert(records)
        conn.commit()
        c.close()

    #---------------------------
    adv_btn_save = ttk.Button(btn_frame, text='Save', style='TButton', width=12, command=save)
    adv_btn_save.grid(row=0, column=0, padx=10, pady=10)

    adv_btn_get = ttk.Button(btn_frame, text='Get Names', style='TButton', width=13, command=get)
    adv_btn_get.grid(row=0, column=1, padx=10, pady=10)
    
    get()
    adv_root.mainloop()

def adv_db():
    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists advertisers (
    adv_1 text,
    adv_2 text,
    adv_3 text,
    adv_4 text,
    adv_5 text,
    adv_6 text,
    adv_7 text,
    adv_8 text,
    adv_9 text,
    adv_10 text)''')
    import_list = ['', '', '', '', '', '', '', '', '', '']  
    c.execute('INSERT INTO advertisers (adv_1, adv_2, adv_3, adv_4, adv_5, adv_6, adv_7, adv_8, adv_9, adv_10) VALUES(?,?,?,?,?,?,?,?,?,?)' , import_list)
    conn.commit()
    c.execute('DELETE from advertisers WHERE rowid ='+ '2')
    conn.commit()
    c.close()
