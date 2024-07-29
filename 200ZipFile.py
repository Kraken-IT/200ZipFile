import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def create_zip_from_folder(source_folder, destination_folder, base_zip_name='archive', num_files_per_zip=200):
    source_files = os.listdir(source_folder)
    zip_count = 0

    for i in range(0, len(source_files), num_files_per_zip):
        zip_count += 1
        zip_files = source_files[i:i + num_files_per_zip]
        zip_name = f'{base_zip_name}_{zip_count}.zip'
        zip_path = os.path.join(destination_folder, zip_name)

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_name in zip_files:
                file_path = os.path.join(source_folder, file_name)
                if os.path.isfile(file_path):  # Проверяем, является ли путь файлом
                    zipf.write(file_path, arcname=file_name)

        print(f'Created zip archive {zip_path} with {len(zip_files)} files.')
    
    messagebox.showinfo("Success", f"Created {zip_count} zip archives in {destination_folder}")

def select_source_folder():
    folder = filedialog.askdirectory()
    if folder:
        source_folder_var.set(folder)

def select_destination_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_folder_var.set(folder)

def start_zipping():
    source_folder = source_folder_var.get()
    destination_folder = destination_folder_var.get()
    
    if not source_folder or not destination_folder:
        messagebox.showwarning("Warning", "Please select both source and destination folders.")
        return
    
    create_zip_from_folder(source_folder, destination_folder)

# Создание основного окна
root = tk.Tk()
root.title("Zip File Creator")

source_folder_var = tk.StringVar()
destination_folder_var = tk.StringVar()

# Создание и размещение виджетов
tk.Label(root, text="Source Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=source_folder_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Destination Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=destination_folder_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Create Zip", command=start_zipping).grid(row=2, column=0, columnspan=3, pady=20)

# Подпись Kraken-IT
tk.Label(root, text="Kraken-IT", font=("Arial", 10)).grid(row=3, column=0, columnspan=3, pady=10)

# Запуск основного цикла приложения
root.mainloop()
