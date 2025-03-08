# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 20:51:32 2025

@author: Ramfis
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

llm=OllamaLLM(model='deepseek-r1:8b')
prompt = PromptTemplate(input_variables=['text_file'], template="""
                                         Eres un experto en archivos de texto multibilingue.
                     Tu funcion es poder recibir el texto completo de diferentes tipos de documentos: word, txt o pdf y dar un resumen del contenido del texto.
                     Ademas, debes dar SOLO cinco palabras clave de la informacion contenida en el texto y un fragmento en el cual podamos ver en que parte del texto podemos
                     encontrar esa palabra clave o la referencia a esa palabra clave

                     Informacion a resumir: {text_file}

                     El formato de tu respuesta debe ser siempre el siguiente y en este orden:
                     
                     Resumen general del texto: (En esta seccion solo debe darse un resumen general de todo el texto)

                     Lista de palabras clave del texto: 
                         - palabra clave 1 : (parte del texto donde aparece la palabra clave o su referencia)
                         - palabra clave 2 : (parte del texto donde aparece la palabra clave o su referencia)
                         - palabra clave 3 : (parte del texto donde aparece la palabra clave o su referencia)                     
                                         """
    )
    
text_agent=LLMChain(llm=llm,prompt=prompt, output_key="text_reply")