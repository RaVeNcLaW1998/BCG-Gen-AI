# 💬 Financial Data Chatbot

A simple financial chatbot web application built using **Streamlit** that answers predefined questions based on a CSV dataset containing financial information for Microsoft, Tesla, and Apple from 2022 to 2025.

---

## 📁 Project Structure

```
├── chatbot.py            # Core chatbot logic and dataset queries
├── streamlit_app.py      # Streamlit UI that connects to chatbot.py
├── data.csv              # Financial dataset used by the chatbot
├── README.md             # Project documentation (this file)
```

---

## 🧠 Features

- Answer predefined queries about:
  - Total revenue across years
  - Net income changes year-over-year
  - Average net income per company
  - Highest revenue year for each company
  - Debt ratio calculation (Liabilities / Assets)
  - Operating cash flow trend for Apple
  - Specific company-year financials

- Clean and styled chat interface using custom HTML/CSS in Streamlit
- Session state memory for chat history
- Form-based input that clears after submission

---

## 🚀 How to Run

### 1. Install Requirements

```bash
pip install streamlit pandas
```

### 2. Prepare the Dataset

Create a file named `data.csv` in the root folder with this format:

```
Company,Year,Total Revenue,Net Income,Total Assets,Total Liabilities,Cash Flow from Operating Activities
Microsoft,2024,245122.00,88136.00,512163.00,243686.00,118548.00
Tesla,2025,97690.00,7153.00,122070.00,48390.00,14923.00
Apple,2024,391035.00,98016.00,364980.00,308030.00,118254.00
...
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

---

## 📌 Example Queries You Can Ask

- `What is the total revenue?`
- `How has net income changed over the last year?`
- `What is the average net income per company?`
- `What year had the highest revenue for each company?`
- `What is the debt ratio for each company in the latest year?`
- `What is the trend in operating cash flow for Apple?`
- `Show me financials for Tesla 2024`

---

## 🛠️ Customization Tips

- Add natural language processing for free-form questions
- Connect a live financial API (e.g., Yahoo Finance)
- Extend chatbot memory with vector storage or a database

---

## 📄 License

MIT License — free to use and modify.
