import sympy as sp

x = sp.Symbol('x')


def hitung_turunan(soal):
    fungsi = sp.sympify(soal)
    turunan = sp.diff(fungsi, x)

    return fungsi, turunan


print("=== DERIVATIVE CALCULATOR ===")

soal = input("Masukkan fungsi f(x): ")

try:
    fungsi, turunan = hitung_turunan(soal)

    print()
    print("Fungsi  :", fungsi)
    print("Turunan :", turunan)

except Exception:
    print()
    print("Input tidak valid!")
    print("Pastikan format fungsi sudah benar.")