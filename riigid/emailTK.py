import tkinter as tk
from tkinter import BUTT, W, E, N, S, messagebox, filedialog
from email.message import EmailMessage
import smtplib, ssl, imghdr, os
from click import command, password_option
def image_add():
    global file
    file=filedialog.askopenfilename()
    label_lisa3.configure(text=file)
def email():
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'testemail@test.com'
    #####https://myaccount.google.com/apppasswords
    password = 'efok fdxj odek tylm'
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(entry_kiri_var)
    msg['Subject'] = entry_teema_var
    msg['From'] = sender_email
    msg['To'] = entry_email_var
    if "file" in globals():
        with open(file, 'rb') as fpilt:
            pilt=fpilt.read()
        msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo('Kiri oli saadetud')
        print('Sent')
        write_to_db(entry_email_var, entry_teema_var, entry_kiri_var)
    except Exception as e:
        print('Error:', e)
def start():
    get_data_entry()
    for x in range(len(entry_email_var)):
        if entry_email_var[x] == ',':
            entry_email_var.split(',')
    delite_entry()
    email()
def write_to_file():
    with open(r'C:\Users\ravil\source\repos\Python-easy-mode\riigid\exit.txt', "w", encoding="utf-8") as f:
        TempVariable = f'{entry_email.get()}◆{entry_teema.get()}◇{entry_kiri.get("1.0", tk.END)}'
        f.write(TempVariable)
def read_from_file():
    file = r'C:\Users\ravil\source\repos\Python-easy-mode\riigid\exit.txt'
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()
        n1 = data.find('◆')
        n2 = data.find('◇')
        entry_email_var, entry_teema_var, entry_kiri_var = data[0:n1].strip(), data[n1+1:n2].strip(), data[n2+1:len(data)].strip()
        #return entry_email_var, entry_teema_var, entry_kiri_var
def before_start():
    global entry_email_var, entry_teema_var, entry_kiri_var
    file_path = r'C:\Users\ravil\source\repos\Python-easy-mode\riigid\exit.txt'
    if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
        TrueOrFalse = messagebox.askyesno("A draft has been found", "Would you like to use a draft?")
        if TrueOrFalse == True:
            read_from_file()
        # print(entry_email_var, entry_teema_var, entry_kiri_var, 'before_start')
    # else:
    #     global entry_email_var, entry_teema_var, entry_kiri_var
def erase_file():
    with open(r'C:\Users\ravil\source\repos\Python-easy-mode\riigid\exit.txt', 'w', encoding="utf-8") as eracefile:
        pass
def on_exit():
    # entry_email_var, entry_teema_var, entry_kiri_var = None
    if len(entry_email_var) != 1 and len(entry_teema_var) != 1 and len(entry_kiri_var) != 1:
        write_to_file()
    window.destroy()
def get_data_entry():
    global entry_email_var, entry_teema_var, entry_kiri_var
    entry_email_var = entry_email.get()
    entry_teema_var = entry_teema.get()
    entry_kiri_var = entry_kiri.get(1.0, tk.END)
def delite_entry():
    entry_email.delete(0, tk.END)
    entry_teema.delete(0, tk.END)
    entry_kiri.delete("1.0", tk.END)
    if "file" in globals():
        label_lisa3.configure(text='...')
    if 'entry_email_var' in globals() or 'entry_teema_var' in globals() or 'entry_kiri_var' in globals():
        erase_file()
#global entry_email_var, entry_teema_var, entry_kiri_var
def WindowTK():
    global window, label_email, label_teema, label_lisa, entry_email, entry_teema, label_lisa3, entry_kiri, label_kiri, button_lisa, button_saada, entry_email_var, entry_teema_var, entry_kiri_var
    entry_email_var, entry_teema_var, entry_kiri_var = '', '', ''
    window = tk.Tk()
    window.geometry('600x650')
    window.resizable(False, False)
    window.title('E-mail sender')
    window.protocol("WM_DELETE_WINDOW", on_exit)
    label_email = tk.Label(window, text='EMAIL: ', font=('Arial',20,'bold'), bg='green', fg='white')
    label_teema = tk.Label(window, text='TEEMA: ', font=('Arial',20,'bold'), bg='green', fg='white')
    label_lisa = tk.Label(window, text='LISA: ', font=('Arial',20,'bold'), bg='green', fg='white')
    entry_email = tk.Entry(window, bg='lightgreen', font=('Arial',15,'bold'))
    entry_email.insert(0, globals().get('entry_email_var', entry_email_var))
    entry_teema = tk.Entry(window, bg='lightgreen', font=('Arial',15,'bold'))
    entry_teema.insert(0, globals().get('entry_teema_var', entry_teema_var))
    label_lisa3 = tk.Label(window, text='...', font=('Arial',10,'bold'), bg='lightgreen', fg='white')
    entry_kiri = tk.Text(window, bg='lightgreen', font='Arial 10', width=40)
    entry_kiri.insert("1.0", globals().get('entry_kiri_var', entry_kiri_var))
    label_kiri = tk.Label(window, text='Kiri', font=('Arial',20,'bold'), bg='green', fg='white')
    button_lisa = tk.Button(window, text='LISA PILT', font=('Arial', 15, 'bold'), command=image_add)
    button_saada = tk.Button(window, text='SAADA', font=('Arial', 15, 'bold'), command=start)
    button_precheck = tk.Button(window, text='eelvaade', font=('Arial', 15, 'bold'), command=eelvade)
    button_signature = tk.Button(window, text='Allkirja', font=('Arial', 15, 'bold'), command=ajalkiri)
    button_puhasta = tk.Button(window, text='Puhasta', font=('Arial', 15, 'bold'), command=delite_entry)
    label_email.grid(row=0, column=0, sticky=W+E+N+S)
    label_teema.grid(row=1, column=0, sticky=W+E+N+S)
    label_lisa.grid(row=2, column=0, sticky=W+E+N+S)
    entry_email.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
    entry_teema.grid(row=1, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
    label_lisa3.grid(row=2, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
    label_kiri.grid(row=4, column=0, padx = 20, sticky=W)
    entry_kiri.grid(row=3, column=1, columnspan=5, rowspan=2, sticky=W+E+N+S, padx = 20)
    button_lisa.grid(row=8, column=1, padx = 20)
    button_saada.grid(row=8, column=2)
    button_precheck.grid(row=8, column=0)
    button_signature.grid(row=8, column=3)
    button_puhasta.grid(row=9, column=0)
    window.mainloop()

def eelvade():
    get_data_entry()
    info = f"""    Saatja: testemail@test.com
    Saaja: {entry_email_var}
    Teema: {entry_teema_var}
    Kiri: {entry_kiri_var}"""
    messagebox.showinfo("eelvade", info)

def ajalkiri():
    entry_kiri.insert("end", 'Saadetud testi e-mail.')
def write_to_db(entry_email_var, entry_teema_var, entry_kiri_var):
    with open(r'C:\Users\ravil\source\repos\Python-easy-mode\riigid\exit.txt', "w", encoding="utf-8") as f:
        TempVariable = f'{entry_email_var}◆{entry_teema_var}◇{entry_kiri_var}'
        f.write(TempVariable)