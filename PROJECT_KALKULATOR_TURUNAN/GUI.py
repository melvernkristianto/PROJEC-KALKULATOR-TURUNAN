import tkinter as tk
from tkinter import messagebox
import sympy as sp

x = sp.Symbol('x')

# tes 123
def hitung_turunan():
    soal = input_fungsi.get()

    try:
        fungsi = sp.sympify(soal)
        turunan = sp.diff(fungsi, x)

        hasil.config(text=f"f'(x) = {turunan}")

    except Exception:
        messagebox.showerror(
            "Error",
            "Fungsi yang dimasukkan tidak valid."
        )


# Membuat window
window = tk.Tk()
window.title("Derivative Calculator")
window.geometry("500x350")


# Judul
judul = tk.Label(
    window,
    text="Derivative Calculator",
    font=("Arial", 20, "bold")
)
judul.pack(pady=20)


# Label input
label_input = tk.Label(
    window,
    text="Masukkan fungsi f(x):",
    font=("Arial", 12)
)
label_input.pack()


# Input
input_fungsi = tk.Entry(
    window,
    width=40,
    font=("Arial", 12)
)
input_fungsi.pack(pady=10)


# Tombol
tombol = tk.Button(
    window,
    text="HITUNG TURUNAN",
    command=hitung_turunan
)
tombol.pack(pady=10)


# Hasil
hasil = tk.Label(
    window,
    text="f'(x) = ",
    font=("Arial", 16, "bold")
)
hasil.pack(pady=20)


# Menjalankan aplikasi
window.mainloop()