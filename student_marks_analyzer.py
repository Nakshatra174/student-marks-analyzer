import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


# ---------------------- FUNCTIONS ----------------------

def analyze_marks():
    try:
        name = entry_name.get()
        roll = entry_roll.get()
        marks_input = entry_marks.get()

        if not name or not roll or not marks_input:
            messagebox.showerror("Error", "Please fill all fields!")
            return

        marks = list(map(int, marks_input.split(",")))

        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)
        percentage = (total / (len(marks) * 100)) * 100

        grade = calculate_grade(average)
        result = check_result(marks)

        report = (
            f"Student Name: {name}\n"
            f"Roll Number: {roll}\n\n"
            f"Total Marks: {total}\n"
            f"Average: {average:.2f}\n"
            f"Highest: {highest}\n"
            f"Lowest: {lowest}\n"
            f"Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}\n"
            f"Result: {result}"
        )

        output_text.set(report)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter marks separated by commas (e.g., 75,80,65)")


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def check_result(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"
    return "Pass"


def show_graph():
    try:
        marks_input = entry_marks.get()

        if not marks_input:
            messagebox.showerror("Error", "Please enter marks first!")
            return

        marks = list(map(int, marks_input.split(",")))
        subjects = [f"Sub {i+1}" for i in range(len(marks))]

        plt.figure(figsize=(6, 4))
        plt.bar(subjects, marks)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title("Student Marks Graph")
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter marks separated by commas!")


def save_report():
    try:
        name = entry_name.get()
        roll = entry_roll.get()
        marks_input = entry_marks.get()

        if not name or not roll or not marks_input:
            messagebox.showerror("Error", "Please fill all fields first!")
            return

        marks = list(map(int, marks_input.split(",")))

        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)
        percentage = (total / (len(marks) * 100)) * 100

        grade = calculate_grade(average)
        result = check_result(marks)

        filename = f"{name}_Report.txt"

        with open(filename, "w") as file:
            file.write("----- Student Report -----\n\n")
            file.write(f"Student Name: {name}\n")
            file.write(f"Roll Number: {roll}\n\n")
            file.write(f"Marks: {marks}\n")
            file.write(f"Total: {total}\n")
            file.write(f"Average: {average:.2f}\n")
            file.write(f"Highest: {highest}\n")
            file.write(f"Lowest: {lowest}\n")
            file.write(f"Percentage: {percentage:.2f}%\n")
            file.write(f"Grade: {grade}\n")
            file.write(f"Result: {result}\n")

        messagebox.showinfo("Success", f"Report successfully saved!\nFile: {filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_marks.delete(0, tk.END)
    output_text.set("")


# ---------------------- GUI SETUP ----------------------

root = tk.Tk()
root.title("Student Marks Analyzer")
root.geometry("520x600")
root.configure(bg="#eef2f3")

title = tk.Label(
    root,
    text="Student Marks Analyzer",
    font=("Arial", 18, "bold"),
    bg="#eef2f3",
    fg="#333"
)
title.pack(pady=15)

input_frame = tk.Frame(root, bg="#eef2f3")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Student Name:", bg="#eef2f3").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(input_frame, width=35)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Roll Number:", bg="#eef2f3").grid(row=1, column=0, sticky="w", pady=5)
entry_roll = tk.Entry(input_frame, width=35)
entry_roll.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Enter marks (comma separated):", bg="#eef2f3").grid(row=2, column=0, sticky="w", pady=5)
entry_marks = tk.Entry(input_frame, width=35)
entry_marks.grid(row=2, column=1, pady=5)

button_frame = tk.Frame(root, bg="#eef2f3")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Analyze", command=analyze_marks,
          bg="#4CAF50", fg="white", width=15, height=2).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Clear", command=clear_fields,
          bg="#f44336", fg="white", width=15, height=2).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Show Graph", command=show_graph,
          bg="#2196F3", fg="white", width=15, height=2).grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Save Report", command=save_report,
          bg="#9C27B0", fg="white", width=15, height=2).grid(row=2, column=0, columnspan=2, pady=5)

output_text = tk.StringVar()

output_label = tk.Label(
    root,
    textvariable=output_text,
    bg="#eef2f3",
    justify="left",
    font=("Arial", 11)
)
output_label.pack(pady=15)

root.mainloop()