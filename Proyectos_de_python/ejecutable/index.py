
from cgitb import text
from distutils import text_file
from itertools import tee
from tkinter import *
import sqlite3
from tkinter import ttk


class Product:
    
    db_name = 'database.db'
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')
        
        #Creating a Frame Container
        frame = LabelFrame(self.wind, text = 'Register A new Product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        #Name Input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name =  Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)
        
        
        #Price Input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)
        
        #Amount Input
        Label(frame, text = 'Amount: ').grid(row =  3, column = 0)
        self.amount = Entry(frame)
        self.amount.grid(row = 3, column = 1)
        
        
        #Measurement units Input
        Label(frame, text = 'Measurement units: ').grid(row =  4, column = 0)
        self.measurement = Entry(frame)
        self.measurement.grid(row = 4, column = 1)        
        
        #Units available Input
        Label(frame, text = 'Units available: ').grid(row =  5, column = 0)
        self.Units = Entry(frame)
        self.Units.grid(row = 5, column = 1)
        
        #Button Add Product
        ttk.Button(frame, text = "Save Product").grid(row = 6, columnspan = 3, sticky = W + E)
        
        
        #Table
        self.tree = ttk.Treeview(height = 20, columns = ('Price', 'Amount', 'Measurement units', 'Units available'))
        self.tree.grid(row = 4, column = 0, columnspan = 3)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('Price', text = 'Price', anchor = CENTER)
        self.tree.heading('Amount', text = 'Amount', anchor = CENTER)
        self.tree.heading('Measurement units', text = 'Measurement units', anchor = CENTER)
        self.tree.heading('Units available', text = 'Units available', anchor = CENTER)
        
        self.get_products()
    
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result    
        
    def get_products(self):
        #cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #quering data
        query = 'SELECT*FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        #filling data 
        for row  in  db_rows:
            print(row)
            self.tree.insert('', 0, text = row[1], values = row[2], text = row[3])
           
    
if __name__ == '__main__':
    window = Tk()
    aplication = Product(window)
    window.mainloop()