# CRUD de Empleados con Python, Flask y MySQL

Este es un proyecto simple de un CRUD (Crear, Leer, Actualizar, Eliminar) de empleados.

## Stack de Tecnologías

*   **Backend:** Python, Flask
*   **Base de Datos:** MySQL
*   **Frontend:** HTML, Bulma CSS
*   **Contenerización:** Docker, Docker Compose

## Cómo ejecutar con Docker

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/jc99k/crud-empleados-python-mysql
    cd crud-empleados-python-mysql
    ```

2.  **Asegurarse de tener Docker y Docker Compose instalados.**

3.  **Levantar los servicios:**
    En la raíz del proyecto, ejecutar el siguiente comando:
    ```bash
    docker-compose up --build
    ```
    Este comando construirá la imagen de la aplicación de Flask, iniciará los servicios de la aplicación y de la base de datos, y creará la base de datos y la tabla de empleados.

4.  **Acceder a la aplicación:**
    Abrir el navegador y visitar `http://localhost:5000`.
