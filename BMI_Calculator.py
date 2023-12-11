import tkinter as tk
from tkinter import Label, Entry, Button

def calculate_bmi(weight, height):
    bmi = weight/(height**2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_and_display_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values for weight and height.")
        return

    if weight <= 0 or height <= 0:
        result_label.config(text="Weight and height must be positive values.")
        return

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    result_label.config(text=f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}")

#For the GUI
root = tk.Tk()
root.geometry("350x220")
root.title("BMI Calculator")
# Set background color for the main window
root.configure(bg="#e6e6e6")
# Creating widgets with background color
weight_label = Label(root, text="Enter your weight (kg):", bg="#e6e6f6")
weight_label.pack(pady=5)
weight_entry = Entry(root, bg="white")
weight_entry.pack(pady=5)

height_label = Label(root, text="Enter your height (m):", bg="#e6e6f6")
height_label.pack(pady=5)
height_entry = Entry(root, bg="white")
height_entry.pack(pady=5)

calculate_button = Button(root, text="Calculate BMI", command=calculate_and_display_bmi, bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

result_label = Label(root, text="", bg="#e6e6e6")
result_label.pack(pady=10)
root.mainloop()