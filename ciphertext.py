import tkinter as tk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        char_code = (ord(char) + shift) % 256
        result += chr(char_code)
    return result

def caesar_decipher(text, shift):
    result = ""
    for char in text:
        char_code = (ord(char) - shift) % 256
        result += chr(char_code)
    return result

def encrypt():
    plaintext = plaintext_text.get()
    shift = int(shift_entry.get())
    ciphertext = caesar_cipher(plaintext, shift)
    result_text.set(ciphertext)

def decrypt():
    ciphertext_text = tk.StringVar()
    ciphertext = ciphertext_text.get()
    shift = int(shift_entry.get())
    plaintext = caesar_decipher(ciphertext, shift)
    result_text.set(plaintext)

app = tk.Tk()
app.title("Caesar Cipher")

plaintext_label = tk.Label(app, text="Ketik Plaintext atau Ciphertext:")
plaintext_label.pack()

plaintext_text = tk.StringVar()
plaintext_entry = tk.Entry(app, textvariable=plaintext_text, width=40)
plaintext_entry.pack()
plaintext_entry.config(bg="yellow")

shift_label = tk.Label(app, text="Jumlah Pergeseran:")
shift_label.pack()

shift_entry = tk.Entry(app, width=40)
shift_entry.pack()
shift_entry.config(bg="yellow")

encode_button = tk.Button(app, text="Encode Caesar Cipher", command=encrypt, bg="blue")
encode_button.pack(side="left")

decode_button = tk.Button(app, text="Decode Caesar Cipher", command=decrypt, bg="red")
decode_button.pack(side="right")

result_text = tk.StringVar()
result_label = tk.Label(app, text="Hasil:")
result_label.pack()

result_entry = tk.Entry(app, textvariable=result_text, state="readonly", width=40 )
result_entry.pack()

app.mainloop()