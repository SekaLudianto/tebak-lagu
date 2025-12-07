import os

# folder saat ini
folder_path = os.getcwd()
output_file = "daftar.txt"

# ambil semua file .json di folder ini
files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

# tulis ke daftar.txt
with open(output_file, "w", encoding="utf-8") as out:
    for f in files:
        out.write(f + "\n")

print(f"Berhasil membuat {output_file} dengan {len(files)} file.")
