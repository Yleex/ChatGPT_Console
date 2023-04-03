# ChatGPT API en Python 💬

Este es un asistente virtual desarrollado en Python que utiliza la API de OpenAI para crear conversaciones con el modelo de lenguaje GPT-4-32k.

## Instalación

Para instalar las dependencias necesarias, puedes correr el siguiente comando:

```bash
pip install openai typer[all] rich
```

## Uso

Para utilizar el asistente, simplemente corre el archivo `main.py` y sigue las instrucciones que se muestran en pantalla.

### Comandos

El asistente cuenta con los siguientes comandos:

-   `exit`: salir de la aplicación
-   `new`: empezar una nueva conversación

### Contexto

El asistente cuenta con un contexto predefinido que se muestra a continuación:

```python
context = [
    {
        "role": "system",
        "content": "Eres un asistente muy útil."
    }
]

messages = [context]
```

## Créditos

Este proyecto fue desarrollado por [Yobriel Castillo](https://github.com/yleex) como parte de un ejercicio para practicar el uso de la API de OpenAI y la librería Typer para crear interfaces de línea de comandos en Python.

Si tienes alguna pregunta o comentario, no dudes en contactarme por correo electrónico a [yleexcode@gmail.com](mailto:yleexcode@gmail.com). ¡Gracias por utilizar mi asistente virtual!
