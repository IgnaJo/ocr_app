# gui/app_window.py

import customtkinter as ctk
from tkinter import filedialog
from services.file_handler import process_files
import os

class AppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.last_directory = os.getcwd()

        self.title("OCR Renamer App")
        self.geometry("600x600")
        ctk.set_appearance_mode("System")

        self.label = ctk.CTkLabel(self, text="Procesamiento de Documentos PDF", font=ctk.CTkFont(size=18, weight="bold"))
        self.label.pack(pady=20)

       
        
        self.input_dir = ctk.StringVar()
        self.output_dir = ctk.StringVar()
        
        #campo para mostrar ruta de carpeta
        self.input_entry = ctk.CTkEntry(self, textvariable=self.input_dir, width=300, state="readonly")
        self.input_entry.pack(pady=20, padx=20)
        self.browse_button = ctk.CTkButton(self, text="Buscar Carpeta con documentos", command=lambda: self.browse_folder("input"))
        self.browse_button.pack(pady=10)
        
        
        #campo para mostrar rura de carpeta de salida
        self.output_dentry = ctk.CTkEntry(self, textvariable=self.output_dir, width=300, state="readonly")
        self.output_dentry.pack(pady=20, padx=20)        
        self.browse_output_button = ctk.CTkButton(self, text="Seleccionar Carpeta de Salida", command=lambda: self.browse_folder("output"))
        self.browse_output_button.pack(pady=10)
        
        
        self.process_button = ctk.CTkButton(self, text="Iniciar Proceso", command=self.run_process)
        self.process_button.pack(pady=10)

        self.log_output = ctk.CTkTextbox(self, width=550, height=250, font=("Courier", 11))
        self.log_output.pack(pady=10)
        
    
    def browse_folder(self, target):
        folder_path = filedialog.askdirectory(initialdir=self.last_directory)
        if folder_path:
            if target == "input":
                self.input_dir.set(folder_path)
            elif target == "output":
                self.output_dir.set(folder_path)
            
        

    def run_process(self):
        
        input_path = self.input_dir.get()
        output_path = self.output_dir.get()
        if not input_path or not output_path:
            self.log_output.insert("end", "[ERROR] Debe seleccionar las carpetas de entrada y salida.\n")
            self.log_output.see("end")
            return
        
        
        self.log_output.insert("end", "[INFO] Iniciando procesamiento...\n")
        self.log_output.see("end")

        try:
            process_files(
                input_dir=self.input_dir.get(),
                output_dir=self.output_dir.get(),
                logger=lambda msg: self.log_output.insert("end", f"[LOG] {msg}\n")
            )
            self.log_output.insert("end", "[OK] Procesamiento completado.\n")
        except Exception as e:
            self.log_output.insert("end", f"[ERROR] {str(e)}\n")

        self.log_output.see("end")
