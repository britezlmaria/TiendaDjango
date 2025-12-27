#  Tienda Online Fullstack - E-commerce con Django

Este es un sistema integral de **Comercio Electrónico** desarrollado con **Python** y **Django**. La plataforma permite una experiencia de compra completa, desde la navegación de productos hasta la gestión del carrito y la autenticación de usuarios, todo bajo una arquitectura profesional y escalable.

##  Funcionalidades Principales

###  Ciclo de Compra Completo
* **Catálogo Dinámico:** Visualización de productos organizados por categorías con carga desde base de datos.
* **Carrito de Compras Pro:** Lógica personalizada para añadir, restar y eliminar productos, manteniendo la persistencia durante la sesión del usuario.
* **Gestión de Pedidos:** Procesamiento de órdenes de compra vinculadas a usuarios registrados.

###  Seguridad y Usuarios
* **Registro e Inicio de Sesión:** Implementación de Vistas Basadas en Clases (`View`) para el alta de usuarios y manejo de sesiones (`login`/`logout`).
* **Validación de Datos:** Sistema de gestión de errores y mensajes informativos (`messages framework`) para una mejor experiencia de usuario.

###  Comunicación y Contenido
* **Blog Integrado:** Sección de noticias o novedades categorizadas para fidelización de clientes.
* **Sistema de Contacto:** Formulario funcional con validación y backend preparado para el envío de correos electrónicos.

##  Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Framework Web:** Django 5.x
* **Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Producción).
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap.
* **Lógica de Sesiones:** Manejo de carrito basado en `request.session`.

##  Arquitectura del Proyecto

El proyecto utiliza un enfoque modular donde cada aplicación de Django cumple un rol específico:
- `Tienda/`: Gestión del catálogo y visualización de productos.
- `Carro/`: Procesamiento lógico de la cesta de compras.
- `Autenticacion/`: Manejo de identidad y seguridad de usuarios.
- `Pedido/`: Persistencia y control de transacciones.
- `Blog/`: Sistema de gestión de contenidos y artículos.
- `Contacto/`: Gestión de comunicación con el cliente.

##  Cómo ejecutar el proyecto

1. Clona este repositorio.
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate
3. Instala Django:
   ```bash
   pip install django
4. Aplica las migraciones:
   ```bash
   python manage.py migrate
5. Inicia el servidor de desarrollo:
   ```bash
    python manage.py runserver

---
**Desarrollado por [Maria Luisa Britez](https://github.com/britezlmaria)** *Estudiante de Licenciatura en Sistemas - Facultad de Informática (UNLP)*
