import spacy

nlp = spacy.load("en_core_web_sm")

def mask_entities(text: str) -> str:
    doc = nlp(text)
    masked = text
    for ent in reversed(doc.ents):
        masked = masked[:ent.start_char] + f"[{ent.label_}]" + masked[ent.end_char:]
    return masked