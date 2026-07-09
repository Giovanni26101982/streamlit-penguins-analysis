# Informe de Laboratorio: Aplicación Streamlit con GitFlow

## 1. Objetivo

Desarrollar una aplicación de análisis de datos sobre el dataset Palmer Penguins utilizando Streamlit, implementando un flujo de trabajo de control de versiones GitFlow e integrando pruebas automatizadas con pytest.

---

## 2. Procedimiento Realizado

2.1. **Configuración del Repositorio y GitFlow**

Se inicializó el repositorio estableciendo la rama **main** para producción y **develop** para integración. El desarrollo se realizó mediante ramas de característica (**feature/**) aisladas para evitar conflictos:

- **feature/validacion-datos**: Implementación de lógica de validación de esquemas y nulos.
- **feature/app-principal**: Estructura base de la interfaz en Streamlit.
- **feature/viz-tabular**: Implementación de visualización de datos interactiva.
- **feature/pruebas-pytest**: Creación de tests unitarios para las funciones de validación.

Cada rama fue fusionada a **develop** utilizando **git merge --no-ff** para preservar el historial de características.

Creación directorio:

<img width="670" height="633" alt="image" src="https://github.com/user-attachments/assets/3f7710c2-6d2a-4582-9692-bd2ea5684913" />

Creación de README.md

<img width="669" height="254" alt="image" src="https://github.com/user-attachments/assets/c18bbfd5-8474-42cf-944c-1593b50130ab" />

Rama Develop

<img width="660" height="165" alt="image" src="https://github.com/user-attachments/assets/b8e71b65-3ee2-4fee-bdd5-ab7f8c07940a" />


2.2. **Desarrollo de la Aplicación**

- **Validación**: Se crearon funciones en **utils/validation.py** para asegurar la integridad del dataset antes de su procesamiento.
- **Interfaz**: La aplicación **app.py** carga el archivo **penguins.csv**, valida los datos y muestra métricas clave (totales y nulos).
- **Visualización**: Se implementó una tabla interactiva y gráficos de distribución utilizando las libreras nativas de Streamlit.

2.3. Pruebas y Release
Se ejecutó el suite de pruebas con pytest, validando el correcto funcionamiento de los módulos de utilidad. Tras verificar la estabilidad en develop, se fusionó el código a main y se etiquetó la versión estable con el tag v101.1.0 hasta el tag v101.1.4.

**Pruebas**

<img width="664" height="216" alt="image" src="https://github.com/user-attachments/assets/6636246a-9ca2-497d-bdbf-ea939a821bd1" />

**Actualización de rama**

<img width="661" height="141" alt="image" src="https://github.com/user-attachments/assets/244217d0-2400-4981-b800-97df0a46f970" />

**Actualización a la rama MAIN**

<img width="663" height="238" alt="image" src="https://github.com/user-attachments/assets/5fb317ba-82e4-4d01-a946-5e7b9bd11390" />


**Release**

<img width="666" height="109" alt="image" src="https://github.com/user-attachments/assets/02a05c7f-f3d7-445a-9dba-98fdadae5dbd" />

<img width="721" height="146" alt="image" src="https://github.com/user-attachments/assets/ddeded02-69a1-45a2-91bc-637084a6c2f8" />

**Vincular repositorio Local a GitHub**

<img width="664" height="170" alt="image" src="https://github.com/user-attachments/assets/70537e6e-d0e9-4495-a8df-bb4b67446af4" />

**Revisar estado de la rama y hacer commit**
<img width="665" height="542" alt="image" src="https://github.com/user-attachments/assets/dd35124a-0e06-4b92-8117-7a7a585fa7dd" />

**Realizamos el Merge**

<img width="661" height="437" alt="image" src="https://github.com/user-attachments/assets/fa16e3a8-c40f-46e4-8250-afa07e5b2a72" />

**Subimos a GitHub**

<img width="665" height="509" alt="image" src="https://github.com/user-attachments/assets/5a517f0d-b6ba-4707-9d69-60a301042afc" />

**Ejecutamos**

<img width="665" height="675" alt="image" src="https://github.com/user-attachments/assets/18390da5-7044-46fb-864c-5da34400187c" />


---

## 3. Evidencias de Ejecución

3.1. **Dashboard Principal**

La aplicación carga correctamente, valida los datos y muestra las métricas iniciales.

<img width="1214" height="378" alt="image" src="https://github.com/user-attachments/assets/543d7c53-384a-41f7-a258-c73a8ee46536" />


3.2. **Visualización Tabular**

Se muestra la tabla interactiva con los datos de los pingüinos y los gráficos de distribución.

<img width="1214" height="505" alt="image" src="https://github.com/user-attachments/assets/1ebfa284-ab3d-4205-9725-e4374883656f" />

<img width="1223" height="338" alt="image" src="https://github.com/user-attachments/assets/5ee75420-a51b-493c-a20f-77017e5feed4" />


3.3. **Pruebas con Pytest**

Ejecución exitosa de los tests unitarios en la terminal, confirmando la validez del código.

<img width="664" height="216" alt="image" src="https://github.com/user-attachments/assets/e38895a9-7d2e-4574-af5d-a88111019d52" />


---

## 4. Conclusión

- Se logró implementar exitosamente un ciclo de vida de desarrollo de software ágil mediante GitFlow, garantizando la calidad del código a través de pruebas unitarias y entregando una aplicación funcional de análisis de datos. El repositorio cuenta con las ramas main, develop, el tag de versión y la documentación requerida.

