import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAI


def tellme_a_joke():
    try:
        # Crea una instancia de Azure OpenAI
        llm = AzureOpenAI(
            deployment_name=os.environ["OPENAI_DEPLOYMENT_NAME"],
            model_name=os.environ[
                "OPENAI_DEPLOYMENT_NAME"
            ],  # Debe ser igual que deployment_name
            api_version=os.environ["OPENAI_API_VERSION"],
        )

        # Ejecuta el LLM y captura la respuesta
        joke = llm.invoke("Cuentame un chiste")

        # Imprime el chiste por consola
        print(joke)

    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Imprime el error para depuración


if __name__ == "__main__":
    load_dotenv()

    # Imprime todas las variables de entorno para depuración
    # print(os.environ)  # Esto te ayudará a verificar que las variables estén correctas

    tellme_a_joke()
