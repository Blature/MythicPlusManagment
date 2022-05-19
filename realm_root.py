from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

def realm_root():

    realm_root = Tk()
    realm_root.configure(bg='#f0f0f0')
    # realm_root.set_theme('classic')
    realm_root.title('Realm Config')
    realm_root.iconbitmap('ico/icon.ico')
    realm_root.geometry('260x570')
    realm_root.resizable(0, 0)

    style = ttk.Style()
    style.theme_use('vista')
    

    data_frame = LabelFrame(realm_root, text= 'Realms')
    data_frame.pack(fill='x', expand='yes', padx=20)
    data_frame.configure(bg='#f0f0f0')  

    realm_label_1 = ttk.Label(data_frame, text = 'Realm 1')
    realm_label_1.grid(row=0, column=0, padx=10, pady= 10)

    var_realm_enr_1 = StringVar()
    realm_etr_1 = ttk.Entry(data_frame, textvariable=var_realm_enr_1, width=15)
    realm_etr_1.grid(row=0, column=1, padx=10, pady=10)

    realm_label_2 = ttk.Label(data_frame, text = 'Realm 2')
    realm_label_2.grid(row=1, column=0, padx=10, pady= 10)

    var_realm_enr_2 = StringVar()
    realm_etr_2 = ttk.Entry(data_frame, textvariable=var_realm_enr_2, width=15)
    realm_etr_2.grid(row=1, column=1, padx=10, pady=10)

    realm_label_3 = ttk.Label(data_frame, text = 'Realm 3')
    realm_label_3.grid(row=2, column=0, padx=10, pady= 10)

    var_realm_enr_3 = StringVar()
    realm_etr_3 = ttk.Entry(data_frame, textvariable=var_realm_enr_3, width=15)
    realm_etr_3.grid(row=2, column=1, padx=10, pady=10)

    realm_label_4 = ttk.Label(data_frame, text = 'Realm 4')
    realm_label_4.grid(row=3, column=0, padx=10, pady= 10)

    var_realm_enr_4 = StringVar()
    realm_etr_4 = ttk.Entry(data_frame, textvariable=var_realm_enr_4, width=15)
    realm_etr_4.grid(row=3, column=1, padx=10, pady=10)

    realm_label_5 = ttk.Label(data_frame, text = 'Realm 5')
    realm_label_5.grid(row=4, column=0, padx=10, pady= 10)

    var_realm_enr_5 = StringVar()
    realm_etr_5 = ttk.Entry(data_frame, textvariable=var_realm_enr_5, width=15)
    realm_etr_5.grid(row=4, column=1, padx=10, pady=10)

    realm_label_6 = ttk.Label(data_frame, text = 'Realm 6')
    realm_label_6.grid(row=5, column=0, padx=10, pady= 10)

    var_realm_enr_6 = StringVar()
    realm_etr_6 = ttk.Entry(data_frame, textvariable=var_realm_enr_6, width=15)
    realm_etr_6.grid(row=5, column=1, padx=10, pady=10)

    realm_label_7 = ttk.Label(data_frame, text = 'Realm 7')
    realm_label_7.grid(row=6, column=0, padx=10, pady= 10)

    var_realm_enr_7 = StringVar()
    realm_etr_7 = ttk.Entry(data_frame, textvariable=var_realm_enr_7, width=15)
    realm_etr_7.grid(row=6, column=1, padx=10, pady=10)

    realm_label_8 = ttk.Label(data_frame, text = 'Realm 8')
    realm_label_8.grid(row=7, column=0, padx=10, pady= 10)

    var_realm_enr_8 = StringVar()
    realm_etr_8 = ttk.Entry(data_frame, textvariable=var_realm_enr_8, width=15)
    realm_etr_8.grid(row=7, column=1, padx=10, pady=10)

    realm_label_9 = ttk.Label(data_frame, text = 'Realm 9')
    realm_label_9.grid(row=8, column=0, padx=10, pady= 10)

    var_realm_enr_9 = StringVar()
    realm_etr_9 = ttk.Entry(data_frame, textvariable=var_realm_enr_9, width=15)
    realm_etr_9.grid(row=8, column=1, padx=10, pady=10)

    realm_label_10 = ttk.Label(data_frame, text = 'Realm 10')
    realm_label_10.grid(row=9, column=0, padx=10, pady= 10)

    var_realm_enr_10 = StringVar()
    realm_etr_10 = ttk.Entry(data_frame, textvariable=var_realm_enr_10, width=15)
    realm_etr_10.grid(row=9, column=1, padx=10, pady=10) 

    
    btn_frame = LabelFrame(realm_root, text= 'Options')
    btn_frame.pack(fill='x', expand='yes', padx=20)
    btn_frame.configure(bg='#f0f0f0')  
    #---------------------------

    def save():
        #-------------------
        conn = sqlite3.connect('M+DataBase.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists realms (
        realm_1 text,
        realm_2 text,
        realm_3 text,
        realm_4 text,
        realm_5 text,
        realm_6 text,
        realm_7 text,
        realm_8 text,
        realm_9 text,
        realm_10 text)''')
        import_list = ['', '', '', '', '', '', '', '', '', '']  
        c.execute('INSERT INTO realms (realm_1, realm_2, realm_3, realm_4, realm_5, realm_6, realm_7, realm_8, realm_9, realm_10) VALUES(?,?,?,?,?,?,?,?,?,?)' , import_list)
        update = "UPDATE realms SET realm_1 = ? , realm_2 = ? , realm_3 = ? , realm_4 = ? , realm_5 = ?, realm_6 = ?, realm_7 = ?, realm_8 = ?, realm_9 = ?, realm_10 = ? WHERE rowid = ?"
        if realm_etr_1.get().isspace():
            realm_etr_1.delete(0, END)
        elif realm_etr_2.get().isspace():
            realm_etr_2.delete(0, END)
        elif realm_etr_3.get().isspace():
            realm_etr_3.delete(0, END)
        elif realm_etr_4.get().isspace():
            realm_etr_4.delete(0, END)
        elif realm_etr_5.get().isspace():
            realm_etr_5.delete(0, END)
        elif realm_etr_6.get().isspace():
            realm_etr_6.delete(0, END)
        elif realm_etr_7.get().isspace():
            realm_etr_7.delete(0, END)
        elif realm_etr_8.get().isspace():
            realm_etr_8.delete(0, END)
        elif realm_etr_9.get().isspace():
            realm_etr_9.delete(0, END)
        elif realm_etr_10.get().isspace():
            realm_etr_10.delete(0, END)       
        
        
        data = [realm_etr_1.get(), realm_etr_2.get(), realm_etr_3.get(), realm_etr_4.get(), realm_etr_5.get(), realm_etr_6.get(), realm_etr_7.get(), realm_etr_8.get(), realm_etr_9.get(), realm_etr_10.get(), 1]  
        c.execute(update, data)
        c.execute('DELETE from realms WHERE rowid ='+ '2')
        conn.commit()
        messagebox.showinfo('Done', 'Your request has been successfully submitted')
        c.close()
        realm_root.destroy()
    def insert(self):
        realm_etr_1.insert(0, self[0][0])
        realm_etr_2.insert(0, self[0][1])
        realm_etr_3.insert(0, self[0][2])
        realm_etr_4.insert(0, self[0][3])
        realm_etr_5.insert(0, self[0][4])
        realm_etr_6.insert(0, self[0][5])
        realm_etr_7.insert(0, self[0][6])
        realm_etr_8.insert(0, self[0][7])
        realm_etr_9.insert(0, self[0][8])
        realm_etr_10.insert(0, self[0][9])


    def delete():
        realm_etr_1.delete(0, END)
        realm_etr_2.delete(0, END)
        realm_etr_3.delete(0, END)
        realm_etr_4.delete(0, END)
        realm_etr_5.delete(0, END)
        realm_etr_6.delete(0, END)
        realm_etr_7.delete(0, END)
        realm_etr_8.delete(0, END)
        realm_etr_9.delete(0, END)
        realm_etr_10.delete(0, END)
    #-------------------
    def get():
        conn = sqlite3.connect('M+DataBase.db')
        c = conn.cursor()
        c.execute('SELECT * FROM realms WHERE rowid =' + '1')
        records = c.fetchall()
        # print(records[0],records[1],records[2],records[3],records[4],records[5],records[6],records[7],records[8],records[9])
        delete()
        insert(records)
        conn.commit()
        c.close()

    #---------------------------
    realm_btn_save = ttk.Button(btn_frame, text='Save', style='TButton', width=12, command=save)
    realm_btn_save.grid(row=0, column=0, padx=10, pady=10)

    realm_btn_get = ttk.Button(btn_frame, text='Get Names', style='TButton', width=13, command=get)
    realm_btn_get.grid(row=0, column=1, padx=10, pady=10)
    
    get()
    realm_root.mainloop()

def realm_db():
    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists realms (
    realm_1 text,
    realm_2 text,
    realm_3 text,
    realm_4 text,
    realm_5 text,
    realm_6 text,
    realm_7 text,
    realm_8 text,
    realm_9 text,
    realm_10 text)''')
    import_list = ['', '', '', '', '', '', '', '', '', '']  
    c.execute('INSERT INTO realms (realm_1, realm_2, realm_3, realm_4, realm_5, realm_6, realm_7, realm_8, realm_9, realm_10) VALUES(?,?,?,?,?,?,?,?,?,?)' , import_list)
    conn.commit()
    c.execute('DELETE from realms WHERE rowid ='+ '2')
    conn.commit()
    c.close()