from gestor_contactos import GestorContactos
import re

class AplicacionContactos:
    def __init__(self):
        self.gestor = GestorContactos()
    
    def validar_email(self, email):
        """Valida el formato del email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def validar_telefono(self, telefono):
        """Valida el formato del teléfono"""
        # Permite números, espacios, guiones y paréntesis
        patron = r'^[\d\s\-\(\)\+]+$'
        return re.match(patron, telefono) is not None and len(telefono.strip()) >= 7
    
    def mostrar_menu(self):
        """Muestra el menú principal"""
        print("\n" + "="*50)
        print("     GESTOR DE CONTACTOS")
        print("="*50)
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        print("="*50)
    
    def agregar_contacto(self):
        """Interfaz para agregar un contacto"""
        print("\n--- AGREGAR CONTACTO ---")
        
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        
        email = input("Email: ").strip()
        if not email or not self.validar_email(email):
            print("Email inválido.")
            return
        
        telefono = input("Teléfono: ").strip()
        if not telefono or not self.validar_telefono(telefono):
            print("Teléfono inválido.")
            return
        
        self.gestor.agregar_contacto(nombre, email, telefono)
    
    def buscar_contacto(self):
        """Interfaz para buscar contactos"""
        print("\n--- BUSCAR CONTACTO ---")
        termino = input("Ingrese término de búsqueda: ").strip()
        
        if not termino:
            print("Debe ingresar un término de búsqueda.")
            return
        
        resultados = self.gestor.buscar_contactos(termino)
        
        if not resultados:
            print("No se encontraron contactos.")
            return
        
        print(f"\nSe encontraron {len(resultados)} contacto(s):")
        print("-" * 60)
        for i, contacto in enumerate(resultados, 1):
            print(f"{i}. {contacto}")
    
    def editar_contacto(self):
        """Interfaz para editar un contacto"""
        print("\n--- EDITAR CONTACTO ---")
        nombre = input("Nombre del contacto a editar: ").strip()
        
        if not nombre:
            print("Debe ingresar un nombre.")
            return
        
        contacto = self.gestor.buscar_contacto_por_nombre(nombre)
        if not contacto:
            print(f"No se encontró un contacto con el nombre '{nombre}'")
            return
        
        print(f"Contacto actual: {contacto}")
        print("Deje en blanco para mantener el valor actual:")
        
        nuevo_email = input(f"Nuevo email ({contacto.email}): ").strip()
        if nuevo_email and not self.validar_email(nuevo_email):
            print("Email inválido.")
            return
        
        nuevo_telefono = input(f"Nuevo teléfono ({contacto.telefono}): ").strip()
        if nuevo_telefono and not self.validar_telefono(nuevo_telefono):
            print("Teléfono inválido.")
            return
        
        self.gestor.editar_contacto(
            nombre, 
            nuevo_email if nuevo_email else None,
            nuevo_telefono if nuevo_telefono else None
        )
    
    def eliminar_contacto(self):
        """Interfaz para eliminar un contacto"""
        print("\n--- ELIMINAR CONTACTO ---")
        nombre = input("Nombre del contacto a eliminar: ").strip()
        
        if not nombre:
            print("Debe ingresar un nombre.")
            return
        
        contacto = self.gestor.buscar_contacto_por_nombre(nombre)
        if not contacto:
            print(f"No se encontró un contacto con el nombre '{nombre}'")
            return
        
        print(f"Contacto a eliminar: {contacto}")
        confirmacion = input("¿Está seguro? (s/N): ").strip().lower()
        
        if confirmacion == 's' or confirmacion == 'si':
            self.gestor.eliminar_contacto(nombre)
        else:
            print("Eliminación cancelada.")
    
    def ejecutar(self):
        """Ejecuta la aplicación principal"""
        print("¡Bienvenido al Gestor de Contactos!")
        
        while True:
            try:
                self.mostrar_menu()
                opcion = input("Seleccione una opción (1-6): ").strip()
                
                if opcion == '1':
                    self.agregar_contacto()
                elif opcion == '2':
                    self.gestor.listar_contactos()
                elif opcion == '3':
                    self.buscar_contacto()
                elif opcion == '4':
                    self.editar_contacto()
                elif opcion == '5':
                    self.eliminar_contacto()
                elif opcion == '6':
                    print("¡Gracias por usar el Gestor de Contactos!")
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")
                
                input("\nPresione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego!")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")

if __name__ == "__main__":
    app = AplicacionContactos()
    app.ejecutar()