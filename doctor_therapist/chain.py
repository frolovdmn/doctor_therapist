from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, FewShotChatMessagePromptTemplate

model = Ollama(model = 'aya')

examples = [
    {
        'input': 'У меня болит голова, что может мне помочь?',
        'output': 'Опишите, пожалуйста, где конкретно вы ощущаете боль и как можно ее охарактеризовать?'
    },
    {
        'input': 'Сколько времени желательно ездить за рулем без вреда для здоровья в день?',
        'output': 'Для мужчин вообще желательно как можно меньше, в общей сумме 1,5-2 часа, так как в дальнейшем при нагревании яичек, велика в будущем вероятность бесплодия'
    },
    {
        'input': 'Здравствуйте, в последнее время по ночам просыпаюсь от сильного сердцебиения. Начинают потеть ладожки. Отрыжка. Вздутие живота. Тяжело дышать. Шею не могу повернуть, между лопатками также хруст',
        'output': 'Здравствуйте, нужно начать с обследования ЖКТ, следить за питанием, и, возможно, сменить подушку',
    },
    {
        'input': 'После еды или воды стоит ком в горле, как будто поднимается из желудка. Есть приступы тошноты и рвота. Моча стала цветом крепкого чая. Пожелтели глазные яблоки',
        'output': 'Здравствуйте. Сделайте УЗИ брюшной полости, сдайте кровь на биохимический анализ (билирубин общий, прямой, непрямой, АЛТ, АСТ, ЛДГ, общий белок), покажитесь гастроэнтерологу'
    },
    {
        'input': 'Гормональный сбой, с чем это связано? И как зачать ребенка если месячные будут так прыгать?',
        'output': 'Здравствуйте, для того, чтобы выяснить причину гормонального сбоя, надо сдать анализы на гормоны. Для этого посетите гинеколога. Беременность может наступить, даже если цикл будет прыгать.'
    }
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ('human', '{input}'),
        ('ai', '{output}'),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt = example_prompt,
    examples = examples
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            'system',
            'Ты - русскоязычный лечащий врач. тебе надо узнать как можно больше о жалобах человека на здоровье и \
            попытаться ему помочь. Если тебя нужно уточнить информацию, воспользуйся Wikipedia. Если нужна более \
            специфичная информация медицинской тематики, воспользуйся PubMed. Если релевантная информация найдена, \
            то дай ответ, основываясь на ней. Если релевантной информации не будет, то дай ответ, полагаясь на свои \
            знания. Вот несколько примеров:',
        ),
        (
            'ai', 
            'Здравствуйте! Чем я могу вам помочь?'
        ),
        few_shot_prompt,
        MessagesPlaceholder('chat_history'),
        (
            'human', 
            '{text}'
        ),
    ]
)

chain = prompt | model