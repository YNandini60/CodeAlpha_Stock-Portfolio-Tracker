# CodeAlpha_Stock-Portfolio-Tracker
This Stock Portfolio Tracker is built for CodeAlpha Internship Task 2. It lets users enter stock symbols and quantities, calculates the total investment using predefined stock prices, and shows a portfolio summary. Results can optionally be saved to a .txt or .csv file.

##  Project Description 

This Stock Portfolio Tracker is built for **CodeAlpha Internship Task 2**. It lets users enter stock symbols and quantities, calculates the total investment using predefined stock prices, and shows a portfolio summary. Results can optionally be saved to a `.txt` or `.csv` file.

It’s a beginner-friendly project that demonstrates key programming concepts like **dictionaries, input/output handling, arithmetic operations, and file handling** in Python. 

# 📊 Stock Portfolio Tracker
**CodeAlpha Internship – Task 2**

##  Overview
This project is a **Stock Portfolio Tracker** developed as part of the **CodeAlpha Internship (Task 2)**.  
The program allows users to input stock symbols and quantities, calculates the total investment value based on predefined stock prices, and generates a portfolio summary. Users can also save results into a `.txt` or `.csv` file.

##  Objective
The goal of this task is to create a **simplified stock tracker** where:
- Users manually input the stocks they own.
- The program uses a **hardcoded dictionary** of stock prices.
- A detailed summary of the portfolio is displayed.
- Users optionally save the results in `.txt` or `.csv` format.
- 
##  Features
- Predefined stock prices (hardcoded dictionary).
- User inputs stock symbol and quantity.
- Validation for incorrect symbols and invalid quantities.
- Displays portfolio with per-stock value and **total investment**.
- Option to save results as:
  - `portfolio.txt`
  - `portfolio.csv`

##  Technologies Used
- **Python 3**
- **Dictionary** (for stock prices)
- **Input/Output handling**
- **Basic arithmetic operations**
- **File handling** (`.txt` and `.csv` writing)

##  How to Run
1. Install Python (version 3.6+ recommended).
2. Save the script as `portfolio_tracker.py`.
3. Run the program in terminal:
   ```bash
   python portfolio_tracker.py
   ```

## 📖 Example Run

```
 Stock Portfolio Tracker
Available stocks: AAPL, TSLA, MSFT, GOOGL, AMZN

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 3

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 2

Enter stock symbol (or 'done' to finish): done

 Portfolio Summary:
AAPL - 3 shares @ $180 = $540
TSLA - 2 shares @ $250 = $500

 Total Investment Value: $1040

Do you want to save results? (txt/csv/no): csv
 Results saved in portfolio.csv
```

##  Learning Outcomes

* Use of **dictionaries** for storing stock data.
* Handling **user input and validation**.
* Performing **arithmetic calculations**.
* Saving output into different **file formats**.
* Strengthened understanding of **Python basics**.

---

 **Author**: \[Srinidhi]
 **Internship**: CodeAlpha Internship
 **Task**: Task 2 – Stock Portfolio Tracker
