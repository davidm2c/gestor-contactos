import csv
import os
from contacto import Contacto

class GestorContactos:
    def __init__(self, archivo_csv='contactos.csv'):
        self.archivo_csv = archivo_csv
        self.contactos = []
        self.cargar_contactos()
    
    def cargar_contactos(self):
        """Carga los contactos desde el archivo CSV"""
        if os.path.exists(self.archivo_csv):
            try:
                with open(self.archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
                    reader = csv.DictReader(archivo)
                    self.contactos = [Contacto.from_dict(fila) for fila in reader]
                print(f"Se cargaron {len(self.contactos)} contactos desde {self.archivo_csv}")
            except Exception as e:
                print(f"Error al cargar contactos: {e}")
                self.contactos = []
        else:
            print(f"Archivo {self.archivo_csv} no existe. Se creará uno nuevo.")
            self.contactos = []
    
    def guardar_contactos(self):
        """Guarda los contactos en el archivo CSV"""
        try:
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
                if self.contactos:
                    fieldnames = ['nombre', 'email', 'telefono']
                    writer = csv.DictWriter(archivo, fieldnames=fieldnames)
                    writer.writeheader()
                    for contacto in self.contactos:
                        writer.writerow(contacto.to_dict())
                print(f"Contactos guardados en {self.archivo_csv}")
        except Exception as e:
            print(f"Error al guardar contactos: {e}")
    
    def agregar_contacto(self, nombre, email, telefono):
        """Agrega un nuevo contacto"""
        # Verificar si el contacto ya existe
        if self.buscar_contacto_por_nombre(nombre):
            print(f"Ya existe un contacto con el nombre '{nombre}'")
            return False
        
        nuevo_contacto = Contacto(nombre, email, telefono)
        self.contactos.append(nuevo_contacto)
        self.guardar_contactos()
        print(f"Contacto '{nombre}' agregado exitosamente.")
        return True
    
    def listar_contactos(self):
        """Lista todos los contactos"""
        if not self.contactos:
            print("No hay contactos registrados.")
            return
        
        print("\n" + "="*60)
        print("LISTA DE CONTACTOS")
        print("="*60)
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i}. {contacto}")
        print("="*60)
    
    def buscar_contacto_por_nombre(self, nombre):
        """Busca un contacto por nombre"""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None
    
    def editar_contacto(self, nombre, nuevo_email=None, nuevo_telefono=None):
        """Edita un contacto existente"""
        contacto = self.buscar_contacto_por_nombre(nombre)
        if not contacto:
            print(f"No se encontró un contacto con el nombre '{nombre}'")
            return False
        
        if nuevo_email:
            contacto.email = nuevo_email
        if nuevo_telefono:
            contacto.telefono = nuevo_telefono
        
        self.guardar_contactos()
        print(f"Contacto '{nombre}' editado exitosamente.")
        return True
    
    def eliminar_contacto(self, nombre):
        """Elimina un contacto"""
        contacto = self.buscar_contacto_por_nombre(nombre)
        if not contacto:
            print(f"No se encontró un contacto con el nombre '{nombre}'")
            return False
        
        self.contactos.remove(contacto)
        self.guardar_contactos()
        print(f"Contacto '{nombre}' eliminado exitosamente.")
        return True
    
    def buscar_contactos(self, termino):
        """Busca contactos que contengan el término en cualquier campo"""
        resultados = []
        termino = termino.lower()
        
        for contacto in self.contactos:
            if (termino in contacto.nombre.lower() or 
                termino in contacto.email.lower() or 
                termino in contacto.telefono.lower()):
                resultados.append(contacto)
        
        return resultados