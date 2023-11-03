from tkinter import *
from tkinter import messagebox
import gtts
import playsound

def create_welcome_audio():
    text = 'Welcome! You have successfully logged in this page'
    sound = gtts.gTTS(text, lang='en')
    sound.save('welcome.mp3')

def validate_login():
    username = entry1.get()
    password = entry2.get()

    if username == '' or password == '':
        messagebox.showerror('Login', 'Fill in all the required information')
    else:
        if not username.replace(" ", "").isalpha():
            messagebox.showerror('Login', 'Username should contain only alphabets.')
        else:
            min_length = 8
            has_letter = False
            has_digit = False
            has_symbol = False
            for char in password:
                if char.isalpha():
                    has_letter = True
                elif char.isdigit():
                    has_digit = True
                elif not char.isalnum():
                    has_symbol = True
            if len(password) <= min_length or not (has_letter and has_digit and has_symbol):
                messagebox.showerror('Login', 'Password should contain alphabets, symbols, and digits.')
            else:
                messagebox.showinfo('Login', 'Login successful!')
                playsound.playsound('welcome.mp3')
                clear_entry_fields()

def clear_entry_fields():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

def create_login_page():
    root = Tk()
    root.config(bg='#333333')
    root.title('Login Page')

    label1 = Label(root, text='Login Page', bg='cyan4', fg='cyan', font=('Arial', 24))
    label1.place(x=500, y=20)

    label2 = Label(root, text='UserName:', font=('Arial', 20), bg='cyan4', fg='white')
    label2.place(x=310, y=190)

    label3 = Label(root, text='Password:', font=('Arial', 20), bg='cyan4', fg='white')
    label3.place(x=310, y=340)

    global entry1
    global entry2
    entry1 = Entry(root, font=('Arial', 15))
    entry1.place(x=600, y=200)

    entry2 = Entry(root, font=('Arial', 15), show='*')
    entry2.place(x=600, y=350)

    button = Button(root, text='Login', bg='cyan3', font=('Arial', 15), bd=5, command=validate_login)
    button.place(x=600, y=500)

    root.mainloop()

if __name__ == '__main__':
    create_welcome_audio()
    create_login_page()
