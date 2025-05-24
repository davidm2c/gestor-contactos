# 📞 Gestor de Contactos

Una aplicación de consola desarrollada en Python para la gestión completa de contactos utilizando Programación Orientada a Objetos y manejo de archivos CSV.

## 📋 Descripción

Esta aplicación permite gestionar una agenda de contactos de manera eficiente a través de una interfaz de consola intuitiva. Los datos se almacenan en formato CSV para facilitar la portabilidad y el intercambio de información.

## ✨ Características

- ➕ **Agregar contactos**: Registro de nuevos contactos con validación de datos
- 📋 **Listar contactos**: Visualización organizada de todos los contactos
- 🔍 **Buscar contactos**: Búsqueda por nombre, email o teléfono
- ✏️ **Editar contactos**: Modificación de información existente
- 🗑️ **Eliminar contactos**: Eliminación segura con confirmación
- 💾 **Persistencia de datos**: Almacenamiento automático en archivo CSV
- ✅ **Validación de datos**: Verificación de formato de email y teléfono
- 🛡️ **Manejo de errores**: Gestión robusta de excepciones

## 🗂️ Estructura del Proyecto

```
contactos/
├── main.py                 # Aplicación principal
├── contacto.py            # Clase Contacto
├── gestor_contactos.py    # Lógica de gestión de contactos
├── contactos.csv          # Archivo de datos (se crea automáticamente)
└── README.md              # Este archivo
```

## 🚀 Instalación y Uso

### Requisitos

- Python 3.6 o superior
- No requiere librerías externas (solo módulos estándar de Python)

### Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/davidm2c/gestor-contactos.git
   cd gestor-contactos
   ```

2. **Ejecuta la aplicación:**
   ```bash
   python main.py
   ```

### Uso

Al ejecutar la aplicación, verás el menú principal:

```
==================================================
     GESTOR DE CONTACTOS
==================================================
1. Agregar contacto
2. Listar contactos
3. Buscar contacto
4. Editar contacto
5. Eliminar contacto
6. Salir
==================================================
```

#### Agregar un Contacto
- Selecciona la opción `1`
- Ingresa el nombre, email y teléfono
- La aplicación validará el formato del email y teléfono

#### Listar Contactos
- Selecciona la opción `2`
- Se mostrarán todos los contactos registrados

#### Buscar Contactos
- Selecciona la opción `3`
- Ingresa cualquier término de búsqueda
- La búsqueda funciona en todos los campos (nombre, email, teléfono)

#### Editar un Contacto
- Selecciona la opción `4`
- Ingresa el nombre del contacto a editar
- Modifica los campos deseados (deja en blanco para mantener el valor actual)

#### Eliminar un Contacto
- Selecciona la opción `5`
- Ingresa el nombre del contacto a eliminar
- Confirma la eliminación

## 🏗️ Arquitectura

### Clases Principales

#### `Contacto`
```python
class Contacto:
    def __init__(self, nombre, email, telefono)
    def __str__(self)
    def to_dict(self)
    def from_dict(cls, data)
```

#### `GestorContactos`
```python
class GestorContactos:
    def cargar_contactos(self)
    def guardar_contactos(self)
    def agregar_contacto(self, nombre, email, telefono)
    def listar_contactos(self)
    def editar_contacto(self, nombre, nuevo_email, nuevo_telefono)
    def eliminar_contacto(self, nombre)
    def buscar_contactos(self, termino)
```

#### `AplicacionContactos`
```python
class AplicacionContactos:
    def mostrar_menu(self)
    def validar_email(self, email)
    def validar_telefono(self, telefono)
    def ejecutar(self)
```

## 📁 Formato del Archivo CSV

El archivo `contactos.csv` tiene la siguiente estructura:

```csv
nombre,email,telefono
Juan Pérez,juan.perez@email.com,+1234567890
María García,maria.garcia@email.com,+0987654321
```

## ✅ Validaciones

### Email
- Formato válido: `usuario@dominio.com`
- Expresión regular: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

### Teléfono
- Permite números, espacios, guiones, paréntesis y signo +
- Mínimo 7 caracteres
- Expresión regular: `^[\d\s\-\(\)\+]+$`

## 🛠️ Funcionalidades Técnicas

- **Persistencia automática**: Los cambios se guardan inmediatamente en el archivo CSV
- **Codificación UTF-8**: Soporte completo para caracteres especiales
- **Búsqueda insensible a mayúsculas**: Las búsquedas no distinguen entre mayúsculas y minúsculas
- **Prevención de duplicados**: No permite contactos con el mismo nombre
- **Manejo de archivos**: Creación automática del archivo CSV si no existe

## 🔧 Manejo de Errores

La aplicación maneja los siguientes tipos de errores:

- Archivos CSV corruptos o inaccesibles
- Datos de entrada inválidos
- Contactos duplicados
- Contactos no encontrados
- Interrupciones del usuario (Ctrl+C)

## 📝 Ejemplos de Uso

### Agregar un contacto
```
--- AGREGAR CONTACTO ---
Nombre: Juan Pérez
Email: juan.perez@email.com
Teléfono: +1234567890
Contacto 'Juan Pérez' agregado exitosamente.
```

### Buscar contactos
```
--- BUSCAR CONTACTO ---
Ingrese término de búsqueda: juan

Se encontraron 1 contacto(s):
------------------------------------------------------------
1. Nombre: Juan Pérez, Email: juan.perez@email.com, Teléfono: +1234567890
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**David M2C**
- GitHub: [@davidm2c](https://github.com/davidm2c)
- Email: tu-email@ejemplo.com

## 🙏 Agradecimientos

- Proyecto desarrollado como parte del curso de Programación Orientada a Objetos
- Inspirado en las mejores prácticas de desarrollo en Python
- Agradecimientos especiales a la comunidad de Python por la documentación y recursos

---

⭐ ¡Si te gusta este proyecto, no olvides darle una estrella!