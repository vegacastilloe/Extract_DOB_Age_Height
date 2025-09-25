# Extract DOB Age Height

![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Extract_DOB_Age_Height)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 809 ---
- 🌟 **Author**: Excel (Vijay A. Verma) BI

    - Extract Date of Birth, Age and Height. Date of birth will appear either in MDY format or in text format as 12th February 2001. Heights will always be in foot inches format like 5'10". Give age in completed years only not in decimals.

 🔰 Este proyecto demuestra cómo extraer información estructurada desde texto libre, respetando la fidelidad del contenido original. Ideal para parsing, validación y enseñanza.

 🔗 Link to Excel file:
 👉 https://lnkd.in/dpjTcabx

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Extract_DOB_Age_Height/blob/main/extract_dob_age_height.py

---
---

## 🧠 Extract DOB Age Height

Este proyecto demuestra cómo extraer información estructurada desde texto libre, respetando la fidelidad del contenido original. Ideal para parsing, validación y enseñanza.


## 📦 Requisitos

- Python 3.9+
- Paquetes:
- pandas
- openpyxl (para leer .xlsx)
- tabulate (solo para impresión bonita)
- Archivo Excel con al menos:
    - La columna 1: `String`.
    - Desde la columna 2 en adelante: resultados esperados para comparación

---

## ✨ ¿Qué hace?

- Extrae **fecha de nacimiento**, **edad explícita** y **altura** desde frases tipo:
  > `"Rohan is 5'10\" tall and was born on 14th March 1995, making him 30 years old."`
- Compara los resultados extraídos contra un DataFrame esperado.
- Normaliza formatos para comparación transparente.
- Muestra una tabla con resultados, esperados y verificación booleana.

## 🧩 Componentes

### 1. `extract_dob(text, edad)`
Extrae fechas en formato `MM/DD/YY` o textual (`14th March 1995`). Si el año tiene 2 dígitos, lo ajusta según la edad explícita.

### 2. `extract_age(text)`
Captura frases como `"30 years old"` o `"at just 22"`.

### 3. `extract_height(text)`
Detecta alturas tipo `5'10"`.

### 4. `normalizar_df(df)`
Convierte fechas, edades y alturas a strings comparables. Limpia nulos (`None`, `NaN`, `NaT`) como `""`.

### 5. `compare_with_expected(df_actual, df_expected)`
Compara dos DataFrames y devuelve uno combinado con:
- Resultado extraído
- Resultado esperado
- Comparación booleana por columna

## 🧪 Ejemplo de uso

```python
df_result = pd.DataFrame({
    'Date of Birth': [...],
    'Age': [...],
    'Height': [...]
})

df_result_normalizado = normalizar_df(df_result)
df_expected_normalizado = normalizar_df(df_expected)

df_final = compare_with_expected(df_result_normalizado, df_expected_normalizado)
```
## 📊 Visualización
```python
from tabulate import tabulate
print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))
```
## 🧼 Limpieza opcional
```python
del df_result, df_final, fechas, edades, alturas
```
## 🧠 Filosofía
Este script respeta la regla de oro del parsing fiel:

“Solo extraer lo que está presente en el texto. Si no está, se deja vacío.”

Ideal para portafolios técnicos, enseñanza de regex, validación de modelos NLP y debugging transparente.

---
## 📄 Licencia

Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.

---
