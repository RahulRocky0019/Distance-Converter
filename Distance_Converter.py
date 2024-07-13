import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    km = entry_val.get()
    print(f"Km: {km}")

    miles = km * 0.621371
    print(f"Miles: {miles}\n")
    output_val.set(f"{miles} miles")


# Title
window = tk.Tk()
# window = ttk.Window(themename="flatly")
window.title("Distance Converter")
window.geometry("300x150")


title_lable = ttk.Label(window, text="Kilometer to Miles", font=("Calibri", 24, "bold"))
title_lable.pack()

# Input
input_field = ttk.Frame(window)
entry_val = tk.DoubleVar()
entry = ttk.Entry(input_field, textvariable=entry_val)
button = ttk.Button(input_field, text="Convert", command=convert)
entry.pack(side="left", padx=5)
button.pack(side="left", padx=5)
input_field.pack(pady=10)

# Output
output_val = tk.StringVar()
output_label = ttk.Label(
    window, text="Output", font=("Calibri", 24), textvariable=output_val
)
output_label.pack()

# Run
window.mainloop()
