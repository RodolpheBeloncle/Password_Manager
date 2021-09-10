from tkinter import *
from tkinter import messagebox
import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # list comprehension
    password_list = [random.choice(letters) for char1 in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char2 in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char3 in range(random.randint(2, 4))]

    random.shuffle(password_list)
    print(password_list)
    password_input.insert(0,"".join(password_list))



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    data_webSite = website_input.get()
    data_userName = userName_input.get()
    data_password = password_input.get()


    if len(data_webSite) == 0  or len(data_password) == 0:
        messagebox.showinfo(title=data_webSite, message="you should not leave filed empty")


    else:
        message = "Save it ?"
        is_ok = messagebox.askokcancel(title=data_webSite, message=message)
        if is_ok:
            print(website_input.get())
            print(userName_input.get())
            print(password_input.get())

            website_input.delete(0,END)
            userName_input.delete(0, END)
            password_input.delete(0, END)
            data_file = open("data.txt","a")
            data_file.write(f"web site : {data_webSite},\nuser name / email : {data_userName},\npassword : {data_password}\n")
            data_file.write("-------------NEXT DATA------------------\n")
            data_file.close()
# ---------------------------- UI SETUP ------------------------------- #

# set window
window = Tk()
window.minsize(width=200,height=200)
window.config(padx=200,pady=200)
window.title("Password Manager")

# set image
canvas = Canvas(width=200,height=200)
padlok_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=padlok_image)
canvas.grid(column=1,row=2)

# set Labels

website_label = Label(text="Website")
website_label.grid(column=0,row=3)

email_username_label = Label(text="Email/Username")
email_username_label .grid(column=0,row=4)


password_label = Label(text="Password")
password_label.grid(column=0,row=5)

# User Input
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1,row=3,columnspan=2)

userName_input = Entry(width=35)
userName_input.grid(column=1,row=4,columnspan=2)
userName_input.insert(0,"youremail@gmail.com")

password_input = Entry(width=20)
password_input.grid(column=1,row=5)



# Set button add & generate password

gen_password_button = Button(text="Generate Password",width=14,command=generate_password)
gen_password_button.grid(column=2,row=5,columnspan=1)

add_button = Button(text="Add",width=15,command=save)
add_button.grid(column=1,row=6,columnspan=2,pady=10)


window.mainloop()