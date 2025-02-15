# Usa un'immagine base con Python
FROM python:3.12

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del progetto nella cartella /app
COPY . .

# Installa le dipendenze
RUN pip install -r requirements.txt

# Espone la porta 8000 (dove gira FastAPI)
EXPOSE 8000

# Comando per avviare il server FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
