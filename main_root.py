from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from traceback import print_tb
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import colorchooser
from configparser import ConfigParser
import sqlite3
import csv
from PyInstaller.utils.hooks import collect_submodules
from PIL import ImageTk, Image
import adv_root
import realm_root

#data

# data = [[1, '+15', 120000, 'Blature', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [2, '+10', 320000, 'Thefinam', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [3, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Twisting Nether', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [4, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', False, 'test test test'],
#         [5, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', False, 'test test test'],
#         [6, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [7, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [8, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [9, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [10, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [11, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [12, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],
#         [111, '+20', 140000, 'Jacko', 'Necrotic Wake', '14/03/2022', 'Draenor', 'Noxic', 'Noxic#1112', True, 'test test test'],

# ]


root = Tk()
root.configure(bg='#f0f0f0')
# root.set_theme('classic')
root.title('Mythic Plus Managment')
root.iconbitmap('ico/icon.ico')
root.geometry('1020x620')
root.resizable(0, 0)
#----------------
#config
# hightlight color #347083
# primary color lightblue
# secondary color white
# button color #03A9F4





parser = ConfigParser()
parser.read('M+Config.ini')

saved_primary_color = parser.get('colors', 'primary_color')
saved_secondary_color = parser.get('colors', 'secondary_color')
saved_highlight_color = parser.get('colors', 'highlight_color')
# saved_button_color = parser.get('colors', 'button_color')


#add menu

def primary_color():
    primary_color = colorchooser.askcolor()[1]
    # my_tree.tag_configure('oddrow', background='white')
    if primary_color :
        my_tree.tag_configure('evenrow', background=primary_color)

        parser = ConfigParser()
        parser.read('M+Config.ini')
        parser.set('colors', 'primary_color', primary_color)
        with open('M+Config.ini', 'w') as configfile:
            parser.write(configfile)
def secondary_color():
    secondary_color = colorchooser.askcolor()[1]
    if secondary_color :
        my_tree.tag_configure('oddrow', background=secondary_color)

        parser = ConfigParser()
        parser.read('M+Config.ini')
        parser.set('colors', 'secondary_color', secondary_color)
        with open('M+Config.ini', 'w') as configfile:
            parser.write(configfile)

def highlight_color():
    highlight_color = colorchooser.askcolor()[1]
    if highlight_color :
        style.map('Treeview', background=[('selected', highlight_color)])

        parser = ConfigParser()
        parser.read('M+Config.ini')
        parser.set('colors', 'hightlight_color', highlight_color)
        with open('M+Config.ini', 'w') as configfile:
            parser.write(configfile)

# def button_color():
#     button_color = colorchooser.askcolor()[1]
#     if button_color :
#         #buttons
#         btn_update.config(fg_color=button_color)
#         btn_add.config(fg_color=button_color) 
#         btn_remove_many.config(fg_color=button_color)
#         # btn_select.config(fg_color=button_color)

#         parser = ConfigParser()
#         parser.read('M+Config.ini')
#         parser.set('colors', 'button_color', button_color)
#         with open('M+Config.ini', 'w') as configfile:
#             parser.write(configfile)
#setcolor
def set_color():
    my_tree.tag_configure('evenrow', background='lightblue')
    my_tree.tag_configure('oddrow', background='white')
    style.map('Treeview', background=[('selected', '#347083')])
    # btn_update.config(fg_color='#03A9F4')
    # btn_add.config(fg_color='#03A9F4')
    # btn_remove_many.config(fg_color='#03A9F4')
    # btn_select.config(fg_color='#03A9F4')
    parser = ConfigParser()
    parser.read('M+Config.ini')
    parser.set('colors', 'primary_color', 'lightblue')
    parser.set('colors', 'secondary_color', 'white')
    parser.set('colors', 'highlight_color', '#347083')
    # parser.set('colors', 'button_color', '#03A9F4')
    with open('M+Config.ini', 'w') as configfile:
        parser.write(configfile)

    
#----------------------------------





#sqlite3

conn = sqlite3.connect('M+DataBase.db')
c = conn.cursor()
c.execute('''CREATE TABLE if not exists runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    key text NOT NULL,
    pot integer NOT NULL,
    advertiser text NOT NULL,
    dungeon text NOT NULL,
    date text,
    realm text NOT NULL,
    char_name text,
    bTag text,
    pay_info text NOT NULL,
    info text)
    ''')

# for record in data:
#     c.execute('INSERT INTO runs VALUES (:id, :key, :pot, :advertiser, :dungeon, :date, :realm, :char_name, :btag, :pay_info, :info)',
#         {
#         'id': record[0],
#         'key': record[1],
#         'pot': record[2],
#         'advertiser': record[3],
#         'dungeon': record[4],
#         'date': record[5],
#         'realm': record[6],
#         'char_name': record[7],
#         'btag': record[8],
#         'pay_info': record[9],
#         'info': record[10],
        
#         }

#         )


# conn.commit()
conn.close()

def select_database():
    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()  
    c.execute('SELECT * FROM runs')
    global records
    records = c.fetchall()
    
    global count
    count = 0
    

    for record in records :
        if count % 2 == 0 :
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]), tags=('oddrow',))
        count += 1
    conn.commit() 
    conn.close()


#tkinter 
style = ttk.Style()
style.theme_use('vista')
style.configure('Treeview', background='#D3D3D3', foreground='black', rowheight=25, fieldbackground='#D3D3D3')
style.map('Treeview', background=[('selected', saved_highlight_color)])

tree_frame = Frame(root)
tree_frame.pack(pady=10, fill= X, padx = 10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
my_tree.pack(fill=X, expand=1)

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ('ID', 'Key', 'POT', 'Advertiser', 'Dungeon', 'Date', 'Realm', 'Char Name', 'BTag', 'Pay Info', 'Info')

my_tree.column("#0", width=0, stretch=NO)
my_tree.column('ID', anchor=W, width=5)
my_tree.column('Key', anchor=W, width=10)
my_tree.column('POT', anchor=CENTER, width=30)
my_tree.column('Advertiser', anchor=CENTER, width=70)
my_tree.column('Dungeon', anchor=CENTER, width=90)
my_tree.column('Date', anchor=CENTER, width=40)
my_tree.column('Realm', anchor=CENTER, width=70)
my_tree.column('Char Name', anchor=CENTER, width=70)
my_tree.column('BTag', anchor=CENTER, width=70)
my_tree.column('Pay Info', anchor=CENTER, width=15)
my_tree.column('Info', anchor=CENTER, width=80)

my_tree.heading("#0", text='', anchor=W)
my_tree.heading('ID', text='ID', anchor=W)
my_tree.heading('Key', text='Key', anchor=W)
my_tree.heading('POT', text='POT', anchor=CENTER)
my_tree.heading('Advertiser', text='Advertiser', anchor=CENTER)
my_tree.heading('Dungeon', text='Dungeon', anchor=CENTER)
my_tree.heading('Date', text='Date', anchor=CENTER)
my_tree.heading('Realm', text='Realm', anchor=CENTER)
my_tree.heading('Char Name', text='Char Name', anchor=CENTER)
my_tree.heading('BTag', text='BTag', anchor=CENTER)
my_tree.heading('Pay Info', text='Pay Info', anchor=CENTER)
my_tree.heading('Info', text='Info',anchor=CENTER)



my_tree.tag_configure('oddrow', background=saved_secondary_color)
my_tree.tag_configure('evenrow', background=saved_primary_color)


#-----------------------------------------------
def advertisers_catch(list):
    adv_root.adv_db()
    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM advertisers WHERE rowid='+ '1')
    adv_records = c.fetchall()
    for new_list in adv_records[0]:
        if new_list != '':
            list.append(new_list)

#-----------------------------------------------
def realms_catch(list):
    realm_root.realm_db()
    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM realms WHERE rowid='+ '1')
    realm_records = c.fetchall()
    for new_list in realm_records[0]:
        if new_list != '':
            list.append(new_list)
#-----------------------------------------------
mythic_level = ['Choose your option', 'Mythic level 0', 'Mythic level +2', 'Mythic level +3', 'Mythic level +4', 'Mythic level +5', 'Mythic level +6', 'Mythic level +7', 'Mythic level +8', 'Mythic level +9', 'Mythic level +10', 'Mythic level +11', 'Mythic level +12', 'Mythic level +13', 'Mythic level +14'
,'Mythic level +15' ,'Mythic level +16', 'Mythic level +17', 'Mythic level +18', 'Mythic level +19', 'Mythic level +20']
#-----------------------------------------------
realms = ['Choose your option']
realms_catch(realms)
#-----------------------------------------------
dungeons = ('Choose your option','The Necrotic Wake','Plaguefall', 'Mists of Tirna Scithe', 'Halls of Atonement', 'Theater of Pain', 'De Other Side', 'Spires of Ascension', 'Sanguine Depths', 'Streets of Wonder', "So'leah's Gambit")
#-----------------------------------------------
advertisers = ['Choose your option']
advertisers_catch(advertisers) 
#-----------------------------------------------

style.configure('TMenubutton', background='#c8c8c8')

data_frame = LabelFrame(root, text= 'Record')
data_frame.pack(fill='x', expand='yes', padx=20)
data_frame.configure(bg='#f0f0f0')


key_label = ttk.Label(data_frame, text = 'Key Level')
key_label.grid(row=0, column=0, padx=10, pady= 10)
var_key_spin = StringVar()
key_spin = ttk.OptionMenu(data_frame, var_key_spin, *mythic_level)
key_spin.config(width=20, style='TMenubutton')
key_spin.grid(row=0, column=1, padx=10, pady=10)

pot_label = ttk.Label(data_frame, text = 'POT')
pot_label.grid(row=0, column=2, padx=10, pady= 10)
var_pot_entry = IntVar()
pot_entry = ttk.Entry(data_frame, width=8, textvariable=var_pot_entry)
pot_entry.grid(row=0, column=3, padx=10, pady= 10)
pot_entry.delete(0, END)

adv_label = ttk.Label(data_frame, text = 'Advertiser')
adv_label.grid(row=0, column=4, padx=10, pady= 10)
var_adv_spin = StringVar()
adv_spin = ttk.OptionMenu(data_frame, var_adv_spin, *advertisers )
adv_spin.config(width=20)
adv_spin.grid(row=0, column=5, padx=10, pady= 10)

dung_label = ttk.Label(data_frame, text = 'Dungeon')
dung_label.grid(row=0, column=6, padx=10, pady= 10)
var_dung_spin = StringVar()
dung_spin = ttk.OptionMenu(data_frame, var_dung_spin, *dungeons )
dung_spin.config(width=20)
dung_spin.grid(row=0, column=7, padx=10, pady= 10)

realm_label = ttk.Label(data_frame, text = 'Realm')
realm_label.grid(row=1, column=0, padx=10, pady= 10)
var_realm_spin = StringVar()
realm_spin = ttk.OptionMenu(data_frame, var_realm_spin, *realms )
realm_spin.config(width=20)
realm_spin.grid(row=1, column=1, padx=10, pady= 10)

date_label = ttk.Label(data_frame, text = 'Date')
date_label.grid(row=1, column=2, padx=10, pady= 10)
var_date_entry = StringVar()
date_entry = DateEntry(data_frame, background='darkblue', foreground='white', borderwidth='2', year=2022, width=10, textvariable=var_date_entry)
date_entry.grid(row=1, column=3, padx=10, pady= 10)



char_label = ttk.Label(data_frame, text = 'Buyer Charecter Name')
char_label.grid(row=1, column=4, padx=10, pady= 10)
var_char_entry = StringVar()
char_entry = ttk.Entry(data_frame, width=15, textvariable=var_char_entry)
char_entry.grid(row=1, column=5, padx=10, pady= 10)

bt_label = ttk.Label(data_frame, text = 'Btag')
bt_label.grid(row=1, column=6, padx=10, pady= 10)
var_bt_entry = StringVar()
bt_entry = ttk.Entry(data_frame, width=15, textvariable=var_bt_entry)
bt_entry.grid(row=1, column=7, padx=10, pady= 10)

pay_label = ttk.Label(data_frame, text = 'Pay Info')
pay_label.grid(row=2, column=0, padx=10, pady= 10)
pay = IntVar()
pay_radio = Checkbutton(data_frame, text='Paid', variable=pay)
pay_radio.grid(row=2, column=1, padx=10, pady= 10)

info_label = ttk.Label(data_frame, text = 'Info')
info_label.grid(row=2, column=2, padx=10, pady= 10)

info_entry = ttk.Entry(data_frame, width=15)
info_entry.grid(row=2, column=3, padx=10, pady= 10)


#select


def select(event):
    try:
        # id_entry.delete(0, END)
        key_spin['menu'].delete(0, END)
        dung_spin['menu'].delete(0, END)
        
        date_entry.delete(0, END)
        info_entry.delete(0, END)
        
        bt_entry.delete(0, END)
        char_entry.delete(0, END)
        realm_spin['menu'].delete(0, END)
        dung_spin['menu'].delete(0, END)
        pot_entry.delete(0, END)

        selected = my_tree.focus()

        values = my_tree.item(selected, 'values')

        # id_entry.insert(0, values[0])
        #advertiser optionmenu
        advertisers_new = [values[3]]
        advertisers_catch(advertisers_new) 
        var_adv_spin.set('') 
        adv_spin_1 = ttk.OptionMenu(data_frame, var_adv_spin, *advertisers_new )
        adv_spin_1.config(width=20)
        adv_spin_1.grid(row=0, column=5, padx=10, pady= 10)   



        #realm optionmenu
        realms_new = [values[6]]
        realms_catch(realms_new)
        var_realm_spin.set('')
        realm_spin_1 = ttk.OptionMenu(data_frame, var_realm_spin, *realms_new )
        realm_spin_1.config(width=20)
        realm_spin_1.grid(row=1, column=1, padx=10, pady= 10)


        #mythic optionmenu                                                 # key_spin.insert(0, f'Mythic Level {values[1]}')
        mythic_level = [f'Mythic level {values[1]}','Mythic level 0', 'Mythic level +2', 'Mythic level +3', 'Mythic level +4', 'Mythic level +5', 'Mythic level +6', 'Mythic level +7', 'Mythic level +8', 'Mythic level +9', 'Mythic level +10', 'Mythic level +11', 'Mythic level +12', 'Mythic level +13', 'Mythic level +14'
                        ,'Mythic level +15' ,'Mythic level +16', 'Mythic level +17', 'Mythic level +18', 'Mythic level +19', 'Mythic level +20']
        var_key_spin.set('')
        key_spin_1 = ttk.OptionMenu(data_frame, var_key_spin, *mythic_level )
        key_spin_1.config(width=20)
        key_spin_1.grid(row=0, column=1, padx=10, pady= 10)
        


        #dung optionmenu
        var_dung_spin.set('')
        dungeons = [values[4],'The Necrotic Wake','Plaguefall', 'Mists of Tirna Scithe', 'Halls of Atonement', 'Theater of Pain', 'De Other Side', 'Spires of Ascension', 'Sanguine Depths', 'Streets of Wonder', "So'leah's Gambit"]
        dung_spin_1 = ttk.OptionMenu(data_frame, var_dung_spin, *dungeons )
        dung_spin_1.config(width=20)
        dung_spin_1.grid(row=0, column=7, padx=10, pady= 10)
        date_entry.insert(0, values[5])
        info_entry.insert(0, values[10])
        
        if values[9] == 'True' :
            
            pay_radio.select()
            
            
        elif values[9] == 'False' :
            pay_radio.deselect()
            
            
            
        bt_entry.insert(0, values[8])
        char_entry.insert(0, values[7])
        # realm_spin.insert(0, values[6])
        # adv_spin.insert(0, values[3])
        pot_entry.insert(0, values[2])
    
    except IndexError:
        pass

def clear():
    # id_entry.delete(0, END)
    # key_spin.delete(0, END)
    # dung_spin.delete(0, END)
    date_entry.delete(0, END)
    info_entry.delete(0, END)
    pay_radio.deselect()
    bt_entry.delete(0, END)
    char_entry.delete(0, END)
    # realm_spin.delete(0, END)
    # adv_spin.delete(0, END)
    pot_entry.delete(0, END)

# def move_up():
#     rows = my_tree.selection()
#     for row in rows :
#         my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# def move_down():
#     rows = my_tree.selection()
#     for row in reversed(rows) :
#         my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()
    c.execute('DELETE from runs WHERE ID =' + records[0][0])
    conn.commit()
    conn.close()
    #clear 
    clear()

    #add message box

    messagebox.showinfo('Deleted', 'Your Record Has been DELETED !')


def remove_many():

    response = messagebox.askyesno('Delete Request', 'Are you sure about that ?')
    if response == 1 :
        x = my_tree.selection()
        want_to_delete = []
        for record in x :
            del_ = my_tree.item(record, 'values')[0]
            want_to_delete.append(del_)

        for record in x :
            my_tree.delete(record)
        
        conn = sqlite3.connect('M+DataBase.db')
        c = conn.cursor()
        # c.execute('''CREATE TABLE if not exists deleted_runs (
        #             id INTEGER PRIMARY KEY AUTOINCREMENT ,
        #             key text NOT NULL,
        #             pot integer NOT NULL,
        #             advertiser text NOT NULL,
        #             dungeon text NOT NULL,
        #             date text,
        #             realm text NOT NULL,
        #             char_name text,
        #             bTag text,
        #             pay_info text NOT NULL,
        #             info text)
        #             ''')
                    
        
        
        # c.execute('SELECT * from runs WHERE ID = ?', [(a,) for a in want_to_delete] )
        # deleted_records = c.fetchall()
        # print(deleted_records)
        
        
        
        
        # list_deleted = [deleted_records[0][1], deleted_records[0][2], deleted_records[0][3], deleted_records[0][4], deleted_records[0][5], deleted_records[0][6], deleted_records[0][7], deleted_records[0][8], deleted_records[0][9], deleted_records[0][10]]
        
        # c.execute('INSERT INTO deleted_runs (key, pot, advertiser, dungeon, date, realm, char_name, btag, pay_info, info) VALUES(?,?,?,?,?,?,?,?,?,?)', list_deleted)
        # conn.commit()

        
        c.executemany('DELETE from runs WHERE ID = ?', [(a,) for a in want_to_delete])
        conn.commit()
        c.close()
        #clear 
        clear()

        #add message box

        messagebox.showinfo('Deleted', 'Your Record Has been DELETED !')

def update():
    selected = my_tree.selection()
    if pay.get() == 1 :
        x = "True"
    elif pay.get() == 0:
        x = "False"
    
    

    key_spin_just_number = str(var_key_spin.get()).split()
    

    my_tree.item(selected, text='', values=(records[0][0], key_spin_just_number[2], pot_entry.get(), var_adv_spin.get(), var_dung_spin.get(), date_entry.get(), var_realm_spin.get(), char_entry.get(), bt_entry.get(), x, info_entry.get(), ))
    #
    
    #id_entry.get("1.0",'end-1c'), key_spin.get("1.0",'end-1c'), adv_spin.get("1.0",'end-1c'), dung_spin.get("1.0",'end-1c'), date_entry.get("1.0",'end-1c'), realm_spin.get("1.0",'end-1c'), char_entry.get("1.0",'end-1c'), bt_entry.get("1.0",'end-1c'), x, info_entry.get("1.0",'end-1c'),

    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()
    # c.execute('''UPDATE runs SET
    #     Key = :key,
    #     POT = :pot,
    #     Advertiser = :advertiser,
    #     Dungeon = :dungeon,
    #     Date = :date,
    #     Realm = :realm,
    #     Char_Name = :char_name,
    #     BTag = :btag,
    #     Pay_Info = :pay_info,
    #     Info = :info
    #     WHERE ID = :id''',
    #     {
    #         'key': key_spin_just_number[2] ,
    #         'pot': pot_entry.get(),
    #         'advertiser': var_adv_spin.get(),
    #         'dungeon': var_dung_spin.get(),
    #         'date': date_entry.get(),
    #         'realm': var_realm_spin.get(),
    #         'char_name': char_entry.get(),
    #         'btag': bt_entry.get(),
    #         'pay_info': x,
    #         'info': info_entry.get(),
    #         'id': id_entry.get(),

    #     })
    
    q = "UPDATE runs SET key = ? , pot = ? , advertiser = ? , dungeon = ? , date = ?, realm = ?, char_name = ?, btag = ?, pay_info = ?, info = ? WHERE id = ?"
    data = (key_spin_just_number[2], pot_entry.get(), var_adv_spin.get(), var_dung_spin.get(), date_entry.get(), var_realm_spin.get(), char_entry.get(), bt_entry.get(), x, info_entry.get(), records[0][0])
    c.execute(q, data)
    # {key_spin_just_number[2]}
    # {pot_entry.get()}
    # {var_adv_spin.get()}
    # {date_entry.get()}
    # {var_dung_spin.get()}
    # {var_realm_spin.get()}
    # {char_entry.get()}
    # {bt_entry.get()}
    # {x}
    # {info_entry.get()}
    # {records[0][0]}
    conn.commit()
    conn.close()

    # id_entry.delete(0, END)
    # key_spin.delete(0, END)
    # dung_spin.delete(0, END)
    date_entry.delete(0, END)
    info_entry.delete(0, END)
    pay_radio.deselect()
    bt_entry.delete(0, END)
    char_entry.delete(0, END)
    # realm_spin.delete(0, END)
    # adv_spin.delete(0, END)
    pot_entry.delete(0, END)

def add():
    try:
        if pay.get() == 1 :
            x = "True"
        elif pay.get() == 0:
            x = "False"
        key_spin_just_number = str(var_key_spin.get()).split()
        conn = sqlite3.connect('M+DataBase.db')
        c = conn.cursor()
        # c.execute('INSERT INTO runs VALUES (:id, :key, :pot, :advertiser, :dungeon, :date, :realm, :char_name, :btag, :pay_info , :info)',
        #     {
        #         # 'id': id_entry.get(),
        #         'key': key_spin_just_number[2] ,
        #         'pot': pot_entry.get(),
        #         'advertiser': var_adv_spin.get(),
        #         'dungeon': var_dung_spin.get(),
        #         'date': date_entry.get(),
        #         'realm': var_realm_spin.get(),
        #         'char_name': char_entry.get(),
        #         'btag': bt_entry.get(),
        #         'pay_info': x,
        #         'info': info_entry.get(),
                
                
        #     }
        
        # )
        
        if var_key_spin.get() == 'Choose your option' :
            messagebox.showinfo('Key', 'You need to fill out the key entry !')
        elif pot_entry.get() == '' or pot_entry.get() == ' ' or pot_entry.get() == '  ' :
            messagebox.showinfo('POT', 'You need to fill out the pot entry !')
        elif var_adv_spin.get() == 'Choose your option' :
            messagebox.showinfo('Advertiser', 'You need to fill out the advertiser entry !')
        elif var_dung_spin.get() == 'Choose your option' :
            messagebox.showinfo('Dungeon', 'You need to fill out the dungeon entry !')
        elif var_realm_spin.get() == 'Choose your option' :
            messagebox.showinfo('Realm', 'You need to fill out the realm entry !')
        
        
        else:
            import_list = [key_spin_just_number[2], pot_entry.get(), var_adv_spin.get(), var_dung_spin.get(), date_entry.get(), var_realm_spin.get(), char_entry.get(), bt_entry.get(), x, info_entry.get()]
            c.execute('INSERT INTO runs (key, pot, advertiser, dungeon, date, realm, char_name, btag, pay_info, info) VALUES(?,?,?,?,?,?,?,?,?,?)' , import_list)

            conn.commit()
            conn.close()
        # id_entry.delete(0, END)
        # key_spin.delete(0, END)
        # dung_spin.delete(0, END)
            date_entry.delete(0, END)
            info_entry.delete(0, END)
            pay_radio.deselect()
            bt_entry.delete(0, END)
            char_entry.delete(0, END)
            # realm_spin.delete(0, END)
            # adv_spin.delete(0, END)
            pot_entry.delete(0, END)
            conn.close()
        #clear treeview

            my_tree.delete(*my_tree.get_children())
            select_database()
    except sqlite3.IntegrityError:
        messagebox.showinfo("Error", "An error has occurred. try again")
    except sqlite3.OperationalError:
        messagebox.showinfo('Error', 'An error has occurred. try again')



def csv_():
    conn = sqlite3.connect('M+DataBase.db')
    c = conn.cursor()  
    c.execute('SELECT * FROM runs')
    
    records = c.fetchall()

    header = ['id', 'key', 'pot', 'advertiser', 'dungeon', 'date', 'realm', 'charname', 'btag', 'pay_info', 'info']
    
    savefile = filedialog.asksaveasfilename(defaultextension=".csv", initialdir='', title='Save File', filetypes=(('Csv files','.csv'),))
    
    if savefile:

        with open(savefile, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            

                    # write multiple rows
            writer.writerows(records)

button_frame = LabelFrame(root, text='Commands')
button_frame.pack(fill='x', expand='yes', padx=20)
button_frame.configure(bg='#f0f0f0')

style.configure('TButton', foreground="Black", background="black")

btn_update = ttk.Button(button_frame, text='Update Data', style='TButton', width=12, command=update)
btn_update.grid(row=0, column=1, padx=10, pady=10)

btn_add = ttk.Button(button_frame, text='Add Data', style='TButton', width=12, command=add)
btn_add.grid(row=0, column=2, padx=10, pady=10)

btn_remove_many = ttk.Button(button_frame, text='Remove Data', style='TButton', width=12, command=remove_many)
btn_remove_many.grid(row=0, column=3, padx=10, pady=10)

btn_clear = ttk.Button(button_frame, text='Clear ', style='TButton', width=12, command=clear)
btn_clear.grid(row=0, column=4, padx=10, pady=10)

variable = StringVar()
variable.set("The Necrotic Wake")
style.configure('TButton', width=20)

root.option_add("*Menu.borderWidth", "3")
root.option_add("*Menu.activeBorderWidth", "3")
root.option_add("*Menu.background", "white")
root.option_add("*Menu.border", "10")
# ['keramik', 'adapta', 'scidpurple', 'radiance', 'scidgrey', 'ubuntu'
# , 'black', 'arc', 'winnative', 'equilux', 'smog', 'yaru', 'xpnative'
# , 'kroc', 'blue', 'scidsand', 'classic', 'alt', 'breeze', 'winxpblue'
# , 'scidpink', 'scidblue', 'scidgreen', 'default', 'plastik'
# , 'clam', 'itft1', 'clearlooks', 'vista', 'scidmint', 'aquativo', 'elegance']

# print(root.get_themes())
Font_tuple = ("Comic Sans MS", 15, "bold")
empty_0 = Label(button_frame, text='').grid(row=0, column=5, padx=140, pady=10)
logo = ImageTk.PhotoImage(Image.open("ico/icon.png"))
empty_1 = Label(button_frame, image=logo).grid(row=0, column=6, padx=0, pady=10)
empty_2 = Label(button_frame, text='Created By Blature', font= Font_tuple).grid(row=0, column=7, padx=0, pady=10)

my_tree.bind('<ButtonRelease-1>', select)


select_database()
#----------------------------------

    

#----------------------------------
#csv menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=0)

my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Export CSV', command=csv_)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Theme', menu=option_menu)


option_menu.add_command(label='Primary Color', command=primary_color)
option_menu.add_command(label='Secondary Color', command=secondary_color)
option_menu.add_command(label='Highlight Color', command=highlight_color)
# option_menu.add_command(label='Buttons Color', command=button_color)
option_menu.add_separator()
option_menu.add_command(label='Default Theme', command=set_color)



config_menu = Menu(my_menu, tearoff=0)

my_menu.add_cascade(label='Config', menu=config_menu)
config_menu.add_command(label='Advertisers', command=adv_root.adv_root)
config_menu.add_command(label='Realms', command=realm_root.realm_root)



root.mainloop()








