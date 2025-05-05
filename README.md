# Django Blog Project

## Descripción general del proyecto
Esta es una aplicación de blog basada en Django que permite a los usuarios ver publicaciones de blog. Incluye características como paginación, vistas a detalle para cada publicación y una interfaz de administración para administrar las publicaciones.

---

## Aplicación core

### **core/settings.py**
- Contiene la configuración para el proyecto Django, incluidas las aplicaciones instaladas, el middleware, la configuración de la base de datos y la configuración de archivos estáticos.
- Key settings:
  - `INSTALLED_APPS`: Incluir `blog` y `django_extensions`.
  - `DATABASES`: Utiliza SQLite como backend de la base de datos.
  - `TEMPLATES`: Configurada para usar plantillas desde `templates` como directorio.

### **core/urls.py**
- Define los patrones de URL para el proyecto.
- Incluye:
  - Interfaz de administración en `/admin/`.
  - URL de la aplicación de blog en `/blog/`.

### **core/wsgi.py**
- Configuración de WSGI para implementar el proyecto.

### **core/asgi.py**
- Configuración de ASGI para la implementación del servidor asincrónico.

---

## Blog Application

### **blog/models.py**
- Define el modelo `Post` con campos como `title`, `slug`, `author`, `body`, `publish`, `created`, `updated`, y `status`.
- Incluye un administrador personalizado `PublishedManager` para filtrar publicaciones publicadas.
- Proporciona un método `get_absolute_url` para generar URL de detalles posteriores.

### **blog/views.py**
- Contiene dos vistas:
  - `post_list`: Muestra una lista paginada de publicaciones publicadas.
  - `post_detail`: Muestra los detalles de una sola publicación.

### **blog/urls.py**
- Mapas de URL a vistas:
  - `/blog/`: Muestra la lista de publicaciones.
  - `/blog/<year>/<month>/<day>/<slug>/`: Muestra una publicación específica.

### **blog/admin.py**
- Configura la interfaz de administrador de Django para el modelo `Post`.
- Features:
  - Lista de visualización de campos como `title`, `slug`, `author`, `publish`, y `status`.
  - Filtros `status`, `created`, `publish`, y `author`.
  - Funcionalidad de búsqueda para `title` y `body`.

### **blog/tests.py**
- Marcador de posición para escribir pruebas para la aplicación del blog.

### **blog/apps.py**
- Configura el app `blog`.

---

## **Templates**

### **templates/base.html**
- Plantilla base para el proyecto.
- Incluye una barra lateral y marcadores de posición para `title` y `content`.

### **templates/post/list.html**
- Plantilla para mostrar una lista de publicaciones de blog.
- Incluye paginación.

### **templates/post/detail.html**
- Plantilla para mostrar los detalles de una sola publicación.

### **templates/pagination.html**
- Plantilla para realizar controles de paginación.

---

## Static Files

### **static/css/style.css**
- Contiene estilos para el blog, que incluye diseño, tipografía y paginación.

---

## Other Files

### **manage.py**
- Punto de entrada para la utilidad de línea de comandos de Django.

### **requirements.txt**
- Enumera las dependencias de Python para el proyecto.

### **.flake8**
- CConfiguración para el Linter Flake8.

### **.gitignore**
- Especifica archivos y directorios para ignorar en el control de versiones.

### **.vscode/settings.json**
- VS Configuración específica del código para el proyecto.

### **db.sqlite3**
- Archivo de base de datos sqlite.

---

## Cómo clonar y ejecutar el proyecto

### Requisitos previos
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Pasos para clonar y correr

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/your-username/django_blog.git
   cd django_blog
    ```

2. **Crear un entorno virtual**
3. ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```
5. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```
6. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```
7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```
8. **Acceder a la aplicación**
   - Abra su navegador web y vaya a `http://localhost:8000/` Para ver el blog.
   - Acceder a la interfaz de administración en `http://localhost:8000/admin/` Uso de las credenciales de Superuser creadas anteriormente.
9. **Crear publicaciones de blog**
   - Use la interfaz de administración para crear y administrar publicaciones de blog.
   - Vea la lista de publicaciones y sus detalles en la página principal.
   - Use la paginación para navegar a través de múltiples publicaciones.
   - Haga clic en un título de publicación para ver sus detalles.
10. **Ejecutar pruebas (opcional)**
    ```bash
    python manage.py test
    ```
11. **Linting (opcional)**
    ```bash
    flake8 .
    ```
12. **Desactivar el entorno virtual (opcional)**
    ```bash
    deactivate
    ```
---