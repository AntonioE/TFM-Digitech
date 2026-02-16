# config.py
# ESTE ES EL ARCHIVO CENTRAL DE CONFIGURACIÓN DE RUTAS

from pathlib import Path

# --- La única línea que quizás tengas que cambiar si mueves el proyecto ---
# ROOT_DIR has been updated to use relative path based on this file's location
ROOT_DIR = Path(__file__).resolve().parent

# --- Definimos las carpetas de primer nivel ---
DATA_DIR = ROOT_DIR / 'data'
MODELS_DIR = ROOT_DIR / 'models'
METADATA_DIR = ROOT_DIR / 'metadata'
ARTIFACTS_DIR = ROOT_DIR / 'artifacts'
DOCS_DIR = ROOT_DIR / 'docs'
NOTEBOOKS_DIR = ROOT_DIR / 'notebooks'

# --- Subcarpetas de DATOS ---
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
ENGINEERED_DATA_DIR = DATA_DIR / 'engineered'
SPLITS_DIR = DATA_DIR / 'splits'

# --- (NUEVO) Subcarpetas para distinguir 'final' vs 'experimentos' ---
# Para datos procesados
FINAL_PROCESSED_DATA_DIR = PROCESSED_DATA_DIR / 'final'
EXP_PROCESSED_DATA_DIR = PROCESSED_DATA_DIR / 'experiments'

# Para datos con ingeniería de características
FINAL_ENGINEERED_DATA_DIR = ENGINEERED_DATA_DIR / 'final'
EXP_ENGINEERED_DATA_DIR = ENGINEERED_DATA_DIR / 'experiments'

# Para modelos
FINAL_MODELS_DIR = MODELS_DIR / 'final'
EXP_MODELS_DIR = MODELS_DIR / 'experiments'

# Para splits
FINAL_SPLITS_DIR = SPLITS_DIR / 'final'
EXP_SPLITS_DIR = SPLITS_DIR / 'experiments' # <-- Opcional, pero bueno para consistencia

# --- AÑADIDO: Para artefactos (pipelines, informes, etc.) ---
FINAL_ARTIFACTS_DIR = ARTIFACTS_DIR / 'final'
EXP_ARTIFACTS_DIR = ARTIFACTS_DIR / 'experiments'


# --- Creación automática de todas las carpetas ---
# Este bloque asegura que todas las carpetas definidas existan.
# Se ejecuta solo una vez cuando se importa el archivo de configuración.
_DIRECTORIES_TO_CREATE = [
    DATA_DIR, MODELS_DIR, METADATA_DIR,
    ARTIFACTS_DIR, DOCS_DIR, NOTEBOOKS_DIR,
    RAW_DATA_DIR, PROCESSED_DATA_DIR,
    ENGINEERED_DATA_DIR, SPLITS_DIR,
    FINAL_PROCESSED_DATA_DIR,
    EXP_PROCESSED_DATA_DIR,
    FINAL_ENGINEERED_DATA_DIR,
    EXP_ENGINEERED_DATA_DIR,
    FINAL_MODELS_DIR, EXP_MODELS_DIR,
    FINAL_ARTIFACTS_DIR, EXP_ARTIFACTS_DIR,
    FINAL_SPLITS_DIR, EXP_SPLITS_DIR
]

for path in _DIRECTORIES_TO_CREATE:
    path.mkdir(parents=True, exist_ok=True)

print("Módulo de configuración cargado y estructura de carpetas asegurada.")