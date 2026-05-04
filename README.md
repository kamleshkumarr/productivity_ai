# 🚀 TaskPilot – Smart Ai Task Manager

A full-stack **AI-powered TaskPilot web app** that helps users manage tasks, track progress, and improve efficiency using intelligent insights.

🔗 **Live Demo:** https://productivity-ai-ij7f.onrender.com/

---

## 📌 Overview

TaskPilot  is a smart task management system that combines traditional features like task tracking and deadlines with **AI-based priority detection and motivation systems**.

---

## ✨ Features

### 🔐 Authentication
- User Signup & Login
- Secure authentication system

### 📋 Task Management
- Create, edit, and delete tasks
- Add descriptions and deadlines
- Mark tasks as completed

### 🧠 AI Features
- Automatic task priority detection (High / Medium / Low)
- Smart productivity suggestions
- Motivation system based on streaks 🔥

### 📊 Dashboard
- View all tasks in one place
- Separate:
  - ✅ Completed tasks  
  - ⏳ Pending tasks  
- Track productivity streak

### ⏰ Insights
- Overdue task tracking
- Daily productivity feedback

---

## 🛠️ Tech Stack

### Backend
- Python (Django)

### Frontend
- HTML, CSS, JavaScript (Django Templates)

### Database
-  PostgreSQL

### AI Integration
- Hugging Face API (Zero-shot classification model)

### Deployment
- Render (Cloud Hosting)

---

## ⚙️ Installation (Local Setup)

```bash
# Clone repository
git clone https://github.com/kamleshkumarr/productivity-ai.git

# Navigate into project
cd productivity-ai

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
