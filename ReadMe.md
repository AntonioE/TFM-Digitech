# Desarrollo del TFM: Perfilación de Riesgo del Inversor

## 1. Flujo de trabajo

Les comparto una visión secuencial y sintética del flujo de trabajo seguido en el TFM, para que puedan contextualizar cada notebook antes de revisarlo.

---

### 1.1. Exploración preliminar  
**Notebooks:** `0_NFCS_2021_EDA`, `0_SCF2022_EDA`

- EDA comparativo NFCS-2021 vs. SCF-2022.  
- Selección definitiva de NFCS-2021 por su variable de tolerancia al riesgo alineada con los objetivos del modelo y su mayor riqueza psicológica.

---

### 1.2. Análisis y depuración en profundidad  
**Notebooks:** `01_NFCS_2021_Full_EDA`, `02_NFCS_Data_Cleaning`

- Análisis detallado de distribuciones, correlaciones y outliers.  
- Limpieza: tratamiento de códigos especiales, imputación estratificada y winsorización.  
- Dataset resultante: 2.824 observaciones × 92 variables, sin valores faltantes críticos.

---

### 1.3. División de datos y selección inicial de variables  
**Notebooks:** `03.1_Division_TrainValTest`, `03.3_Seleccion_Features_Manual`, `03.4_Optimizacion_Features`

- División `train/validation/test`.  
- Selección automática descartada por proponer ítems excesivamente técnicos.  
- Selección manual basada en dominio, reduciendo a ~10 preguntas amigables para el usuario.  
- Codificación y optimización de esas variables para modelado.

---

### 1.4. Gestión del desbalance  
**Notebooks:** `03.5_Modelo_2outputs`, `03.5_Modelo_3outputs`

- Variable objetivo originalmente en 4 clases y altamente desbalanceada.  
- Se evaluaron configuraciones de 3 y 2 clases; la versión binaria aportó mayor estabilidad y mejores métricas globales.

---

### 1.5. Primer ciclo de modelado  
**Notebooks:** `04.1_Modelo_RegresionLogistica`, `04.2_Modelo_RandomForest`, `04.3_Modelo_LightGBM`

- Entrenamiento sobre las features optimizadas y la versión binaria de la variable objetivo.  
- Los resultados, aunque aceptables, no alcanzaron el umbral deseado → necesidad de mejorar ingeniería de variables.

---

### 1.6. Ingeniería de características avanzada  
**Notebooks:** `05.0_Ingenieria_Avanzada_Automatica`, `05.1_Ingenieria_Avanzada_95`, `06.0_Modelado_Comparacion`

- Generación automática: impacto limitado.  
- Ingeniería manual de 11 nuevas variables (dataset “95 ultimate”).  
- Comparación de modelos:
  - Dataset base (95 limpias) → mejor en población general.  
  - Dataset 95 ultimate → superior en detección de perfiles de alto riesgo.

---

### 1.7. Modelos especializados y optimización final  
**Notebooks:** `06.0_Modelado_Comparacion`, `06.1_Optimizacion_Modelo_Academico`, `06.2_Optimizacion_Modelo_Coste`, `06.3_Optimizacion_Modelo_Detector`

- Definición de tres modelos finales:  
  1. Académico – maximiza AUC (dataset base).  
  2. Coste – minimiza penalización económica (95 ultimate).  
  3. Detector – maximiza recall de alto riesgo (95 ultimate).  
- Ajuste de hiperparámetros, balanceo y umbrales específicos para cada caso de uso.

---

## 2. Estructura del Proyecto

Este repositorio ha sido unificado y optimizado para su evaluación inmediata:

- **Configuración Local:** El archivo `config.py` gestiona las rutas de forma relativa, permitiendo que el proyecto funcione en cualquier máquina tras ser clonado.
- **Optimización de Datos:** Se ha convertido el dataset SCF 2022 de formato `.dta` (225MB) a `.parquet` (12MB) para garantizar una descarga rápida y evitar límites de tamaño en GitHub, manteniendo la integridad total de los datos.

---

## 3. Instrucciones de Ejecución

Este proyecto ha sido optimizado para ejecutarse tanto en un entorno local como en Google Colab.

### 3.1. Ejecución Local (Recomendado)

Para reproducir los resultados en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/AntonioE/TFM-Digitech.git
   cd TFM-Digitech
   ```

2. **Instalar dependencias:**
   Se recomienda usar un entorno virtual (venv o conda).
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar Notebooks:**
   Inicia Jupyter Lab o Jupyter Notebook:
   ```bash
   jupyter lab
   ```
   Navega a la carpeta `/notebooks` y ejecuta los análisis en el orden numerado.
   
   > **Nota sobre Rutas:** El archivo `config.py` detecta automáticamente la ubicación del proyecto, por lo que no es necesario modificar rutas manualmente.

### 3.2. Ejecución en Google Colab

Si prefieres usar Google Colab:

1. Sube la carpeta `TFM-AntonioEsquinas` a la raíz de tu Google Drive.
2. Abre los notebooks desde la carpeta.
3. El código detectará el entorno y montará Google Drive si es necesario (se han comentado las líneas automáticas para compatibilidad local, pero puedes descomentarlas si el script no detecta el entorno automáticamente).

---

## 4. Estructura del Repositorio

- `notebooks/`: Código fuente de los análisis.
- `data/`: Datos crudos y procesados.
- `models/`: Modelos entrenados guardados.
- `config.py`: Gestión de rutas centralizada.
- `requirements.txt`: Lista de librerías necesarias.



