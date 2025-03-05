import tkinter as tk
import re
from tkinter import *
from tkinter import messagebox

class Converter:
    def __init__(self):
        # main window setup
        self.window = tk.Tk()
        self.window.title = "Binary Converter"
        self.window.config(background="white")

        # text showing conversion state app currently in
        self.state_text = tk.Message(text="*converting from digits to binary",font=("Aerial",10),width=200,bg="#9090C0",fg="black")
        self.state_text.pack(padx=10,pady=5)

        # input box for desired conversion values to be inputted within
        self.entry_box = tk.Entry(self.window,font=("Aerial",10))
        self.entry_box.pack(padx=10,pady=10)

        # enter button
        self.button = tk.Button(text="enter value",bg="#36454F",fg="lightgray",activebackground="black",activeforeground="white",command=self.conv_call)
        self.button.pack(padx=20,pady=20)

        self.check_state = tk.IntVar()
        
        # check box for switching of converter states
        self.check = tk.Checkbutton(text="integer converter/binary converter",font=("Aerial",8),bg="white",activebackground="black",activeforeground="white",variable=self.check_state,command=self.conversion_state)
        self.check.pack(padx=10,pady=10)


        self.window.mainloop()



    def int_conv(self):
        try:
            binary_conv = ""
            inputted_int_value = int(self.entry_box.get())

            # converting inputted value into binary and showing user
            while inputted_int_value > 0:
                remainder = inputted_int_value % 2
                binary_conv = str(remainder) + binary_conv
                inputted_int_value = inputted_int_value // 2
            messagebox.showinfo(title="Conversion",message="The binary conversion of the inputted integer is " + binary_conv)

        # error case handling in case of any non integer value passed
        except ValueError:
            messagebox.showinfo(title="Value Error Has Occured",message="Please input an integer or integers")

    
    def bin_conv(self):
        inputted_bin_value = str(self.entry_box.get())

        # converting inputted value into integer using the RE fullmatch function and showing to user
        if bool(re.fullmatch(r"[01]+", inputted_bin_value)) == True:
            integer_conv = int(inputted_bin_value,2)
            messagebox.showinfo(title="Conversion",message="The integer conversion of the inputted binary sequence is " + str(integer_conv))

        # handling scenerio of no value or non binary value being passed
        else:
            messagebox.showinfo(title="Value Error Has Occured",message="Please input a binary sequence")



    def conv_call(self):
        # making a function to (when button clicked) call and check both binary and integer conversion functions
        if self.check_state.get() == 0:
            self.int_conv()
        if self.check_state.get() == 1:
            self.bin_conv()



    def conversion_state(self):
        if self.check_state.get() == 1:
            # when check pressed, switching conversion state to binary - integer
            self.window.config(background="black")
            self.check.config(bg="black",fg="white",activebackground="white",activeforeground="black")
            self.state_text.config(text="*converting from binary to integers",bg=("#2A3439"),fg="white")
            self.button.config(bg="#E5E4E2",fg="#36454F",activebackground="white",activeforeground="black",)
        if self.check_state.get() == 0:
            # when check unpressed, switching conversion state to integer - binary
            self.window.config(background="white")
            self.check.config(bg="white",fg="black",activebackground="black",activeforeground="white")
            self.state_text.config(text="*converting from integers to binary",bg="#9090C0",fg="black")
            self.button.config(bg="#36454F",fg="lightgray",activebackground="black",activeforeground="white",)

        

window = Converter()