![Cover](/static/images/careerpath-ai.png)

# 🎓 CareerPath AI - AI Career Guidance for Indian Students (Hackathon Project)

CareerPath AI is an AI-powered career guidance platform designed to help Indian students make informed academic and career decisions using **Retrieval-Augmented Generation (RAG)**.

Unlike traditional chatbots, this system generates answers strictly from verified career-related documents, reducing hallucinations and improving trust.

---

## 🚀 Live Demo

🔗 **Live Application:**  
[CareerPath AI](https://career-guidance-rag-app.onrender.com/)

🔗 **GitHub Repository:**  
[Source Code](https://github.com/surajsingh241205/career-guidance-rag)

---

## 🧠 Key Features

- 🎯 Career guidance after 10th, 12th, and graduation
- 🏛️ Government exams and skill-based career suggestions
- 📚 Document-grounded AI responses (RAG-based)
- 🔍 FAISS vector database for efficient retrieval
- ⚡ Fast inference using Groq LLM (LLaMA 3.1)
- 🌐 Deployed and publicly accessible
- 🇮🇳 Designed for the Indian education system

---

## 🏗️ System Architecture

User Query
↓
Flask Web Interface
↓
FAISS Vector Database (Career Documents)
↓
Retriever (Top-k relevant chunks)
↓
Groq LLM (LLaMA 3.1)
↓
Context-aware Career Guidance


---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- LangChain
- FAISS (Vector Database)

### AI / LLM
- Retrieval-Augmented Generation (RAG)
- Groq API (LLaMA 3.1)

### Frontend
- HTML
- Tailwind CSS
- JavaScript

### Deployment
- Render (Cloud Platform)

---

## ⚙️ How It Works

1. Career-related documents are collected and structured.
2. Documents are converted into vector representations.
3. FAISS retrieves the most relevant content based on the user query.
4. The LLM generates responses strictly using retrieved context.
5. The final answer is shown through a web interface.

This ensures **reliable, explainable, and context-aware guidance**.

---

## 🚧 Challenges Faced

- Managing rapid LangChain API changes
- Deploying AI systems on free cloud tiers
- Avoiding heavy GPU dependencies
- Ensuring consistency between ingestion and retrieval
- Designing a scalable RAG pipeline

---

## 📘 What I Learned

- End-to-end RAG system implementation
- Practical AI deployment challenges
- Vector database handling
- System-level AI thinking beyond prompt engineering
- Product-focused AI development

---

## 🌱 Future Improvements

- User login and personalized student profiles
- Suggested career recommendation cards
- Multilingual support (Hindi & regional languages)
- Resume and marksheet analysis
- Admin dashboard for updating career knowledge
- Analytics on student career trends

---

## ⚠️ Disclaimer

This project is intended for educational guidance purposes only  
and does not replace professional career counseling.

---

## 👨‍💻 Author

**Suraj Singh**  
AI & Data Science Enthusiast  

If you found this project interesting, feel free to ⭐ the repository!

