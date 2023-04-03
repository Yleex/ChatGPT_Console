import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table


def main():

  openai.api_key = "ApiKey creada en https://platform.openai.com"

  print("{bold green}ChatGPT API en Python{/bold green}💬")

  table=Table("Comando", "Descripción")
  table.add_row("exit", "Salir de la application")
  table.add_row("new", "Empezar una nueva conversacion")

  print (table)

  # Context del asistente
  context=[{"role":"system",
            "content": "Eres un asistente muy útil."}]
  messages=[context]

  while True:

    content=__prompt()

    if content=="new":
       print("🤖Nueva Conversación Creada!")
       messages=[context]
       content=__prompt()

    messages.append({"role":"user",
                    "content": content})

    response=openai.ChatCompletion.create(
        model="gpt-4-32k",messages=messages)
    
    response_content=response.choices[0].message.content
    
    messages.append({"role":"assistant", "content": response_content})

    print("f[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
   prompt=typer.prompt("\n¿Sobre qué quieres háblar? ")

  if prompt=="exit":
    exit=typer.confirm("✋ ¿Estás seguro?")
    if exit:
      print ("Adios✋")
      raise typer.Abort()

    return __prompt()
 
if __name__ == "__main__":
  typer.run(main)

  # Creator Yobriel Castillo (YLEEX)
  # yleexcode@gmail.com 