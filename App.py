# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 20:11:43 2025

@author: Ramfis
"""

import streamlit as st
from pathlib import Path
from utils import *
from AI_agent import text_agent
import re
import time

st.title('Asistente Resumen de textos')

st.info("""Este asistente recibira texto en formatos word, txt, pdf o ingresados manualmente. 
        \n Posteriormente, resumira la informacion del texto y dara palabras clave del mismo""")

toggle=st.toggle('Sube un archivo o ingresa un texto')

if toggle:
    
    file = st.file_uploader('Sube tu archivo aqui', type=['docx','txt','pdf'])
        
    if file:
        file_ext=Path(file.name).suffix
        text_final=read_file(file, file_ext)
        start=time.time()
        ai_reply=text_agent({'text_file':text_final})
        final_reply=re.sub("<think>.*?</think>","",ai_reply['text_reply'],flags=re.DOTALL)
        ext_time=time.time() - start
        st.info(f'El programa tomo {ext_time} en ejecutar')
        st.write(final_reply)
    else:
        st.info('Esperando ingresar el texto')

else:
    
    text_final = st.text_input('Ingresa tu texto manualmente aqui')
    
    if text_final != '':

        start=time.time()
        ai_reply=text_agent({'text_file':text_final})
        final_reply=re.sub("<think>.*?</think>","",ai_reply['text_reply'],flags=re.DOTALL)
        ext_time=time.time() - start
        st.info(f'El programa tomo {ext_time} en ejecutar')
        st.write(final_reply)
    else:
        st.info('Esperando ingresar el texto')
    