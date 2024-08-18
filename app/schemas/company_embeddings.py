from typing_extensions import Dict, List

from langchain_community.vectorstores import FAISS

from app.models import ObjectId


class CompanyEmbeddingsSchema:
    _id: ObjectId
    company: str
    model: str
    services: List[str]
    embeddings: Dict[str, FAISS]

    def __init__(
        self,
        _id: ObjectId,
        company: str,
        model: str,
        services: List[str],
        embeddings: Dict[str, FAISS],
    ):
        self._id = _id
        self.company = company
        self.model = model
        self.services = services
        self.embeddings = embeddings

    def __str__(self) -> str:
        return (
            "CompanyEmbeddingsSchema(\n\t"
            + f"_id={self._id},\n\t"
            + f"company={self.company},\n\t"
            + f"model={self.model},\n\t"
            + f"services={self.services},\n\t"
            + "embeddings={\n\t"
            + f"\t{self.model}: {self.embeddings[self.model]}\n"
            + "}\n"
            + ")"
        )
