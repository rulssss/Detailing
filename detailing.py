import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functions import *


def mostrar_todos_datos():
    # Función que mostrará todos los datos
    c = 0
    all_data = traer_todos_losdatos()
    if all_data:
        result_text.config(state="normal", font=("Segoe UI", 16))  # Habilitar edición temporalmente
        result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto
        result_text.insert(tk.END, "client,year,month,job,car,amount,cost\n")

        for i in all_data:
            new_text = f"{i}\n"  # Añade el nuevo dato
            result_text.insert(tk.END, new_text)  # Acumula los datos en el texto
        
        result_text.config(state="disabled")  # Deshabilitar edición
    else:
        result_text.config(state="normal", font=("Segoe UI", 20))  # Habilitar edición temporalmente
        result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto
        result_text.insert(tk.END, "No hay datos para mostrar.")
        result_text.config(state="disabled")  # Deshabilitar edición
            



def cargar_datos(txt):
    result_text.config(state="normal")  # Habilitar edición temporalmente
    result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto
    result_text.config(state="disabled")  # Deshabilitar edición
    
    load_data(txt)

    text_box.delete("1.0", tk.END)  # Borrar el contenido del cuadro de texto
    
    global texto_ingresado
    texto_ingresado = "" # resetea la variable cn el texto 
    
    


def buscar_datos():
    result_text.config(state="normal", font=("Segoe UI", 30))  # Habilitar edición temporalmente
    result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto
    result_text.config(state="disabled")  # Deshabilitar edición
    
    top = tk.Toplevel()
    top.title("Buscar Datos")
    top.configure(bg="white")
    top.geometry("400x250")

    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    x = (screen_width - 400) // 2
    y = (screen_height - 250) // 2

    top.geometry(f"400x250+{x}+{y}")

    label = tk.Label(top, text="Ingresa el número del mes (1-12):", bg="white", font=("Segoe UI", 16))
    label.pack(padx=10, pady=(20, 10))

    entry = tk.Entry(top, font=("Segoe UI", 16), bg="#d7d7d7")
    entry.pack(padx=10, pady=10)

    def on_submit():
        try:
            mes = int(entry.get())
            if 1 <= mes <= 12:
                total_a = total_amount(mes)
                total_c = total_cost(mes)

                result_text.config(state="normal")  # Habilitar edición temporalmente
                if total_a[0] is None:
                    result_text.insert(tk.END, f"No se realizaron trabajos en el mes {mes}.")
                else:
                    diff = total_a[0] - total_c[0]
                    result_text.insert(tk.END, f"Mes: {mes}\nMonto total: {total_a[0]}\nCosto total: {total_c[0]}\nDiferencia (monto-costo): {diff}\n")
                result_text.config(state="disabled")  # Deshabilitar edición
                top.destroy()
            else:
                messagebox.showwarning("Entrada inválida", "Por favor, ingresa un número de mes válido (1-12).")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Por favor, ingresa un número válido.")

    button_frame = tk.Frame(top, bg="white")
    button_frame.pack(pady=20)

    submit_button = tk.Button(button_frame, text="Buscar", command=on_submit, width=12, relief="flat", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
    submit_button.pack(side=tk.LEFT, padx=10)

    cancel_button = tk.Button(button_frame, text="Cancelar", command=top.destroy, width=12, relief="flat", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
    cancel_button.pack(side=tk.LEFT, padx=10)

    top.transient(ventana)
    top.grab_set()
    ventana.wait_window(top)


def borrar_datos():
    clear_data()
    result_text.config(state="normal", font=("Segoe UI", 20))  # Habilitar edición temporalmente
    result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto
    result_text.insert(tk.END, "Datos Borrados.")
    result_text.config(state="disabled")  # Deshabilitar edición


def actualizar_texto(event):
    global texto_ingresado
    texto_ingresado = text_box.get("1.0", tk.END).strip()


ventana = tk.Tk()
ventana.title("Gestión de Datos")
ventana.state('zoomed')

style = ttk.Style()
style.configure("TNotebook.Tab", font=("Segoe UI", 12))

frame_width = 200

notebook = ttk.Notebook(ventana, style="TNotebook")
notebook.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

frame_buscar = tk.Frame(notebook, width=frame_width, padx=10, pady=10, bd=2, relief="groove")
notebook.add(frame_buscar, text="Buscar datos")
frame_buscar.pack_propagate(False)

label_buscar = tk.Label(frame_buscar, text="Buscar datos", font=("Arial", 14), bg="#d7d7d7")
label_buscar.pack(fill=tk.X, pady=(0, 30))

btn_buscar = tk.Button(frame_buscar, text="Buscar Datos por Mes", command=buscar_datos, width=20, height=2, bg="#d7d7d7", bd=0, fg="black", font=("Segoe UI", 10, "bold"))
btn_buscar.pack(pady=10)

frame_datos = tk.Frame(notebook, width=frame_width, padx=10, pady=10, bd=2, relief="groove")
notebook.add(frame_datos, text="Datos")
frame_datos.pack_propagate(False)

label_datos = tk.Label(frame_datos, text="Datos", font=("Arial", 14), bg="#d7d7d7")
label_datos.pack(fill=tk.X, pady=(0, 30))

btn_cargar = tk.Button(frame_datos, text="Cargar Datos", command=lambda: cargar_datos(texto_ingresado), width=20, height=2, bg="#d7d7d7", bd=0, fg="black", font=("Segoe UI", 10, "bold"))
btn_cargar.pack(pady=10)

btn_mostrar_todos = tk.Button(frame_datos, text="Mostrar Todos los Datos", command=mostrar_todos_datos, width=20, height=2, bg="#d7d7d7", bd=0, fg="black", font=("Segoe UI", 10, "bold"))
btn_mostrar_todos.pack(pady=10)

btn_borrar = tk.Button(frame_datos, text="Borrar Datos", command=borrar_datos, width=12, height=1, bg="#ef3232", fg="black", bd=0, font=("Segoe UI", 12, "bold"), border=4)
btn_borrar.pack(side=tk.BOTTOM, anchor="s", pady=10)

frame_derecho = tk.Frame(ventana, padx=10, pady=10)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_derecho)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Crear el Text widget con estado no editable
result_text = tk.Text(frame_derecho, bg="white", font=("Segoe UI", 12), yscrollcommand=scrollbar.set, state="disabled", height=10)
result_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=result_text.yview)

text_box = tk.Text(frame_derecho, height=15, font=("Segoe UI", 12))
text_box.pack(fill=tk.X, padx=10, pady=10)

text_box.bind("<KeyRelease>", actualizar_texto)

texto_ingresado = ""

ventana.mainloop()