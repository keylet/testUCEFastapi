import openai
from pydantic import BaseModel


class Document(BaseModel):
        prompt: str = ''

def inference (prompt:str) -> list:
    openai.organization = 'org-cvN58jMk2mDktc3nh8tKnOt7'
    openai.api_key = ''
    print('[PROCESANDO]'.center(40,'-'))

    completion =openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content": """Eres un profesor de programacion para niños, genera una explicacion para el tema que se te proporciona
        E.G: Programación: #ejemmplo dek rol que hara
        -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""}, #ejemmplo del rol que hara E.G
        {"role":"user","content":prompt} #pregunta a realizar
    ]
)

content :  completion.choices[0].message.content
total_tokens = completion.usage.total_tokens

print('[SE TERMINO DE PROCESAR]',center(40,'-'))
return [content, total_tokens]
