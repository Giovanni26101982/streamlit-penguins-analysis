#Actividad No. 1

#Laboratorio GIT aplicado a una aplicación Streamlit para análisis de datos

# Grupo 4
## 🚀 Integrantes
| Nro. | Nombre | Link |
|------|---------|---------|
| 1 | Giovanni Xavier Baño Jaya | https://github.com/Giovanni26101982/Grupo4_Docker_TareaFinal |
| 2 | Jara Pauta Cesar Paúl | https://github.com/PaulJara84/Grupo4_Docker_TareaFinal |

---

## 📖 1. Configuración Inicial y GitFlow

El primer paso es establecer la estructura de ramas adecuada. GitFlow utiliza ramas específicas para desarrollo y características, asegurando que la rama **main** (o **master**) contenga solo código estable.

**Inicialización del Repositorio**

Crea un directorio para tu proyecto e inicializa Git. Es crucial crear la rama develop desde el inicio, ya que todo el desarrollo ocurrirá allí. 


```bash
# Crear carpeta y entrar
mkdir streamlit-penguins-analysis
cd streamlit-penguins-analysis

# Inicializar git
git init

# Crear archivo README.md inicial y hacer el primer commit en main
echo "# Análisis de Datos Penguins con Streamlit" > README.md
git add README.md
git commit -m "Initial commit"

# Crear rama develop y cambiar a ella
git branch develop
git checkout develop   
```

---

**Estrategia de Ramas para las Actividades**

Para cumplir con los requisitos sin generar conflictos ni usar hotfixes, se crearán ramas de característica (**feature/**) individuales desde **develop** para cada tarea solicitada:

1. **feature/validacion-datos**: Para las funciones de validación.
2. **feature/app-principal**: Para la interfaz base de Streamlit.
3. **feature/viz-tabular**: Para la tabla de datos interactiva.
4. **feature/pruebas-pytest**: Para los tests unitarios. 



## 🖥️ Descarga del repositorio

   - Descargar el repositorio
     ```bash
     git clone https://github.com/Giovanni26101982/Grupo4_Docker_TareaFinal.git
     ```
<img width="1125" height="305" alt="image" src="https://github.com/user-attachments/assets/3b02a6b7-49a1-42c2-a1af-cdb5f3eb8703" />

   - Navegar a la carpeta descargada 
     ```bash
     cd Grupo4_Docker_TareaFinal/
     ```
<img width="1123" height="64" alt="tarea final" src="https://github.com/user-attachments/assets/96636ef1-0f24-421d-a876-0c1f684a148c" />


---

## 🚀 Requisitos previos
- Docker instalado
- Docker Compose instalado

---

## 📂 Estructura
```bash
flowise-postgres/
│── docker-compose.yml
│── .env
└── README.md
```

---


## ✅ Conclusiones

1. **Compatibilidad de versión de Compose**

   -	La instrucción name: solo es reconocida en la especificación moderna de Compose (ejecutando docker compose en lugar de docker-compose).
     <img width="886" height="117" alt="image" src="https://github.com/user-attachments/assets/9d6de6da-b703-4fc5-a47b-2afc23410a30" />

   -	Se detectó que version: ya es obsoleto en Compose V2, por lo que puede omitirse para evitar advertencias.
     <img width="711" height="441" alt="image" src="https://github.com/user-attachments/assets/a68e5832-6cc0-4540-a947-db94d9bbd159" />

2. **Gestión de espacio en disco**

   - Durante la descarga de la imagen flowiseai/flowise:1.6.3 se produjo un error de “no space left on device”.
   - Se resolvió mediante limpieza de imágenes, volúmenes y contenedores no utilizados, confirmando la importancia de tener espacio disponible antes de la instalación.

3.	**Ejecución del contenedor Flowise**
   
      - El contenedor entraba en bucle de reinicios porque la imagen oficial requiere ejecutar explícitamente el comando flowise start.
      - Al añadir command: ["flowise", "start"] en el docker-compose.yml, el servicio se inicializó correctamente y quedó accesible en el puerto configurado.
     
4.	**Base de datos y persistencia**

      - El contenedor PostgreSQL respondió como healthy, lo que confirma que la configuración de credenciales (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB) fue 
