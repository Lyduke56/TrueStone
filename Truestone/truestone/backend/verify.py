import fastapi, uvicorn, spacy, torch, transformers

print("FastAPI:", fastapi.__version__)
print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)

nlp = spacy.load("en_core_web_sm")
doc = nlp("Si Rodrigo Duterte ay nagsalita sa Maynila ngayong araw.")
for ent in doc.ents:
    print(f"  {ent.text!r} → {ent.label_}")
    