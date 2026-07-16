from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

print("=" * 50)
print("Chat com a OpenAI")
print("Digite 'sair' para encerrar o programa.")
print("=" * 50)

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        print("\nPrograma encerrado. Até logo!")
        break

    try:
        resposta = client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.7,
            max_tokens=200,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um professor de Python. "
                        "Explique as respostas de forma clara, simples e objetiva."
                    )
                },
                {
                    "role": "user",
                    "content": pergunta
                }
            ]
        )

        print("\nIA:")
        print(resposta.choices[0].message.content)

    except Exception as erro:
        print("\nOcorreu um erro:")
        print(erro)