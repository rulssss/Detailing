import psycopg2
from tkinter import messagebox
import os
import tkinter as tk


#################################################

connection = psycopg2.connect(
host="localhost",
user="postgres",
password="",
database="tiziano",
port="5432"
)
# autocommit
connection.autocommit = True

#################################################
#################################################
#################################################
#################################################

    

def traer_todos_losdatos():
    cursor= connection.cursor()
    query_data = f"SELECT * FROM jobs"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    return data

def ventana_confirmacion():
    resultado = tk.BooleanVar()
    
    # Crear una nueva ventana (modal)
    confirm_window = tk.Toplevel()
    confirm_window.title("Confirmación")
    confirm_window.geometry("400x200")  # Ajustar el tamaño a uno más grande
    confirm_window.config(bg="white")  # Fondo blanco, típico de ventanas de Windows
    confirm_window.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana emergente

    # Centrando la ventana
    screen_width = confirm_window.winfo_screenwidth()
    screen_height = confirm_window.winfo_screenheight()
    window_width = 400
    window_height = 200
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    confirm_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Etiqueta con el mensaje
    label = tk.Label(confirm_window, text="¿Está seguro de borrar TODOS los datos?", font=("Segoe UI", 12), bg="white")
    label.pack(pady=40)  # Ajustar el espaciado para mayor separación

    # Función para manejar el botón "Sí"
    def on_yes():
        resultado.set(True)
        confirm_window.destroy()

    # Función para manejar el botón "No"
    def on_no():
        resultado.set(False)
        confirm_window.destroy()

    # Crear el marco para los botones
    button_frame = tk.Frame(confirm_window, bg="white")
    button_frame.pack(pady=20)

    # Botón "Sí" con estilo y tamaño más grande
    btn_yes = tk.Button(button_frame, text="Sí", command=on_yes, width=12, relief="flat", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
    btn_yes.pack(side=tk.LEFT, padx=15)

    # Botón "No" con estilo y tamaño más grande
    btn_no = tk.Button(button_frame, text="No", command=on_no, width=12, relief="flat", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
    btn_no.pack(side=tk.LEFT, padx=15)

    confirm_window.wait_window()

    return resultado.get()

def clear_data():
    
    v = ventana_confirmacion()
    if v:
        
        cursor = connection.cursor()
        query_clear_data = "TRUNCATE jobs"
        cursor.execute(query_clear_data)
        cursor.close()
        messagebox.showinfo("Datos", "Datos borrados con éxito.")
    else:
        pass
    


def verificar_lineas():
    archivo = open("datos.csv", "r")
    c = 0
    for renglon in archivo:
        l = renglon.split(",")
        c += 1
        if c == 1:
            pass
        else:
    
            id_job = str(search_job_id(l[3])[0])

            if l[0].isalpha() and l[1].isdigit() and l[2].isdigit() and id_job.isdigit() and l[4].isalpha() and l[5].isdigit() and l[6].strip().isdigit():
                ver = True

            else:
                ver = False
                messagebox.showinfo("Cargar Datos", f"Hay algun dato ingresados en la linea {c} que no corresponde al tipo de dato admitido.")
                break

    archivo.close()
    return ver




def search_job_id(job):
    cursor = connection.cursor()
    query_job_id = f"SELECT job_id FROM type_jobs WHERE name=%s"
    value = [job]
    cursor.execute(query_job_id, value)
    dato = cursor.fetchall()
    if dato == []:
        print(f"Trabajo {job} no existente.")
    else:
        return dato[0]
        

    cursor.close()

def create_file(txt):
    with open('datos.csv', 'w', encoding='utf-8') as archivo:
        archivo.write(txt)

    

def load():
    ver = verificar_lineas()
    if ver:
        archivo = open("datos.csv", "r")
        c = 0
        for renglon in archivo:
            l = renglon.split(",")
            c += 1
            if c == 1:
                pass
            else:
                id_job = str(search_job_id(l[3])[0])

                client = f"{l[0]}"
                year = l[1]
                month = l[2]
                job = id_job
                car = f"{l[4]}"
                amount = l[5]
                cost = l[6]

                cursor = connection.cursor()
                query_insert = f"INSERT INTO jobs(client, year, month, job, car, amount, cost) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                values = (client, year, month, job, car, amount, cost)
                cursor.execute(query_insert, values)
                cursor.close()
                ver = True
                
        messagebox.showinfo("Cargar Datos", "Datos cargados con éxito.")
       
        
        archivo.close()
        
    


def load_data(txt):

    create_file(txt)

    archivo = open("datos.csv", "r")
    c = 0
   
    
    if os.path.getsize("datos.csv") > 0:
        
        for renglon in archivo:
            l = renglon.split(",")
            c += 1
            
            if c == 1 and l[0] == "client" and l[1] == "year" and l[2] == "month" and l[3] == "job" and l[4] == "car" and l[5] == "amount" and l[6] == "cost\n":
                v = True
                break
            else:
                v = False
                break
        
        if v:
            load()
        
        else:
            messagebox.showinfo("Cargar Datos", "Formato no valido.")           
                  
    else:
        messagebox.showinfo("Cargar Datos", "Nota vacia.")

    archivo.close()
    
    

def total_amount(month):
    cursor= connection.cursor()
    query_amount = f"SELECT SUM(amount) FROM jobs WHERE month=%s"
    m = (month,)
    cursor.execute(query_amount, m)
    data = cursor.fetchall()
    cursor.close()

    return data[0]

def total_cost(month):
    cursor= connection.cursor()
    query_cost = f"SELECT SUM(cost) FROM jobs WHERE month=%s"
    m = (month,)
    cursor.execute(query_cost, m)
    data = cursor.fetchall()
    cursor.close()

    return data[0]


    


