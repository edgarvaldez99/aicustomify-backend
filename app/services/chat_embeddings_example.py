from typing import List
import os

from openai import OpenAI
from pandas import read_csv, DataFrame  # type: ignore

from app.constants import DEFAULT_LLM_NAME, OPENAI_KEY
from app.repositories import create_company_embeddings, get_company_embeddings


client = OpenAI(api_key=OPENAI_KEY)


def get_dataframe_by_csv(filename="texto.csv") -> DataFrame:
    path = os.path.dirname(os.path.realpath(__file__))
    service_df = read_csv(f"{path}/{filename}")
    return service_df


def search_text_in_service(search_text: str) -> str | None:
    service_df = get_dataframe_by_csv("comidas_ricas_sa_services_example.csv")
    services: List[str] = service_df["Servicios"].tolist()
    company_embeddings = get_company_embeddings("comidas ricas sa")
    if company_embeddings is None:
        company_embeddings = create_company_embeddings(
            "comidas ricas sa",
            services,
            model=DEFAULT_LLM_NAME,
        )
    knowledge_base = company_embeddings.embeddings.get(DEFAULT_LLM_NAME, None)
    if knowledge_base is None:
        return None
    documents = knowledge_base.similarity_search(search_text, 3)
    if len(documents) == 0:
        return None
    context = ". ".join([ctx.page_content for ctx in documents])
    instructions = f"Responde a la pregunta del usuario dentro de este contexto: {context}"  # noqa: E501
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": instructions,
            },
            {"role": "user", "content": search_text},
        ],
    )
    msg = response.choices[0].message.content
    return msg
