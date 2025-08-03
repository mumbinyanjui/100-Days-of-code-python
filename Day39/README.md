\# ✈️ Day 39 – Flight Deal Finder (Capstone Project: Part 1)



\## 🚀 Goal

Create a backend system that searches for \*\*flight deals\*\* using the Kiwi Tequila API and stores them in a Google Sheet for later notification.



This is \*\*Part 1\*\* of the Flight Club capstone project. In Part 2 (Day 40), we'll notify users when the price drops below a threshold.



---



\## 🧰 Tech Stack

\- \*\*Language:\*\* Python 3

\- \*\*APIs Used:\*\*  

&nbsp; - \[Kiwi Tequila API (Skypicker)](https://tequila.kiwi.com/) – for flight data  

&nbsp; - \[Sheety API](https://sheety.co) – for storing search targets  

\- \*\*Libraries:\*\* `requests`, `datetime`, `os`



---



\## 🧠 How It Works



1\. A Google Sheet contains cities and their target flight prices (managed via Sheety).

2\. The script:

&nbsp;  - Converts city names into IATA codes (e.g., Nairobi → NBO)

&nbsp;  - Searches for flights from a source city (e.g., LON) to each destination

&nbsp;  - Compares found prices against the user-defined "lowestPrice"

&nbsp;  - Updates the sheet with missing IATA codes



---



\## 🗃️ Data Format



\*\*Google Sheet (Flight Deals):\*\*



| city    | iataCode | lowestPrice |

|---------|----------|-------------|

| Nairobi | NBO      | 450         |

| Paris   | PAR      | 300         |



---







