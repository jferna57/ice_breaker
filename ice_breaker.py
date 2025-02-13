from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
import os
from rich.console import Console
from rich.markdown import Markdown

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
        given the linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
        3. how many people conections has
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template  # Cambiado a lista
    )
    
    # llm = ChatOllama(model="deepseek-r1:1.5b")

    # llm = AzureChatOpenAI(
    #     temperature=0,
    #     model_name=os.environ["OPENAI_DEPLOYMENT_NAME"]
    # )
    
    llm = ChatGroq(
        temperature=0,
        model="llama3-8b-8192"
    )

    information = scrape_linkedin_profile('https://www.linkedin.com/in/jferna57', True)
    
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    # Verificar el tipo de `res` y extraer el texto de la respuesta (si es necesario)
    # print("Generated response:", res)

    # Asegúrate de extraer el texto del objeto AIMessage
    if hasattr(res, "text"):
        response_text = res.text
    else:
        response_text = str(res)  # Si no tiene el atributo 'text', convierte a string

    # Para imprimir texto Markdown de forma estructurada
    markdown = Markdown(res.content)  # Usa el texto extraído
    console = Console()
    console.print(markdown)
