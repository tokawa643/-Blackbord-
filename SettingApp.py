import tkinter as tk
from tkinterdnd2 import DND_TEXT, TkinterDnD
import sqlite3
import webbrowser
from tkinter import messagebox

conn = sqlite3.connect('url.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS url (id integer PRIMARY KEY AUTOINCREMENT,
            chk_number integer, name text, url text, chk_comits integer);''')
c.execute('select count(*) from url')
count = c.fetchone()
while count[0] < 30:
    try:
        c.execute("INSERT INTO url(chk_number,name,url,chk_comits) VALUES(1,'','',1)")
        conn.commit()
        c.execute('select count(*) from url')
        count = c.fetchone()        
    except:
        print('保存できませんでした')
if c.execute('''select trim(replace(url, ' ', '_')) from url'''):    
    acquire_entries = c.fetchall()
if c.execute('''select trim(replace(name, ' ', '_')) from url'''):    
    acquire_names = c.fetchall()  
if c.execute('SELECT chk_number FROM url'):
    acquire_chknumbers = c.fetchall()  
if c.execute('SELECT chk_comits FROM url'):
    acquire_chkcomits = c.fetchall()   
table_name = 'url'  

conn = sqlite3.connect('url2.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS url2 (id integer PRIMARY KEY AUTOINCREMENT, email text, password text, email2 text, password2 text);''')
c.execute('select count(*) from url2')
count = c.fetchone()
while count[0] < 1:
    try:
        c.execute("INSERT INTO url2(email,password,email2,password2) VALUES('','','','')")
        conn.commit()
        c.execute('select count(*) from url2')
        count = c.fetchone()        
    except:
        print('保存できませんでした2')
conn.commit()
conn.close()
table_name2 = 'url2'


# Tkinter お決まりフレーズ
class App(TkinterDnD.Tk) :
    def __init__(self) :
        super().__init__()    

        # タイトルとウィンドウサイズ
        self.title('設定フォーム－Blackbord「連絡事項」「教材」更新通知アプリ－')
        self.resizable(0, 0)
        self.geometry('780x760+0+0')
        self.configure(bg='snow') 

        self.men = tk.Menu(self, background='#003898', tearoff=0) 
        self.config(menu=self.men)
        menu_file = tk.Menu(self, tearoff=0, activebackground='sky blue', activeforeground='black')             
        self.men.add_cascade(label='必須', menu=menu_file)  
        def subscribe_form():
            def keep_login_elem2():
                getry1 = entry1_change.get() 
                getry2 = entry2_change.get()       
                try:
                    conn = sqlite3.connect('url2.db')
                    c = conn.cursor()
                    c.execute("UPDATE %s SET email=? WHERE id=?" % table_name2,(getry1, 1))
                    c.execute("UPDATE %s SET password=? WHERE id=?" % table_name2,(getry2, 1))
                    conn.commit()           
                    conn.close()               
                    messagebox.showinfo('', 'stuアカウントを登録しました') 
                    sub_win.destroy()
                except:
                    messagebox.showerror('エラー', 'アカウントを保存できませんでした')     
            def pass_disp():
                getvar = keep_button_var.get()
                if getvar == True:
                    entry2_change.configure(show='')
                else:
                    entry2_change.configure(show='・')            
            sub_win = tk.Toplevel()
            sub_win.resizable(0, 0)
            sub_win.geometry("400x200+560+250")
            sub_win.title('stuアカウント登録フォーム－Blackbord「連絡事項」「教材」更新通知アプリ－')
            sub_win.configure(bg='snow')         
            label1_change = tk.Label(sub_win, text='ID', width=10, bg='snow')        
            label2_change = tk.Label(sub_win, text='パスワード', width=10, bg='snow')        
            entry1_change = tk.Entry(sub_win, width=30)
            entry2_change = tk.Entry(sub_win, show='・', width=30)
            conn = sqlite3.connect('url2.db')
            c = conn.cursor()
            if c.execute('''select trim(replace(email, ' ', '_')) from url2'''):    
                acquire_email = c.fetchone()
            if c.execute('''select trim(replace(password, ' ', '_')) from url2'''):    
                acquire_pass = c.fetchone()             
            entry1_change.insert(0, acquire_email[0])
            entry2_change.insert(0, acquire_pass[0])
            keep_button = tk.Button(sub_win, width=7, text='保存', command=keep_login_elem2) 
            keep_button_var = tk.BooleanVar()
            keep_button_chk = tk.Checkbutton(sub_win, command=pass_disp, text='パスワードを表示する', bg='snow', activebackground='snow', variable=keep_button_var, onvalue=True, offvalue=False)        
            label1_change.place(x=75,y=10)
            label2_change.place(x=90,y=70)        
            entry1_change.place(x=105,y=30)
            entry2_change.place(x=105,y=90)
            keep_button.place(x=230,y=150)
            keep_button_chk.place(x=100,y=110)  
        menu_file.add_command(label='stuアカウント登録', command=subscribe_form)               
        def subscribe_form2():
            def keep_login_elem2():
                getry1 = entry1_change.get() 
                getry2 = entry2_change.get()       
                try:
                    conn = sqlite3.connect('url2.db')
                    c = conn.cursor()
                    c.execute("UPDATE %s SET email2=? WHERE id=?" % table_name2,(getry1, 1))
                    c.execute("UPDATE %s SET password2=? WHERE id=?" % table_name2,(getry2, 1))
                    conn.commit()           
                    conn.close()               
                    messagebox.showinfo('', '教育用アカウントを登録しました') 
                    sub_win.destroy()
                except:
                    messagebox.showerror('エラー', 'アカウントを保存できませんでした')     
            def pass_disp2():
                getvar = keep_button_var.get()
                if getvar == True:
                    entry2_change.configure(show='')
                else:
                    entry2_change.configure(show='・')            
            sub_win = tk.Toplevel()
            sub_win.resizable(0, 0)
            sub_win.geometry("400x200+560+250")
            sub_win.title('教育用アカウント登録フォーム－Blackbord「連絡事項」「教材」更新通知アプリ－')
            sub_win.configure(bg='snow')         
            label1_change = tk.Label(sub_win, text='ID', width=10, bg='snow')        
            label2_change = tk.Label(sub_win, text='パスワード', width=10, bg='snow')        
            entry1_change = tk.Entry(sub_win, width=30)
            entry2_change = tk.Entry(sub_win, show='・', width=30)
            conn = sqlite3.connect('url2.db')
            c = conn.cursor()
            if c.execute('''select trim(replace(email2, ' ', '_')) from url2'''):    
                acquire_email = c.fetchone()
            if c.execute('''select trim(replace(password2, ' ', '_')) from url2'''):    
                acquire_pass = c.fetchone()             
            entry1_change.insert(0, acquire_email[0])
            entry2_change.insert(0, acquire_pass[0])
            keep_button = tk.Button(sub_win, width=7, text='保存', command=keep_login_elem2) 
            keep_button_var = tk.BooleanVar()
            keep_button_chk = tk.Checkbutton(sub_win, command=pass_disp2, text='パスワードを表示する', bg='snow', activebackground='snow', variable=keep_button_var, onvalue=True, offvalue=False)        
            label1_change.place(x=75,y=10)
            label2_change.place(x=90,y=70)        
            entry1_change.place(x=105,y=30)
            entry2_change.place(x=105,y=90)
            keep_button.place(x=230,y=150)
            keep_button_chk.place(x=100,y=110)                    
        menu_file.add_command(label='教育用アカウント登録', command=subscribe_form2)                     
                     
        self.FrameWindow = tk.Frame(self, bg='snow')
        self.FrameWindow.place(x=75, y=40) 
        self.canvas = tk.Canvas(self.FrameWindow, width=640, height=670, bg='snow', highlightthickness=0)
        self.canvas.grid(row=0, column=0) 
        self.scrollbar = tk.Scrollbar(self.FrameWindow, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')             
        self.canvas["yscrollcommand"] = self.scrollbar.set
        # Canvasの位置の初期化
        self.canvas.yview_moveto(0)
        self.canvas.config(scrollregion=(0,0,0,1340)) #スクロール範囲
        self.frame_canvas = tk.Frame(self.canvas, bg='snow')  #frameの中にcanvas,bar用のframeを作成
        # Frame Widgetを Canvas Widget上に配置
        self.canvas.create_window((0,0), window=self.frame_canvas, anchor=tk.NW, width=self.canvas.cget('width'))
        self.canvas.bind("<MouseWheel>", self.mouse_y_scroll)  
        self.frame_canvas.bind("<MouseWheel>", self.mouse_y_scroll)        

        self.Button_name = tk.Button(self, width=19, bd=0, text='NAME', bg='orange red')
        self.Button_Entry = tk.Button(self, width=58, bd=0, text='URL', bg='orange red')
        self.Button_link = tk.Button(self, width=5, bd=0, text='LINK', bg='orange red')
        self.Button_on_off = tk.Button(self, width=6, bd=0, text='ON/OFF', bg='orange red')
        self.Button_name.place(x=75, y=0)
        self.Button_Entry.place(x=215, y=0)
        self.Button_link.place(x=628, y=0)
        self.Button_on_off.place(x=670, y=0)

        self.var_comits = tk.StringVar(value=acquire_chkcomits[0])      
        self.chk_comits = tk.Checkbutton(self, onvalue='1', offvalue='0',
        bg='snow', activebackground='snow', text='COMITSの通知を許可する',
        variable=self.var_comits, command=self.keep_chk_comits)          
        self.chk_comits.place(x=70, y=720)        

        self.chk_comits.bind('<1>', self.noti_chk_comits)         

        # エントリーウィジェットマネージャを初期化  
        self.nameEntries = []
        self.Entries = []  # エントリーウィジェットのインスタンス
        self.links = []
        self.chks = []
        self.var = []

        # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
        self.index = 0           # 最新のインデックス番号
        self.indexes = []        # インデックスの並び

        # 最初のエントリーウィジェットを作成して配置
        self.createEntry(0)  

        for _ in range(29):
            self.increase_Entry(id=self.index)

        for i in range(30):      
            if acquire_entries[i] == ('',):    
                self.Entries[i].insert(tk.END, 'URLをドラッグ＆ドロップしてください')
            else:
                self.Entries[i].insert(tk.END, acquire_entries[i]) 
            if acquire_names[i] == ('',): 
                self.nameEntries[i].insert(tk.END, '名前を入力してください')                 
            else:
                self.nameEntries[i].insert(tk.END, acquire_names[i])                 
            self.var[i].set((acquire_chknumbers[i]))
            self.chks[i].config(variable=self.var[i])
            if self.var[i].get() == '(0,)':
                self.nameEntries[i]['state'] = 'disable'
                self.Entries[i]['state'] = 'disable'   
                self.links[i]['state']  = 'disable'  

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, 'units')
        elif event.delta < 0:
            self.canvas.yview_scroll(1, 'units')                             

    # エントリーウィジェットを追加するボタンのようなラベルをクリック
    def increase_Entry(self, id) :

        # 追加する位置
        next = self.indexes.index(id) + 1
        self.index = self.index + 1

        # エントリーウィジェットを作成して配置
        self.createEntry(next) 

    # エントリーウィジェットを再配置
    def updateEntries(self):
        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.indexes)) :      
            self.nameEntries[i].grid(column=0, row=i, pady=13)        
            self.Entries[i].grid(column=1, row=i)
            self.Entries[i].lift()
            self.links[i].grid(column=2, row=i, padx=5)
            self.chks[i].grid(column=3, row=i, padx=10)

    # テキストを取得、データベースに追加するボタン
    def keep_name(self, event, id) :
        Getname = []
        current = self.indexes.index(id)
        for current in range(len(self.indexes)) :
            Getname.append(self.nameEntries[current].get())                                  
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]                                        
        null = ''
        try:     
            for i in range(30):   
                conn = sqlite3.connect('url.db')
                c = conn.cursor()    
                if not Getname[i]:                    
                    c.execute("UPDATE %s SET name=? WHERE id=?" % table_name,(null, numbers[i]))                      
                else:
                    c.execute("UPDATE %s SET name=? WHERE id=?" % table_name,(Getname[i], numbers[i]))  
                self.label = tk.Label(self, width=35, text='名前を保存しました!', bg='snow', fg='deep sky blue')
                self.label.place(x=295, y=27)   
                self.label.after(2000, self.label.destroy)       
                conn.commit()
                conn.close()                     
        except:
            event.widget.delete(0, tk.END)
            self.label = tk.Label(self, width=35, text='名前を保存できませんでした', bg='snow', fg='red')
            self.label.place(x=295, y=27)   
            self.label.after(2000, self.label.destroy)  

    def keep_url(self, event, id):  
        GetEntry = []
        current = self.indexes.index(id)
        for current in range(len(self.indexes)) :
            GetEntry.append(self.Entries[current].get())  
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]  
        if 'https://nuchs.blackboard.com/webapps/blackboard/content' in event.widget.get() or 'https://nuchs.blackboard.com/webapps/blackboard/execute' in event.widget.get():                        
            try:      
                for i in range(30):
                    conn = sqlite3.connect('url.db')
                    c = conn.cursor()                
                    c.execute("UPDATE %s SET url=? WHERE id=?" % table_name,(GetEntry[i], numbers[i]))
                    self.label_keep_url = tk.Label(self, width=35, text='URLを保存しました!', fg='deep sky blue', bg='snow')
                    self.label_keep_url.place(x=295, y=27)
                    self.label_keep_url.after(2000, self.label_keep_url.destroy)
                    conn.commit()
                    conn.close()                     
            except:
                event.widget.delete(0, tk.END)
                self.label2 = tk.Label(self, width=35, text='※URLを正常に保存できませんでした', bg='snow', fg='red')
                self.label2.place(x=295, y=27)
                self.label2.after(2000, self.label2.destroy) 
        else:            
            try:                 
                for i in range(30):     
                    event.widget.delete(0, tk.END)   
                    event.widget.config(bg='IndianRed1')                    
                    self.label_keep_url = tk.Label(self, width=35, text='※扱えるURLはBbの「連絡事項」「教材」のページです', fg='red', bg='snow')
                    self.label_keep_url.place(x=295, y=27)
                    event.widget.after(2000, self.snow)
                    self.label_keep_url.after(2000, self.label_keep_url.destroy)                                          
                    conn = sqlite3.connect('url.db')
                    c = conn.cursor()                                                      
                    c.execute("UPDATE %s SET url=? WHERE id=?" % table_name,(self.Entries[i].get(), numbers[i]))                                                    
                    conn.commit()
                    conn.close()                                          
            except:
                event.widget.delete(0, tk.END)
                self.label2 = tk.Label(self, width=35, text='※URLを正常に保存できませんでした', bg='snow', fg='red')
                self.label2.place(x=295, y=27)
                self.label2.after(2000, self.label2.destroy)  

    def keep_chk(self, id):   
        Getvar = []   
        current = self.indexes.index(id)
        for current in range(len(self.indexes)) :
            Getvar.append(self.var[current].get())                 
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]   
        for i in range(30):             
                try:
                    conn = sqlite3.connect('url.db')
                    c = conn.cursor()  
                    if Getvar[i] == '1':               
                        c.execute('select name from url')                           
                        acquire_names = c.fetchall()                   
                        c.execute("UPDATE %s SET chk_number=? WHERE id=?" % table_name,(1, numbers[i])) 
                        conn.commit()
                        conn.close()      
                        self.nameEntries[i]['state'] = 'normal'   
                        self.Entries[i]['state'] = 'normal'   
                        self.links[i]['state'] = 'normal' 
                except:
                    self.label_0 = tk.Label(self, width=35, text='※ONにできません', bg='snow', fg='red')
                    self.label_0.place(x=295, y=27)   
                    self.label_0.after(2000, self.label_0.destroy)    
                try:                                                 
                    if Getvar[i] == '0':    
                        c.execute('select name from url')                           
                        acquire_names = c.fetchall()                    
                        c.execute("UPDATE %s SET chk_number=? WHERE id=?" % table_name,(0, numbers[i]))   
                        conn.commit()
                        conn.close()  
                        self.nameEntries[i]['state'] = 'disable'   
                        self.Entries[i]['state'] = 'disable'   
                        self.links[i]['state'] = 'disable'                      
                except:
                    self.label_0 = tk.Label(self, width=35, text='※OFFにできません', bg='snow', fg='red')
                    self.label_0.place(x=295, y=27)   
                    self.label_0.after(2000, self.label_0.destroy)                                

    def noti_chk(self, event, id):        
        Getvar = []   
        current = self.indexes.index(id)
        conn = sqlite3.connect('url.db')
        c = conn.cursor()
        c.execute('select name from url')
        acquire_names = c.fetchall()        
        for current in range(len(self.indexes)) :
            Getvar.append(self.var[current].get())  
        for i in range(30):            
            if event.widget == self.chks[i]:   
                if Getvar[i] == '(1,)' or Getvar[i] == '1':
                    if acquire_names[i][0] == '' or acquire_names[i][0] == '名前を入力してください':
                        self.label_0 = tk.Label(self, width=35, text='通知OFF', bg='snow', fg='red')
                        self.label_0.place(x=295, y=27)   
                        self.label_0.after(2000, self.label_0.destroy) 
                    else:                        
                        self.label_0 = tk.Label(self, width=35, text='「' + str(acquire_names[i][0]) + '」' '通知OFF', bg='snow', fg='red')
                        self.label_0.place(x=295, y=27)   
                        self.label_0.after(2000, self.label_0.destroy) 
                elif Getvar[i] == '(0,)' or Getvar[i] == '0': 
                    if acquire_names[i][0] == '' or acquire_names[i][0] == '名前を入力してください':
                        self.label_0 = tk.Label(self, width=35, text='通知ON', bg='snow', fg='deep sky blue')
                        self.label_0.place(x=295, y=27)   
                        self.label_0.after(2000, self.label_0.destroy) 
                    else:                                       
                        self.label_0 = tk.Label(self, width=35, text='「' + str(acquire_names[i][0]) + '」' '通知ON', bg='snow', fg='deep sky blue')
                        self.label_0.place(x=295, y=27)   
                        self.label_0.after(2000, self.label_0.destroy)  

    def noti_chk_comits(self, event):
        if event.widget == self.chk_comits:
            if self.var_comits.get() == '(1,)' or self.var_comits.get() =='1':
                self.label_0_comits = tk.Label(self, width=35, text='COMITS通知OFF', bg='snow', fg='red')
                self.label_0_comits.place(x=295, y=27)   
                self.label_0_comits.after(2000, self.label_0_comits.destroy)
            elif self.var_comits.get() == '(0,)' or self.var_comits.get() =='0':
                self.label_0_comits = tk.Label(self, width=35, text='COMITS通知ON', bg='snow', fg='deep sky blue')
                self.label_0_comits.place(x=295, y=27)   
                self.label_0_comits.after(2000, self.label_0_comits.destroy)              

    def keep_chk_comits(self):    
        conn = sqlite3.connect('url.db')
        c = conn.cursor()  
        try:
            if self.var_comits.get() == '1':
                c.execute("UPDATE url SET chk_comits=1 WHERE id=1") 
                conn.commit()
                conn.close()      
        except:
            self.label_1 = tk.Label(self, width=35, text='※ONにできません', bg='snow', fg='red')
            self.label_1.place(x=295, y=27)   
            self.label_1.after(2000, self.label_1.destroy) 
        try:                                            
            if self.var_comits.get() == '0':      
                c.execute("UPDATE url SET chk_comits=0 WHERE id=1")   
                conn.commit()
                conn.close()   
        except:
            self.label_1 = tk.Label(self, width=35, text='※OFFにできません', bg='snow', fg='red')
            self.label_1.place(x=295, y=27)   
            self.label_1.after(2000, self.label_1.destroy)             

    def cursor_delete(self, event):   
        if event.widget.get() == '名前を入力してください':     
            event.widget.delete(0, tk.END)
    def cursor_delete2(self, event):
        if event.widget.get() == 'URLをドラッグ＆ドロップしてください':     
            event.widget.delete(0, tk.END)
    def Enterで保存(self, event):
        self.label_ = tk.Label(self, width=35, text='Enterで保存', bg='snow', fg='deep sky blue')
        self.label_.place(x=295, y=27)   
        self.label_.after(2000, self.label_.destroy)
    def ドラッグアンドドロップで保存(self, evennt):
        self.label_2 = tk.Label(self, width=35, text='ドラッグ＆ドロップで保存', bg='snow', fg='deep sky blue')
        self.label_2.place(x=295, y=27)   
        self.label_2.after(2000, self.label_2.destroy)    
    def URLのリンク(self, event):
        conn = sqlite3.connect('url.db')
        c = conn.cursor()
        c.execute('select name from url')
        acquire_names = c.fetchall()
        for i in range(30):            
            if event.widget == self.links[i]:
                if acquire_names[i][0] == '' or acquire_names[i][0] == '名前を入力してください':
                    self.label_3 = tk.Label(self, width=35, text='URLのリンクです', bg='snow', fg='deep sky blue')
                    self.label_3.place(x=295, y=27) 
                else:
                    if len(acquire_names[i][0]) < 21:
                        self.label_3 = tk.Label(self, width=35, text='「' + str((acquire_names[i][0][0:20])) + '」' + 'のURLのリンクです', bg='snow', fg='deep sky blue')
                        self.label_3.place(x=295, y=27)  
                    else:
                        self.label_3 = tk.Label(self, width=35, text='「' + str((acquire_names[i][0][0:20])) + '...' + '」' + 'のURLのリンクです', bg='snow', fg='deep sky blue')
                        self.label_3.place(x=295, y=27) 
    def URLのリンク2(self, event):
        self.label_3.destroy()                
    def cursor_create(self, event):        
        if not event.widget.get():
            event.widget.insert(tk.END, '名前を入力してください')
    def cursor_create2(self, event):        
        if not event.widget.get():
            event.widget.insert(tk.END, 'URLをドラッグ＆ドロップしてください')            
    def enter_bg_links(self, event):
        event.widget['bg'] = 'thistle2'
    def leave_bg_links(self, event): 
        event.widget['bg'] = 'snow'    
    def snow(self):
        for i in range(30):
            self.Entries[i].config(bg='snow')               
    def link_open(self, event, id):  
        GetEntry = []
        current = self.indexes.index(id)
        for current in range(len(self.indexes)) :
            GetEntry.append(self.Entries[current].get())  
        for i in range(30):
            if event.widget == self.links[i]:
                webbrowser.open(GetEntry[i])                     

    # エントリーウィジェットを作成して配置
    def createEntry(self, next) :  
        def drop(event):
            if event.data.startswith('https://'):
                var_entry.set(event.data)            
            else:
                var_entry.set('https://' + event.data)
        var_entry = tk.StringVar()
        self.name_entry = tk.Entry(self.frame_canvas, width=19, bg='snow', font=('Yu Gothic UI Semibold',9))        
        self.entry = tk.Entry(self.frame_canvas, width=69, textvar=var_entry, bg='snow')
        self.entry.drop_target_register(DND_TEXT)     
        self.name_entry.bind('<Return>', lambda event, id=self.index:self.keep_name(event, id))
        self.entry.dnd_bind('<<Drop>>', drop)                                
        self.entry.dnd_bind('<<Drop>>', lambda event, id=self.index:self.keep_url(event, id), '+')
        self.nameEntries.insert(next, self.name_entry)
        self.Entries.insert(next, self.entry)

        self.links.insert(next, tk.Button(
            self.frame_canvas, 
            text='🔗',
            fg='#33ff33',
            bg='snow',
            bd=0,
            highlightthickness=0,
            font=('Arial Black', 13)
             ))

                                             
        self.chks.insert(next, tk.Checkbutton(
            self.frame_canvas,
            bg='snow',
            activebackground='snow',
            onvalue='1',
            offvalue='0',
            command=lambda id=self.index:self.keep_chk(id)
            ))                  

        self.var.insert(next, tk.StringVar(self.frame_canvas))

        self.nameEntries[next].bind('<FocusIn>', self.cursor_delete)
        self.nameEntries[next].bind('<FocusIn>', self.Enterで保存, '+')
        self.nameEntries[next].bind('<FocusOut>', self.cursor_create)

        self.Entries[next].bind('<FocusIn>', self.cursor_delete2)
        self.Entries[next].bind('<FocusIn>', self.ドラッグアンドドロップで保存, '+')
        self.Entries[next].bind('<FocusOut>', self.cursor_create2)        

        self.links[next].bind('<1>', lambda event, id=self.index:self.link_open(event, id))
        self.links[next].bind('<Enter>', self.enter_bg_links)
        self.links[next].bind('<Enter>', self.URLのリンク, '+')
        self.links[next].bind('<Leave>', self.leave_bg_links)
        self.links[next].bind('<Leave>', self.URLのリンク2, '+')

        self.chks[next].bind('<1>', lambda event, id=self.index:self.noti_chk(event, id))

        self.nameEntries[next].bind("<MouseWheel>", self.mouse_y_scroll)   
        self.Entries[next].bind("<MouseWheel>", self.mouse_y_scroll)   
        self.links[next].bind("<MouseWheel>", self.mouse_y_scroll)   
        self.chks[next].bind("<MouseWheel>", self.mouse_y_scroll)   

        # インデックスマネージャに登録
        self.indexes.insert(next, self.index)

        # 再配置
        self.updateEntries()                     

if __name__ == '__main__' :
    app = App()    
    app.mainloop()      
