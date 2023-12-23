import os
from pathlib import Path
from typing import List

import faiss
import numpy as np
import pandas as pd
import torch
from sentence_transformers import CrossEncoder, SentenceTransformer

EMBEDDER_MODEL = "intfloat/multilingual-e5-large"
RERANKER_MODEL = "PitKoro/cross-encoder-ru-msmarco-passage"


class VacancySearcher:
    vacancy_columns = [
        "title",
        "salary",
        "experience",
        "job_type",
        "description",
        "key_skills",
        "company",
    ]

    def __init__(
        self,
        embedder_model: str = EMBEDDER_MODEL,
        reranker_model: str = RERANKER_MODEL,
    ) -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

        self._embedder = SentenceTransformer(embedder_model, device=device)
        self._reranker = CrossEncoder(reranker_model, max_length=4096, device=device)

        self._vacancies_df = pd.read_csv(os.path.join(os.pardir, "data", "it_jobs.csv"))
        self._faiss_index = faiss.read_index(
            os.path.join(os.pardir, "data", "vacancy.index")
        )

    def search(self, query, top_k: int = 3) -> List[dict]:
        query_vector = self._embedder.encode([query])
        top_k_results = self._faiss_index.search(query_vector, top_k)

        top_k_ids = top_k_results[1].tolist()[0]
        top_k_ids = list(np.unique(top_k_ids))
        search_results = [self._fetch_vacancy_info(idx) for idx in top_k_ids]

        return self._rerank(query, search_results)

    def _fetch_vacancy_info(self, vacancy_idx: int) -> dict:
        info = self._vacancies_df.iloc[vacancy_idx]
        meta_dict = info[self.vacancy_columns].to_dict()
        meta_dict["text"] = info["text"][:1024]

        return meta_dict

    def _rerank(self, query: str, inputs: dict) -> List[dict]:
        model_inputs = [[query, item["text"]] for item in inputs]
        scores = self._reranker.predict(model_inputs)

        ranked_results = [
            {**input, "score": score} for input, score in zip(inputs, scores)
        ]

        return sorted(ranked_results, key=lambda x: x["score"], reverse=True)
