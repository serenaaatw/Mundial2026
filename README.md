# WORLDCUP MANAGER

## Integrantes del grupo
- Serena Vargas
- Tomás Caballero
- Uriel Martínez
- Diego Caipe

---

## Descripción breve

WorldCup Manager es una aplicación web desarrollada con Flask y SQLAlchemy que permite gestionar los partidos del Mundial 2026. Los usuarios pueden consultar próximos encuentros, resultados, partidos suspendidos e información general relacionada con la competición. Además, los administradores disponen de funcionalidades CRUD para la gestión completa de los datos.
    
---

## Configuración de la base de datos

Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

```env
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base>
MYSQL_HOST=<host_de_mysql>
MYSQL_PORT=<puerto_de_mysql>
API_KEY=<clave_openweather>
SECRET_KEY=<clave_de_sesión>
```
Debe crear una cuenta en OpenWeather y obtener la clave de la API, con el plan gratuito es suficiente.

---

## Requisitos

- Python 3.10 o superior
- MySQL
- Cuenta de OpenWeather

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/serenaaatw/Mundial2026.git
```

### 2. Ingresar al repositorio
```bash
cd Mundial2026
code .
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```
### 5. Roles
Para acceder a las funcionalidades de administrador es necesario que cambie su rol desde la base de datos. Esto se implementa con el objetivo de proteger la aplicación frente a otros usuarios.
    
```sql
UPDATE usuarios
SET rol = 'admin'
WHERE email = 'correo@ejemplo.com';
```
### 6. Rutas
    Para comenzar a utilizar la aplicación, abra en el navegador: http://localhost:5000/login
---

## Endpoints implementados

- GET-POST /register: Permite registrar nuevos usuarios.
  
- GET-POST /login: Permite iniciar una sesión.
- GET /logout : Permite cerrar una sesión.
- POST /partidos/crear: Permite crear un nuevo partido en la base de datos.
- GET /partidos/nuevo: Hace posible acceder al formulario para añadir un nuevo partido.
- GET /partidos: Permite visualizar todos los partidos cargados en la base de datos.
- GET /partidos/<int:partido_id>/editar: Permite al usuario administrador acceder al formulario para editar un partido.
- GET /partidos/<int:partido_id>: Permite obtener un partido existente mediante su id.
- POST /partidos/<int:partido_id>: Permite actualizar los datos de un partido existente.
- GET /partidos/<int:partido_id>/eliminar: Permite eliminar un partido de la base de datos.
- GET /suspendidos: Permite visualizar todos los partidos que han sido suspendidos.
- GET /suspendidos/<int:partido_id>/reprogramar: Accede al formulario para poder reprogramar un partido.
- POST /suspendidos/<int:partido_id>/reprogramar: Crea un nuevo partido en la base de datos, reprogramando alguno que haya sido suspendido.
- GET /general: Permite acceder a un apartado con información general sobre partidos.
- GET /resultados: Lista todos los resultados de partidos ya finalizados
- GET /resultados/nuevo: Permite acceder al formulario para añadir un nuevo resultado.
- POST /resultados/crear: Permite añadir nuevos resultados.
- GET /resultados/<int:id_res>/editar: Permite acceder al formulario para editar un resultado.
- POST /resultados/<int:id_res>/editar: Permite editar un resultado.
- GET /resultados/<int:id_res>/eliminar: Permite eliminar un resultado.
- GET /ver_usuario: Permite ver datos de un determinado usuario
- GET /ver_usuario/editar: Permite ingresar al formulario para editar los datos del usuario.
- POST /ver_usuario: Permite cambiar los datos del usuario.
---

## Proyecto académico

Trabajo práctico desarrollado para fines educativos utilizando Flask, SQLAlchemy y MySQL.
