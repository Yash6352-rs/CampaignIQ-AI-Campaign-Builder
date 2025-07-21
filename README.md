# 📣 CampaignIQ – Multi-Agent Marketing Campaign Generator

**CampaignIQ** is a Flask-based web application that uses multiple intelligent agents powered by Gemini 1.5 Flash and LangChain to generate personalized, multi-channel marketing campaigns for any product.

Ideal for marketers, entrepreneurs, and students, it combines LLMs and user input to produce high-quality, downloadable marketing strategy documents within seconds.

---

## ✨ Features

- Input any product and select your preferred marketing channels
- AI generates:
  - Product analysis
  - Customer segments
  - Target personas
  - Marketing content (social/email/blog)
  - Channel-specific campaign strategy
- Download campaign report as a .txt file
- Responsive UI with spinner loader and dark-themed layout
- Built using multi-agent LLM chains with LangChain
- API Key securely managed using .env

---

## 📸 Screenshots

**1. Input Form UI**
Users can enter a product and choose channels like Instagram, YouTube, Email, Blog, etc.

<img width="1100" height="1042" alt="image" src="https://github.com/user-attachments/assets/8e804190-58c8-4f52-8055-e6d266108297" />


**2. Result Page**
CampaignIQ generates and displays structured campaign content across sections.

<img width="1144" height="1040" alt="image" src="https://github.com/user-attachments/assets/bfae5143-c94b-442c-b38c-6a9aced09a02" />


**3. Download Option**
Download your generated campaign plan instantly as a .txt file.

<img width="1144" height="1040" alt="image" src="https://github.com/user-attachments/assets/9e578861-c13c-4801-897c-6c239e646866" />


---

## 🗂️ Project Structure

campaigniq/
- app.py ( Flask app setup and routes )
- agents_logic.py ( Multi-agent chain logic using LangChain & Gemini )
- templates\
  - index.html ( Form page )
  - result.html ( Output/result page )
- static\
  - indexstyle.css ( Styling for index )
  - resultstyle.css  ( Styling for result )  
- .env (API key )
- .gitignore ( Files/folders to ignore in Git )
- README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

- git clone https://github.com/your-username/campaigniq.git
- cd campaigniq

### 2. Create Virtual Environment (optional but recommended)

This or use anaconda prompt
- python -m venv venv
- source venv/bin/activate

Or use Anaconda:
- conda create -n campaign python=3.10 -y
- conda activate campaign

### 3. Install Requirements

pip install flask python-dotenv langchain langchain-google-genai

### 4. Setup Gemini API Key

Create a .env file in the root directory:
- GEMINI_API_KEY=your_google_gemini_api_key

### 5. Running the App

streamlit run app.py

Then open your browser at:
- http://127.0.0.1:5000

---

## 🧠 How It Works

- Input a product name and select marketing channels.
- Five LangChain-based agents (analyzer, segmenter, persona builder, content writer, strategist) generate campaign content.
- The result is displayed in sections and can be downloaded as .txt.

---

## 📌 Tech Stack

- Flask – Backend framework for web interface
- LangChain – Multi-agent architecture and chain handling
- Gemini 1.5 Flash – LLM for generating content
- HTML/CSS/JS – Frontend
- Python-dotenv – Secure API key storage


---

**🚀 “Plan smarter, launch faster – with AI-powered campaigns.”**
