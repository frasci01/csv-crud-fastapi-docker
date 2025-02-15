# csv-crud-fastapi-docker
exercise for Social Thingum

# 📊 CSV CRUD API con FastAPI e Docker

Questo progetto fornisce un'API REST basata su **FastAPI** per gestire operazioni CRUD su un file CSV.  
L'API è containerizzata con **Docker** e permette di aggiungere, leggere, aggiornare ed eliminare record da un file CSV.

---

## 🚀 Funzionalità
✅ Aggiungere un record al CSV (`POST /items/`)  
✅ Ottenere tutti i record (`GET /items/`)  
✅ Ottenere un record per ID (`GET /items/{id}`)  
✅ Aggiornare un record (`PUT /items/{id}`)  
✅ Eliminare un record (`DELETE /items/{id}`)  
✅ Contare i record nel CSV (`GET /items/count`)  

---

## 🛠️ Requisiti
Prima di iniziare, assicurati di avere installato:  
- **Python 3.10+**  
- **FastAPI & Uvicorn**  
- **Docker (opzionale, per containerizzazione)**  

Se non hai Docker, installalo da qui: [Docker Desktop](https://www.docker.com/products/docker-desktop).

---

## ⚡ Installazione e Avvio

### **1️⃣ Clonare il repository**
git clone https://github.com/tuo-username/csv-crud-fastapi-docker.git
cd csv-crud-fastapi-docker

### **2️⃣ Creare l'ambiente virtuale**
conda create --name project python=3.10
conda activate project

### **3️⃣ Installare le dipendenze**
pip install -r requirements.txt

### **3️⃣ Avviare il server FastAPI**
uvicorn app:app --reload

Ora l'API è disponibile su:
👉 http://localhost:8000

🐳 Eseguire con Docker
1️⃣ Costruire l'immagine Docker
docker build -t csv-crud-fastapi .
2️⃣ Avviare il container
docker run -p 8000:8000 csv-crud-fastapi

📂 Struttura del Progetto
csv-crud-fastapi/
│── app.py                # API FastAPI
│── data.csv              # File CSV con i dati
│── Dockerfile            # Configurazione Docker
│── requirements.txt      # Dipendenze Python
│── README.md             # Documentazione
