# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 20:42:34 2025

@author: Ramfis
"""

import fitz
import docx


def read_pdf(file):
    doc_pdf=fitz.open(stream=file.read())
    full_text=[]
    for page in doc_pdf:
        text=page.get_text()
        full_text.append(text)
    return '\n'.join(full_text)

def read_word(file):
    doc_doc = docx.Document(file)
    full_text=[]
    for text in doc_doc.paragraphs:
        full_text.append(text.text)
    print('\n'.join(full_text))
    return '\n'.join(full_text)

def read_txt(file):
    return file.read().decode("utf-8")
    
def read_file(file, file_ext):
    if file_ext == '.pdf':
        return read_pdf(file)
    elif file_ext == '.docx':
        return read_word(file)
    elif file_ext == '.txt':    
        return read_txt(file)
    else:
        return 'Extension incorrecta, intenta de nuevo'