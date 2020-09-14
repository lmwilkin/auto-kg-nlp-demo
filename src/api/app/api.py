from collections import defaultdict
import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)

from app.models import (
    RecordRequest,
    RecordResponse,
)


app = FastAPI(
    title="spacy_en",
    version="1.1",
    description="FastAPI written in Python to wrap SpaCy",
)

import spacy
nlp = spacy.load("en_core_web_lg")

import neuralcoref
neuralcoref.add_to_pipe(nlp)

logger = logging.getLogger("gunicorn.error")


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


@app.get("/status")
def read_status():
    """
    Returns a health message for the NER service.
    """
    return {"status": "healthy"}


@app.post("/resolve_coreference", response_model=RecordResponse, tags=["coref"])
async def resolve_coreference(body: RecordRequest):
    """Resolve coreference in a document"""
    doc = nlp(body.text)
    doc = nlp(doc._.coref_resolved)
    return {"data": {"resolved_text": str(doc)},}

