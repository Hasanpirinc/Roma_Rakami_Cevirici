import tkinter as tk

# Roma rakamları ve karşılık geldiği sayılar
roma_rakamlari = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roma_to_arabic(roma):
    """
    Roma rakamlarını Arabic integer'a çeviren fonksiyon
    """
    total = 0
    prev_value = 0
    for rakam in reversed(roma):
        value = roma_rakamlari.get(rakam, None)
        if value is None:
            return "Hatalı Roma rakamı"
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def convert_and_display():
    roma = entry.get().upper()
    arabic = roma_to_arabic(roma)
    result_label.config(text=str(arabic))

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("Roma Rakamı Dönüştürücü")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Roma Rakamı:")
label.grid(row=0, column=0, sticky="e")

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

convert_button = tk.Button(frame, text="Çevir", command=convert_and_display)
convert_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=1, columnspan=3, pady=10)

root.mainloop()
