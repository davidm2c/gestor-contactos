class Contacto:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"
    
    def __repr__(self):
        return f"Contacto('{self.nombre}', '{self.email}', '{self.telefono}')"
    
    def to_dict(self):
        """Convierte el contacto a diccionario para CSV"""
        return {
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un contacto desde un diccionario"""
        return cls(data['nombre'], data['email'], data['telefono'])