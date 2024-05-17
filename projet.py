import subprocess
import webbrowser
import time
import tkinter as tk
from tkinter import messagebox

def install_package(package):
    try:
        subprocess.check_call(['pip', 'install', package])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while installing {package}: {str(e)}")

def start_notebook():
    notebook_path = 'CNN.ipynb'
    
    try:
        subprocess.Popen(['jupyter', 'notebook', notebook_path])
        time.sleep(5)  # Attendre 5 secondes pour que le serveur Jupyter démarre
        webbrowser.open(f'http://localhost:8888/notebooks/{notebook_path}')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_styled_button(master, text, command):
    button = tk.Button(master, text=text, command=command, 
                       bg='#f5f5f5', fg='#333333', 
                       activebackground='#e7e7e7', activeforeground='#000000', 
                       relief='flat', font=('Helvetica', 10, 'bold'),
                       padx=10, pady=5)
    button.pack(pady=20, ipadx=10, ipady=5)
    return button

# Installation des bibliothèques nécessaires
packages_to_install = ['notebook', 'keras', 'tensorflow', 'utils']
for package in packages_to_install:
    install_package(package)

# Creation de la fenetre principale
root = tk.Tk()
root.title("Notebook Launcher")

# Taille de la fenetre
root.geometry('300x200')

title_label = tk.Label(root, text="Jupyter Notebook Launcher", 
                       bg='#f5f5f5', fg='#333333', 
                       font=('Helvetica', 14, 'bold'))
title_label.pack(pady=20)

start_button = create_styled_button(root, "Start Notebook", start_notebook)

root.configure(bg='#f5f5f5')

root.mainloop()

