# Day 53: Automated Rental Listings Form Filler 🏘️✍️

Today’s project was all about automation and scraping! I built a bot that scrapes rental listing data (price, address, link) from a sample Zillow-style site and automatically fills out a Google Form for each listing.

## 🔧 Technologies Used:
- `BeautifulSoup` for scraping listing data (addresses, prices, links)
- `Selenium` for browser automation to fill out a Google Form
- `requests` for sending GET requests with custom headers
- `XPath` selectors to interact with Google Form fields

## 💡 How it works:
1. Scrapes the sample Zillow-Clone site: [https://appbrewery.github.io/Zillow-Clone/](https://appbrewery.github.io/Zillow-Clone/)
2. Collects:
   - Listing links
   - Rental prices
   - Property addresses
3. Uses Selenium to auto-fill and submit a Google Form for each listing.

## 📌 Key Learning:
- Using `select()` with CSS selectors in BeautifulSoup
- Cleaning scraped data (removing `\n`, `/mo`, `+`)
- Filling forms dynamically using `find_element(By.XPATH, ...)` in Selenium

## 🧪 Next Steps:
- Add a headless browser for background automation
- Store listings in a Google Sheet or database
- Extend this to real Zillow (with legal caution)

## 🚀 Project Outcome:
Automated rental data entry from a webpage to a form – a practical skill for scraping + automation!

---

### Run Instructions

1. Create your own Google Form with 3 short answer fields: **Address**, **Price**, **Link**
2. Replace `"YOUR_GOOGLE_FORM_LINK_HERE"` with your actual Google Form URL in the script
3. Run the script to see browser automation in action
