# Servicio de Cobertura

Este repositorio contiene el código fuente para el servicio encargado de manejar las consultas relacionadas con códigos postales y coberturas de paqueterías en México. Este servicio es parte fundamental del sistema y está construido usando Django.

## Prerrequisitos

Antes de comenzar con la configuración del entorno local, asegúrate de tener lo siguiente:

- **PostgreSQL**: Necesario para gestionar la base de datos del proyecto.
- **Python**: Asegúrate de tener Python instalado para ejecutar scripts y gestionar dependencias.
- **Archivo .env**: Obtén el archivo .env con las configuraciones de entorno necesarias solicitándolo al personal autorizado.
- **Clonar el repositorio**: Clona este repositorio en tu equipo local para acceder al código fuente y trabajar en el proyecto:

  ```bash
  git clone https://github.com/Sheeping-project/cobertura.git
  cd nombre-del-repo
  ```

## Configuración Inicial del Entorno Local

Sigue los pasos a continuación para configurar tu entorno local y comenzar a trabajar en el proyecto.

### 1. Crear Base de Datos Local

Para crear la base de datos local necesaria para el proyecto en PostgreSQL, utiliza los siguientes comandos en `psql` como referencia:

```psql
-- Crear la base de datos para el proyecto
CREATE DATABASE nombre_de_la_base_de_datos;

-- Crear un nuevo usuario con una contraseña segura
CREATE USER nombre_de_usuario WITH PASSWORD 'tu_contraseña';

-- Otorgar todos los privilegios sobre la base de datos al usuario recién creado
GRANT ALL PRIVILEGES ON DATABASE nombre_de_la_base_de_datos TO nombre_de_usuario;

-- Asignar la propiedad de la base de datos al usuario recién creado
ALTER DATABASE nombre_de_la_base_de_datos OWNER TO nombre_de_usuario;

-- Los siguientes dos comandos son necesarios en PostgreSQL 15 y versiones posteriores
-- Conectar a la base de datos recién creada
\connect nombre_de_la_base_de_datos;

-- Otorgar permisos de creación en el esquema público al usuario
GRANT CREATE ON SCHEMA public TO nombre_de_usuario;
```

### 2. Crear un Entorno Virtual

Crea un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv venv
```

### 3. Activar el Entorno Virtual

Activa el entorno virtual recién creado:

En Windows:

```bash
venv\Scripts\activate
```

En macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Instalar Dependencias del Proyecto

Con el entorno virtual activado, instala todas las dependencias necesarias para el proyecto:

```bash
pip install -r requirements/local.txt
```

### 5. Configurar Variables de Entorno

Crea un archivo .env con las configuraciones locales. Puedes usar el archivo .env.example como referencia:

```bash
cp .env.example .env
```
Edita el archivo .env con las configuraciones específicas para tu entorno local.

### 6. Aplicar Migraciones

Realiza las migraciones necesarias para cada aplicación del proyecto:

```bash
python manage.py makemigrations core accounts states cities neighborhoods carriers services postalcodes postalconnectedservices zonification
python manage.py migrate
```

### 7. Validar Migraciones

Antes de crear un superusuario, asegúrate de que todas las migraciones se han aplicado correctamente:

```bash
python manage.py showmigrations
```

### 8. Crear Superusuario

Para gestionar tu proyecto con control total y acceso administrativo, es fundamental crear un superusuario:

```bash
python manage.py createsuperuser
```

### 9.- Arrancar Servidor

Una vez que hayas completado los pasos anteriores, el entorno local estará listo para ejecutar y desarrollar el proyecto. Puedes iniciar el servidor de desarrollo de Django con el siguiente comando:

```bash
python manage.py runserver
```
