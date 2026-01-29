# 🕸️ NEXUS | Real-Time Market Intelligence Dashboard

### 🚀 Overview
**NEXUS** is a competitive intelligence tool designed to automate price tracking and market analysis. It simulates a real-time scraping engine that monitors competitor pricing across multiple e-commerce platforms (Amazon, eBay, BestBuy) to identify undercutting risks and margin opportunities.

This project demonstrates the ability to transform raw data into actionable business insights using **Python** and **Interactive Visualization**.

---

### 📸 Dashboard Preview
<img width="1366" height="768" alt="Screenshot (254)" src="https://github.com/user-attachments/assets/10065c7b-f77b-4890-9f48-259fd7a8bb43" />



---

### ⚡ Key Features
* **Real-Time Monitoring:** Simulates live data feeds with a sidebar log showing proxy rotation and scraping status.
* **Price Gap Analysis:** Interactive bar charts comparing "My Price" vs. "Competitor Price" to spot immediate threats.
* **Automated Alerts:** Logic-based status engine that flags products as `⚠️ CRITICAL` if a competitor undercuts price.
* **Demand Heatmap:** A scatter plot correlating Price vs. Demand Score to find the "Sweet Spot" for pricing strategies.
* **Data Export:** One-click CSV export for offline analysis in Excel.

### 🛠️ Tech Stack
* **Core Logic:** `Python 3.10+`
* **Data Processing:** `Pandas` (Data cleaning, difference calculation)
* **Visualization:** `Plotly Express` & `Graph Objects` (Interactive charts)
* **Frontend/UI:** `Streamlit` (Web framework)

---

### 💻 How to Run This Project
If you want to test the dashboard locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/nexus-market-monitor.git](https://github.com/YOUR-USERNAME/nexus-market-monitor.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    streamlit run price_monitor.py
    ```

---

### 👨‍💻 Author
**Lee-roy B.**

* [LinkedIn Profile](https://www.linkedin.com/in/lee-roy-chimuka)
* [Fiverr Profile](https://www.fiverr.com/leeroybreat)
