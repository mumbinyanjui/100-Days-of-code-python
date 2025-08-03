\# 📣 Day 40 – Flight Club: Flight Deal Notification System ✈️📬



\## 🎯 Goal



Extend the Flight Deal Finder (Day 39) by:

\- Automatically \*\*notifying users\*\* via \*\*email\*\* when cheap flights are found.

\- Reading user data (name, email) from a second Google Sheet.

\- Sending \*\*personalized alerts\*\* using `smtplib`.



---



\## 🧰 Tech Stack



\- \*\*Language:\*\* Python 3

\- \*\*APIs Used:\*\*

&nbsp; - \[Tequila Kiwi API](https://tequila.kiwi.com/)

&nbsp; - \[Sheety API](https://sheety.co) – for both flight data and user records

\- \*\*Email Client:\*\* SMTP with Gmail or custom SMTP

\- \*\*Libraries:\*\* `smtplib`, `datetime`, `requests`, `os`



---



\## 🧠 What’s New in Part 2?



✅ Adds \*\*user management\*\* with names \& emails via Sheety  

✅ Sends \*\*HTML-formatted email notifications\*\* when deals are found  

✅ Checks flight price against the "lowestPrice" in the Google Sheet  

✅ Refactors logic into clear classes: `FlightSearch`, `DataManager`, `NotificationManager`



---









