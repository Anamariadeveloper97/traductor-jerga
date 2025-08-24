# 💻✨ Traductor de Jerga Técnica a Lenguaje Sencillo

> Una herramienta pensada para ayudar a desarrolladores **junior** (y no tan junior 😅)  
> a entender documentación técnica complicada o código *legacy* sin morir en el intento.  

---

## 🌟 Características

✅ **Traduce jerga técnica a lenguaje simple** (gracias a OpenAI 🤖).  
✅ **Interfaz bonita** con fondo animado, corazones 💜 y rayos ⚡.  
✅ **Dictado por voz**: pega texto o simplemente dicta con 🎤.    
✅ **Botones animados** que hacen tu experiencia más divertida.  
✅ **Diseño responsive** para usar desde tu laptop o tu celu 📱. 

## 🛠️ Requisitos

- 🐍 **Python 3.9+**
- 📦 Paquetes: `flask`, `openai`, `python-dotenv` (para despliegue en Render)
- Una **API Key de OpenAI** (guárdala como variable de entorno)

## 🚀 Ejecución Local

### 1️⃣ Clonar el proyecto
```bash
git clone https://github.com/Anamariadeveloper97/traductor-jerga.git
cd traductor-jerga 

2️⃣ Crear entorno virtual (opcional pero recomendado)
python -m venv venv  - Activar entorno .\venv\Scripts\activate 

3️⃣ Instalar dependencias
pip install flask  
pip install openai
pip install python-dotenv
4️⃣ Configurar tu API Key

En Linux / Mac:

export OPENAI_API_KEY="tu_api_key_aqui"

En Windows (PowerShell):

setx OPENAI_API_KEY "tu_api_key_aqui" 
 
5️⃣ Ejecutar la aplicación
python app.py