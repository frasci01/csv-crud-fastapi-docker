from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

CSV_FILE = "data.csv"

# Se il file non esiste, lo creiamo con le intestazioni corrette
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["id", "nome", "cognome", "codice_fiscale"])
    df.to_csv(CSV_FILE, index=False)

# Funzione per leggere il CSV
def read_csv():
    return pd.read_csv(CSV_FILE)

# Funzione per scrivere nel CSV
def write_csv(df):
    df.to_csv(CSV_FILE, index=False)

# **CREATE: Aggiungere un nuovo record**
@app.post("/items/")
async def create_item(id: int, nome: str, cognome: str, codice_fiscale: str):
    df = read_csv()
    
    if str(id) in df["id"].astype(str).values:
        raise HTTPException(status_code=400, detail="ID già esistente")
    
    new_record = pd.DataFrame([[id, nome, cognome, codice_fiscale]], columns=df.columns)
    df = pd.concat([df, new_record], ignore_index=True)
    write_csv(df)
    
    return {"id": id, "nome": nome, "cognome": cognome, "codice_fiscale": codice_fiscale}

# **READ: Ottenere tutti i record**
@app.get("/items/")
async def get_all_items():
    df = read_csv()
    return df.to_dict(orient="records")

# **READ: Ottenere un singolo record per ID**
@app.get("/items/{id}")
async def get_item(id: int):
    df = read_csv()
    record = df[df["id"] == id]
    
    if record.empty:
        raise HTTPException(status_code=404, detail="Record non trovato")
    
    return record.to_dict(orient="records")[0]

# **UPDATE: Aggiornare un record**
@app.put("/items/{id}")
async def update_item(id: int, nome: str, cognome: str, codice_fiscale: str):
    df = read_csv()
    
    if id not in df["id"].values:
        raise HTTPException(status_code=404, detail="Record non trovato")
    
    df.loc[df["id"] == id, ["nome", "cognome", "codice_fiscale"]] = [nome, cognome, codice_fiscale]
    write_csv(df)
    
    return {"id": id, "nome": nome, "cognome": cognome, "codice_fiscale": codice_fiscale}

# **DELETE: Eliminare un record**
@app.delete("/items/{id}")
async def delete_item(id: int):
    df = read_csv()
    
    if id not in df["id"].values:
        raise HTTPException(status_code=404, detail="Record non trovato")
    
    df = df[df["id"] != id]
    write_csv(df)
    
    return {"message": "Item deleted successfully"}

# **COUNT: Ottenere il numero di righe nel CSV**
@app.get("/items/count")
async def count_items():
    df = read_csv()
    return {"count": len(df)}
