from fastapi import FastAPI

app = FastAPI(title="LegalEase API")

@app.get("/")
def home():
    return {"message": "LegalEase API - Gemini 1.5 Pro - Running"}

@app.post("/generate")
def generate_doc(doc_type: str, parties: str, terms: str):
    return {"document": f"Generated {doc_type} for {parties} with terms: {terms}"}
