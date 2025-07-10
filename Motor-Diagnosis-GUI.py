# motor_diagnosis_gui.py
# Created by Aymen Amour Dit Zerrouk - Open Source GUI Diagnostic Tool

import tkinter as tk
from tkinter import messagebox

def diagnose_motor(temp, vibration, current):
    issues = []

    if temp > 80:
        issues.append("🚨 High temperature detected!")
    elif temp > 60:
        issues.append("⚠️ Temperature nearing safety limit.")

    if vibration > 6.0:
        issues.append("🚨 Abnormal vibration level!")
    elif vibration > 4.0:
        issues.append("⚠️ Slightly high vibration.")

    if current > 15:
        issues.append("🚨 Overcurrent detected!")
    elif current > 12:
        issues.append("⚠️ Current is approaching the upper threshold.")

    if not issues:
        return "✅ The motor is in good condition."
    else:
        return "\n".join(issues)

def on_diagnose():
    try:
        temp = float(entry_temp.get())
        vib = float(entry_vib.get())
        curr = float(entry_curr.get())
        result = diagnose_motor(temp, vib, curr)
        messagebox.showinfo("Diagnosis Report", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Electric Motor Diagnosis System")
root.geometry("400x300")
root.configure(bg="#f9f9f9")

tk.Label(root, text="Temperature (°C):", bg="#f9f9f9").pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack()

tk.Label(root, text="Vibration (mm/s):", bg="#f9f9f9").pack(pady=5)
entry_vib = tk.Entry(root)
entry_vib.pack()

tk.Label(root, text="Current (A):", bg="#f9f9f9").pack(pady=5)
entry_curr = tk.Entry(root)
entry_curr.pack()

tk.Button(root, text="Diagnose", command=on_diagnose, bg="#2196F3", fg="white", padx=10, pady=5).pack(pady=20)

tk.Label(root, text="© Aymen Amour Dit Zerrouk - Open Source", font=("Arial", 8), bg="#f9f9f9").pack(side="bottom", pady=5)

root.mainloop()
