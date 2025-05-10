# GENAI_Project-Advanced-MCQ-Generator
# 🧠 Advanced MCQ Generator Using Generative AI

An AI-powered full-stack web application that automatically generates Multiple Choice Questions (MCQs) from web articles using Natural Language Processing and Generative AI. Built for educators, students, and trainers to simplify assessment creation with intelligent, customizable questions.

---

## 🚀 Features

- 🌐 **URL-based Content Extraction** – Scrape text from any user-provided webpage using Beautiful Soup.
- 🤖 **AI-powered Question Generation** – Automatically generate context-aware and grammatically valid MCQs using SpaCy + custom logic.
- 🎚️ **Custom Generation Settings** – Choose:
  - Number of Questions
  - Difficulty Level (Easy / Medium / Hard)
  - Number of Correct Answers per Question
  - Temperature Control (to adjust AI randomness)
- 📝 **Answer Explanations & Hints** – Every question includes detailed feedback and an optional hint for learning reinforcement.
- 📄 **Download as PDF** – Export question sets as PDF with or without answers.
- 🔐 **JWT Authentication** – Secure login and user session management.
- 📦 **MongoDB Backend** – Store and retrieve generated questions using a fast and scalable NoSQL database.

---

## 📸 Screenshots

> _Add screenshots here to demonstrate UI, customization panel, MCQ output, and PDF download._

**Example Screenshots:**

### login
![image](https://github.com/user-attachments/assets/a4128783-8daf-4007-a250-09f3c0224a73)


### 🎛️ MCQ Settings Panel  
![image](https://github.com/user-attachments/assets/49586d8c-0433-4e2e-ab6f-c638540507db)
![image](https://github.com/user-attachments/assets/651e7c31-5a48-43c2-8996-c8604bcddcc4)
![image](https://github.com/user-attachments/assets/0b5a507a-6eb8-48f2-bf0e-93a5baeb62ba)


### 🧾 Generated Questions Preview  
![image](https://github.com/user-attachments/assets/d33ebd20-abcb-4470-879e-3495b51bbaca)
![image](https://github.com/user-attachments/assets/92a3433d-d43b-4fc4-8761-e9cba993b408)


### 📤 PDF Export View  
![image](https://github.com/user-attachments/assets/efe66e2a-fd90-4aa3-b75f-9c856d840d65)

### extract questions from the given url
![image](https://github.com/user-attachments/assets/c38559c2-7c26-4eca-9356-60244681cb1e)

---

## 🛠️ Tech Stack

**Frontend:**
- React.js
- Material UI
- Tailwind CSS

**Backend:**
- Django
- Django REST Framework
- BeautifulSoup (for scraping)
- SpaCy (for NLP/NER)
- PyMongo

**Database:**
- MongoDB

**Authentication:**
- JWT (JSON Web Tokens)

---

## 🔍 Project Architecture

```plaintext
User Input (URL + Settings)
        ↓
Content Scraper (BeautifulSoup)
        ↓
NLP Processing (SpaCy NER)
        ↓
Question Generator (Logic + AI)
        ↓
MCQ Output (with Feedback & Hint)
        ↓
Frontend UI + PDF Export
🧪 Testing Overview
✅ Testing Strategy
Input Validation for various types of URLs and content

Relevance and grammar of generated MCQs

End-to-end flow from login → generate → export

🔍 Types of Testing Conducted
Unit Testing: Modules for scraping, question generation, APIs

Integration Testing: Communication between Django & React

User Testing: UI/UX feedback and question quality testing

Performance Testing: Large content processing and export validation

📊 Results
✅ Accurate MCQs with relevant explanations and hints

🧠 Handles edge cases like sparse/noisy text

⚡ Fast performance with minimal delay

🧭 Future Enhancements
🧠 Domain-Specific Tuning (Science, History, Technology, etc.)

📊 Auto-Classified Difficulty Levels using AI

🎤 Voice and 🖼️ Image Input for question generation

📈 User Feedback System to improve question quality

🌍 Multi-language MCQ generation using multilingual NLP models

📂 Getting Started
⚙️ Prerequisites
Python 3.9+

Node.js 18+

MongoDB (Local or Atlas Cloud)

🚀 Backend Setup

cd backend
pip install -r requirements.txt
python manage.py runserver
💻 Frontend Setup

cd frontend
npm install
npm run dev
📎 GitHub Repository
🔗 Project Repo: GENAI_Project-Advanced-MCQ-Generator

🙌 Contributors
Ansh Agarwal – Full Stack Developer & Project Lead

Thanks to all early testers and reviewers!

📜 License
This project is licensed under the MIT License.

Let me know if you'd like this saved as a downloadable `.md` file or if you want help creating the screenshots to insert into the placeholders.







