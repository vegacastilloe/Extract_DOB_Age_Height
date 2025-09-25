_import pandas as pd
import re
from tabulate import tabulate
#
# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :1].dropna(how='all')
from datetime import datetime

# 🧩 Lista original
if isinstance(df_input, pd.DataFrame):
    df_input = df_input.values.tolist()

def normalizar_df(df):
    df = df.copy()
    for col in df.columns:
        df[col] = df[col].apply(lambda x:
            "" if pd.isna(x) or x is pd.NaT else
            str(int(float(x))) if isinstance(x, (float, int)) and col == 'Age' else
            x.strftime('%m/%d/%Y') if isinstance(x, datetime) and col == 'Date of Birth' else
            str(x)
        )
    return df

# 🧠 Función para verificar con la respuesta esperada
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual == df_expected
    return pd.concat([df_actual, df_expected, comparison], axis=1)


# 🎯 Función para extraer fecha y formatearla como MM/DD/YYYY
def extract_dob(text, edad=None):
    # MM/DD/YY or MM/DD/YYYY
    mdy = re.search(r'\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b', text)
    if mdy:
        m, d, y = mdy.groups()
        if len(y) == 2:
            y_int = int(y)
            if edad and (datetime.today().year - (2000 + y_int)) == int(edad):
                y = str(2000 + y_int)
            else:
                y = str(1900 + y_int)
        return f"{int(m):02d}/{int(d):02d}/{y}"

    # Textual format: 12th February 2001
    text_date = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b', text)
    if text_date:
        d, month_str, y = text_date.groups()
        m = datetime.strptime(month_str, '%B').month
        return f"{m:02d}/{int(d):02d}/{y}"

    return None

# 🎂 Función para extraer edad explícita
def extract_age(text):
    match = re.search(r'(?<!\')(\d{1,2})(?:\.\d+)?\s+years\s+old', text)
    if match:
        return match.group(1)

    # 🆕 Captura frases tipo "at just 22" o "just 22"
    match_alt = re.search(r'\bat\s+just\s+(\d{1,2})(?:\.\d+)?\b', text)
    if match_alt:
        return match_alt.group(1)

    return None

# 🎯 Función para extraer altura
def extract_height(text):
    match = re.search(r'\b\d{1,2}\'\d{1,2}"', text)
    return match.group(0) if match else None

# 🧼 Parsing principal
fechas, edades, alturas = [], [], []

for fila in df_input:
    texto = fila[0]
    fechas.append(extract_dob(texto))
    edades.append(extract_age(texto))
    alturas.append(extract_height(texto))

# 📊 Crear DataFrame
df_result = pd.DataFrame({
    'Date of Birth': fechas,
    'Age': edades,
    'Height': alturas
})
df_result_normalizado = normalizar_df(df_result)

# 🧪 Comparación con columnas esperadas
test = df_raw.iloc[:, 1:].copy()
test['Date of Birth'] = test['Date of Birth'].apply(lambda x: x.strftime('%m/%d/%Y') if pd.notna(x) else None)
test['Age'] = test['Age'].apply(lambda x: str(int(float(x))) if pd.notna(x) else None)
test['Height'] = test['Height'].apply(lambda x: str(x) if pd.notna(x) else None)

test_normalizado = normalizar_df(test)
df_final = compare_with_expected(df_result_normalizado, test_normalizado)

#df_final = compare_with_expected(df_result, test)
print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))

# Limpieza opcional
del df_result, df_final, fechas, edades, alturas

# 💾 Exportación opcional
# df_input.to_excel("Extract_DOB_Age_Height_output.xlsx", index=False)
