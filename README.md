# 🧠 GENAI_Project – Advanced MCQ Generator Using Generative AI

An AI-powered full-stack web application that automatically generates Multiple Choice Questions (MCQs) from web articles using Natural Language Processing (NLP) and Generative AI. Designed for educators, students, and trainers, this tool streamlines assessment creation with intelligent, customizable questions.

---

## 🚀 Features

- 🌐 **URL-based Content Extraction** – Scrapes meaningful content from webpages using BeautifulSoup.
- 🤖 **AI-driven Question Generation** – Generates high-quality MCQs using OpenAI GPT models and SpaCy NLP techniques.
- 🎚️ **Custom Generation Settings** – Tailor your quiz with:
  - Number of Questions
  - Difficulty Level (Easy / Medium / Hard)
  - Number of Correct Answers
  - Temperature Control (AI creativity)
- 🧠 **Hints and Explanations** – Enhances understanding with helpful hints and explanations for each question.
- 📄 **PDF Export** – Export MCQs with or without answers for offline usage.
- 🔐 **Secure Authentication** – Login system using JWT tokens.
- 🧾 **Session Management** – Save your generated content securely using MongoDB.
- 🧪 **Tested Workflow** – Robust input handling, grammar checks, and end-to-end generation validation.

---

## 📸 Screenshots
### 🔐 Login  
![Login](https://github.com/user-attachments/assets/a4128783-8daf-4007-a250-09f3c0224a73)

### 🎛️ MCQ Settings Panel  
![Settings](https://github.com/user-attachments/assets/49586d8c-0433-4e2e-ab6f-c638540507db)  
![Settings 2](https://github.com/user-attachments/assets/651e7c31-5a48-43c2-8996-c8604bcddcc4)  
![Settings 3](https://github.com/user-attachments/assets/0b5a507a-6eb8-48f2-bf0e-93a5baeb62ba)

### 🧾 Generated Questions Preview  
![Questions](https://github.com/user-attachments/assets/d33ebd20-abcb-4470-879e-3495b51bbaca)  
![Questions 2](https://github.com/user-attachments/assets/92a3433d-d43b-4fc4-8761-e9cba993b408)

### 📤 PDF Export View  
![PDF Export](https://github.com/user-attachments/assets/efe66e2a-fd90-4aa3-b75f-9c856d840d65)

### 🌐 Extract Questions from URL  
![Extract](https://github.com/user-attachments/assets/c38559c2-7c26-4eca-9356-60244681cb1e)

---

## 🛠️ Tech Stack

### 🔧 Frontend
- **React.js** – Modern UI with reusable components
- **Tailwind CSS** – Utility-first styling
- **Material UI** – Pre-built responsive components
- **Streamlit** – Used optionally for simplified front-end visualization

### ⚙️ Backend
- **Django** – High-level Python web framework
- **Django REST Framework** – For building RESTful APIs
- **BeautifulSoup** – Web scraping library
- **SpaCy** – NLP engine for named entity recognition
- **OpenAI GPT API** – Generative AI for question and explanation generation
- **PyMongo** – Python driver for MongoDB

### 🗄️ Database
- **MongoDB** – NoSQL database for storing users and generated MCQs

### 🔐 Authentication
- **JWT (JSON Web Tokens)** – Secure, stateless authentication

---

## 📐 Project Architecture

```plaintext
User Input (URL + Settings)
        ↓
Content Scraper (BeautifulSoup)
        ↓
NLP Pipeline (SpaCy)
        ↓
AI Question Generator (OpenAI GPT API)
        ↓
Question Formatting + Explanation
        ↓
Frontend Display + PDF Export
✅ Testing Overview
🧪 Testing Strategy
Input validation for multiple URL types and content formats

Relevance and grammar accuracy of AI-generated MCQs

End-to-end validation from login → generate → export

🧪 Testing Types
Unit Testing: Scraping, NLP, and MCQ generation logic

Integration Testing: Django API ↔ React frontend communication

Performance Testing: Handles large web pages and fast generation

User Testing: Usability and interface feedback

📈 Results
✅ Generates context-aware MCQs with logical distractors and feedback
💬 Includes quality explanations and optional hints
⚡ Fast and scalable performance across platforms
🧠 Handles edge cases like minimal or noisy text inputs

🔮 Future Enhancements
📚 Domain-specific tuning (Science, History, Technology, etc.)
🧠 AI-based automatic difficulty classification
🎤 Speech or 🖼️ Image-based content input
🌍 Multilingual MCQ generation (via multilingual NLP models)
📊 Analytics & Feedback System for improving question quality

🧩 Getting Started
⚙️ Prerequisites
Python 3.9+
Node.js 18+
MongoDB (Local or Atlas)
OpenAI API Key (for GPT usage)

🚀 Backend Setup
cd backend
pip install -r requirements.txt
python manage.py runserver

💻 Frontend Setup
cd frontend
npm install
npm run dev

👨‍💻 Contributors
Ansh Agarwal – Full Stack Developer
📧 Email: agarwalansh651@gmail.com

📜 License
This project is licensed under the MIT Licens
