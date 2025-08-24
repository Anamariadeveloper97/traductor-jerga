# app.py
from flask import Flask, render_template, request, jsonify # servidor y utilidades web
from openai import OpenAI                                 # SDK oficial de OpenAI
from dotenv import load_dotenv                            # para leer .env (opcional)
import os                                                 # utilidades del sistema

load_dotenv()                    # carga variables de .env si existe; opcional
app = Flask(__name__)            # crea la app Flask
client = OpenAI()                # instancia el cliente; toma OPENAI_API_KEY del entorno

def system_prompt():
    # Instrucciones breves para la "traducción" a lenguaje sencillo
    return (
        "Eres un traductor de jerga técnica a español claro para devs junior. "
        "Explica con ejemplos simples, bullets y analogías cortas. "
        "Si hay código, describe qué hace en pasos. "
        "Evita palabreo; sé preciso y amable."
    )

@app.get("/")                                             # ruta principal: sirve la página
def index():
    return render_template("index.html")

@app.post("/explain")                                     # endpoint que procesa el texto
def explain():
    data = request.get_json(silent=True) or {}            # lee JSON del fetch
    text = (data.get("text") or "").strip()               # texto del usuario
    if not text:
        return jsonify({"error": "Por favor pega algún texto."}), 400

    try:
        # Llamada al Responses API: modelo + input (system + user)
        # output_text: helper del SDK para quedarnos con el texto plano resultante.
        # Doc: ver Responses API y output_text en guías. 
        # (Parámetros mínimos para mantenerlo simple)
        resp = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": system_prompt()},
                {"role": "user", "content": text},
            ],
        )
        explanation = resp.output_text  # texto final ya listo para mostrar
        return jsonify({"explanation": explanation})
    except Exception as e:
        # En producción, loguea e detalla mejor; aquí devolvemos mensaje breve.
        print("Error OpenAI:", e)
        return jsonify({"error": "Ocurrió un problema al pedir la explicación."}), 500

if __name__ == "__main__":       # arranque local
    app.run(debug=True)          # debug=True para dev; quítalo en prod
