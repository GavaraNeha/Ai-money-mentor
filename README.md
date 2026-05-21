# 💰 AI Money Mentor

> **A smart financial assistant for students — analyze income, track expenses, and get personalized savings advice in real time.**

🔗 **Live Demo:** [ai-money-mentor-9gbc.onrender.com](https://ai-money-mentor-9gbc.onrender.com/)  
📁 **Repository:** [GavaraNeha/Ai-money-mentor](https://github.com/GavaraNeha/Ai-money-mentor)

---

## 📌 Problem Statement

Most students have no structured way to track their spending or plan savings. Financial apps are either too complex or built for salaried adults — not for students managing pocket money, part-time income, or stipends.

**AI Money Mentor** bridges that gap by giving students a simple, intelligent dashboard to understand their money health, visualize spending, and receive actionable financial advice — all in one place.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏥 **Money Health Score** | AI-generated score rating your overall financial health |
| 🥧 **Expense Breakdown** | Interactive pie chart showing spending across categories |
| 💾 **Savings Calculator** | Computes how much you save based on income vs. expenses |
| 🎯 **Goal Tracking** | Set and monitor savings targets |
| 💡 **Personalized Advice** | Context-aware financial tips based on your spending patterns |
| 📊 **Interactive Dashboard** | Clean, real-time UI built for mobile and desktop |

---

## 🧠 How It Works

```
User inputs income + expense categories
              ↓
Flask backend processes and calculates savings & ratios
              ↓
AI logic generates a Money Health Score (0–100)
              ↓
Chart.js renders live expense breakdown pie chart
              ↓
Personalized financial advice surfaced based on patterns
              ↓
Dashboard displays full financial summary
```

**Advice engine considers:**
- Income-to-expense ratio
- Savings rate vs. recommended benchmarks (50/30/20 rule)
- High-spend category flags
- Goal feasibility based on current savings pace

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Frontend** | HTML, CSS, Jinja2 Templates |
| **Data Visualization** | Chart.js (interactive pie charts) |
| **Deployment** | Render (live cloud hosting) |
| **Process Management** | Procfile (Gunicorn) |
| **Version Control** | Git, GitHub |

---

## 🚀 Getting Started (Local Setup)

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/GavaraNeha/Ai-money-mentor.git
cd Ai-money-mentor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open your browser at `http://localhost:5000`

---

## 📂 Project Structure

```
Ai-money-mentor/
│
├── templates/
│   └── index.html          # Main dashboard UI (Jinja2 template)
│
├── static/                 # CSS, JS, assets
├── app.py                  # Flask app + financial logic
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment config (Gunicorn)
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

---

## 💡 Example Usage

**User Input:**
- Monthly Income: ₹15,000
- Rent: ₹4,000 | Food: ₹3,500 | Transport: ₹1,200 | Entertainment: ₹2,000 | Other: ₹1,500

**AI Money Mentor Output:**
- 💚 **Money Health Score: 72 / 100 — Good**
- 💾 **Monthly Savings: ₹2,800 (18.7%)**
- ⚠️ **Flag:** Entertainment spend is 13% of income — above the recommended 10%
- 💡 **Advice:** *"Reducing entertainment by ₹500/month could grow your savings by ₹6,000 annually. Consider setting a weekly cap."*

---

## 🔮 Future Enhancements

- [ ] User accounts with persistent savings history
- [ ] Monthly trend charts (bar/line graphs over time)
- [ ] CSV export of financial reports
- [ ] UPI/bank statement import for auto-categorization
- [ ] SMS/email alerts when overspending detected
- [ ] Multi-currency support for international students

---

## 👩‍💻 About the Developer

**Gavara Neha** — B.Tech in AI & Machine Learning, Aditya University  
Building AI tools that solve everyday problems for students and young professionals.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-GavaraNeha-black?style=flat&logo=github)](https://github.com/GavaraNeha)
[![LeetCode](https://img.shields.io/badge/LeetCode-100%2B%20Solved-orange?style=flat&logo=leetcode)](https://leetcode.com)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

> *Because every student deserves to understand where their money goes — and how to make it work harder.*
