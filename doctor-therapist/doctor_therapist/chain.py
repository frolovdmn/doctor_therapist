from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            'system',
            'Ты - русскоязычный лечащий врач. тебе надо узнать как можно больше о жалобах человека на здоровье и \
            попытаться ему помочь',
        ),
        (
            'ai', 
            'Здравствуйте! Как я могу вам помочь?'
        ),
        MessagesPlaceholder('chat_history'),
        (
            'human', 
            '{text}'
        ),
    ]
)

_model = Ollama(model = 'aya')

chain = _prompt | _model
