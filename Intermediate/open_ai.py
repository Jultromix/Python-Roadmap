from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()


def analize_news_with_ai(articles: list[dict], query: str) -> str | None:

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    context = "\n".join(
        [
            # f"- {article['title']} : {article.get('description', '')[:100]}..."
            # for article in articles[:10]  # Limitar para control de costos
            f"- {article.get('title')} : {(article.get('description') or '')[:100]}..."
            for article in articles[:5]
        ]
    )

    print("this is the context", context)

    prompt = f"""
        Based on this news :
        {context}

        Question: {query}
        Answer concisely in spanish
    """

    response = client.responses.create(
        model="gpt-5.2",
        instructions="You are a coding assistant reads a context and answers briefly",
        input=prompt,
    )

    print(response.output_text)
    return None
