
# IA-Generative 🧠✨

Ce projet est une application web d'**IA générative** qui permet de générer du texte en utilisant le modèle **GPT-2**.  
Il est composé de deux parties :

- Un **backend** en Python avec **FastAPI**
- Un **frontend** en **Angular**

---

## ⚙️ Fonctionnalités

- Génération de texte à partir d'un prompt utilisateur
- Historique des requêtes et réponses (limité aux 10 dernières)
- Interface utilisateur simple avec textarea et liste des résultats
- Appels API sécurisés avec CORS

---

## 📁 Structure du projet

```
IA-Generative/
├── main.py            # Backend FastAPI
├── fastapi-angular/   # Frontend Angular
│   └── app/
│       └── app.component.ts
│       └── app.component.html
│       └── app.component.sass
├── README.md
```

---

## 🚀 Démarrer le projet

### 🔧 Prérequis

- **Python 3.12**
- **Node.js** (Angular)
- **Angular CLI**

### 1. Installation du backend

```bash
pip install fastapi uvicorn transformers
```

#### Lancer le serveur FastAPI

```bash
uvicorn main:app --reload
```

Le backend sera accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000)

> Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 2. Installation du frontend Angular

```bash
cd fastapi-angular
npm install
npm start
```

L'interface sera disponible sur [http://localhost:4200](http://localhost:4200)

---

## 📡 API Endpoints

### `POST /generate/`

Génère du texte à partir d'un prompt.

#### Exemple de requête :

```json
{
  "prompt": "Il était une fois"
}
```

#### Exemple de réponse :

```json
{
  "generated_text": "Il était une fois une princesse dans un château lointain...",
  "history": [
    {
      "prompt": "Il était une fois",
      "response": "Il était une fois une princesse..."
    }
  ]
}
```

---

### `GET /history/`

Récupère l'historique des 10 dernières générations de texte.

---

## 🧠 Modèle utilisé

- [`gpt2`](https://huggingface.co/gpt2) via [Hugging Face Transformers](https://github.com/huggingface/transformers)
- Chargé avec :  
  ```python
  pipeline("text-generation", model="gpt2")
  ```

---

## 🔒 CORS

Le backend autorise uniquement l'origine suivante :

```python
origins = [
    "http://localhost:4200"
]
```

---

## 📄 Licence

Ce projet est open-source. Utilisation libre à des fins personnelles ou pédagogiques.

---

**Développé avec ❤️ en FastAPI & Angular**
