# Sistema de Gestión de partidos del mundial 2026
# WORLDCUP MANAGER

## Integrantes del grupo
- Serena Vargas
- Tomás Caballero
- Uriel Martínez
- Diego Caipe

---

## Descripción breve
Este proyecto consiste en una aplicación desarrollada para gestionar todos los partidos del mundial 2026. Creando un sistema completo aplicando ----
---

## Configuración de la base de datos

Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

```env
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base>
MYSQL_HOST=<host_de_mysql>
MYSQL_PORT=<puerto_de_mysql>
API_KEY = <clave_openweather>
```

---

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

---

## Endpoints implementados

- GET /partidos
- POST /partidos
- DELETE /partidos/<int:partido_id>
- PUT /propietario/<int:patrido_id>
- 

---

## Aporte de cada integrante

### Tomás Caballero
- Creacion controlador usuario
- Creacion ruta usuario(ver, editar y actualizar)
- Creación ver perfil html
- Creación editar perfil html
- Creación ver perfil css
- Creacion editar perfil css
- Cargar foto de perfil en perfil
- Validar direccion de correo 

### Uriel Martinez
- Creación de modelo Usuario.
- Creación de modelo Administrador.
- Creación de modelo Cliente.
- Creación del auth controler (register,login,loguot)
- Rutas correspodientes al register, login y logout.
- Creación de aut.html y static css (estructuta y visulización).
### Serena Vargas
- Creación modelo equipo
- Creación modelo estadio
- Creación modelo partido
- Carga de carpeta img
- Base html
- Partidos html
- Actualizar partido html
- Partidos css
- Base css
- Partidos controller
- Estadio controller
- Partido css
- Endpoint partido (CRUD)
- Validaciones al actualiza partido

### Diego Caipe

---

## Trabajo grupal
- Configuración de la aplicación
- Configuración de la base de datos
- Integración general del proyecto
