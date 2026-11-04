# CoderBlog - Plataforma Web con Django (Entrega Final)

Aplicación web completa desarrollada con el framework Django (Python) que implementa un sistema de gestión de publicaciones (Blog) con autenticación de usuarios, panel de administración, subida de contenido multimedia y diseño responsivo con Bootstrap 5.

---

## 🚀 Funcionalidades Principales

### 📝 Blog & Publicaciones
- **CRUD Completo:** Listar, ver detalle, crear, editar y eliminar publicaciones desde la interfaz web.
- **Soporte Multimedia:** Carga de imágenes de portada con protección en plantillas (la interfaz no se rompe ante publicaciones sin imagen).
- **Buscador en Tiempo Real:** Filtro por título o contenido de los posts con avisos ante búsquedas sin coincidencias.
- **Sección 'Acerca de mí':** Página informativa institucional del autor del proyecto.

### 👤 Usuarios & Autenticación
- **Sistema de Acceso:** Registro de nuevos usuarios, inicio de sesión (Login) y cierre de sesión (Logout).
- **Rutas Protegidas:** Creación, edición, eliminación de posts y edición de perfil restringidas exclusivamente a usuarios autenticados mediante `LoginRequiredMixin` y decoradores `@login_required`.
- **Perfil de Usuario:** Visualización y edición de datos personales (nombre, apellido, email, biografía y avatar/foto de perfil).
- **Distinción de Roles:** La interfaz adapta sus botones y accesos según el estado de la sesión (visitante anónimo vs. usuario autenticado).

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12+**
- **Django 5.x** (Framework web MVT)
- **SQLite3** (Motor de base de datos)
- **Pillow** (Procesamiento y gestión de imágenes)
- **Bootstrap 5 & Bootstrap Icons** (Diseño de interfaz responsiva)
- **HTML5 & CSS3**

---

## 💻 Instrucciones de Instalación y Ejecución Local

Para clonar y ejecutar este proyecto en tu entorno local, seguí estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/frankochan10/Trabajo-Final-Python.git
cd Trabajo-Final-Python