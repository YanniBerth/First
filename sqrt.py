import openai

# Definir la clave API directamente como una variable
openai.api_key = "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"  # Reemplaza con tu clave API real

# Crear una función para generar código a través de ChatGPT
def generar_codigo(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # O gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Eres un ayudante que genera código Python."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Guardar el código generado en un archivo
def guardar_codigo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as file:
        file.write(contenido)

# Ejemplo de uso
prompt = "Genera un código en Python que calcule la raíz cuadrada de un número."
codigo_generado = generar_codigo(prompt)

# Guardar el código en un archivo .py
guardar_codigo('codigo_generado.py', codigo_generado)

print(f"Código generado y guardado en codigo_generado.py")
