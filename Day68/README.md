# Day 68 — Authentication with Flask

## 📝 Overview  
On Day 68, you add **user authentication** to your Flask applications. The goal is to let users **register**, **login**, **logout**, and protect routes so only authenticated users can access certain features. :contentReference[oaicite:1]{index=1}  

You will integrate registration and login logic with hashed passwords, session management, and route protection.

---

## 🎯 Goals & Deliverables  
- **User Registration**: allow new users to create an account (username/email + password)  
- **Password Hashing**: store passwords securely (never plaintext)  
- **Login / Logout**: let users log in (session / cookie) and log out  
- **Protected Routes**: restrict certain views/pages to authenticated users only  
- **Redirects & Feedback**: redirect unauthorized users (e.g. to login), show error messages  
- **User Context**: make current user information available in templates (e.g. `current_user`)  
- **Optional Enhancements**: “Remember me” functionality, password reset, email confirmation  

---

## 🛠 Tools & Libraries  
- **Flask**  
- **Werkzeug** (for password hashing: `generate_password_hash`, `check_password_hash`)  
- **Flask-Login** (or manual session management)  
- **Flask-WTF** (for form handling & validation)  
- **Flask URL routing / blueprints**  
- **Templates (Jinja2)** — login, register, logout pages  
- **Database / ORM (SQLAlchemy or similar)** to store user records  

---

## ✅ Tips & Best Practices  
1. **Never store passwords in plaintext** — always hash + salt (e.g. `generate_password_hash`).  
2. Validate registration data (e.g. duplicate username/email, password strength).  
3. On login, compare hashed password via `check_password_hash`.  
4. Use `login_required` decorator (if using Flask-Login) or manual checks.  
5. Keep the **session** minimal — store user ID or token, not whole user object.  
6. Use `@before_request` or context processors to provide `current_user` to templates.  
7. Provide **flash messages** (e.g. “Invalid credentials”, “Registration successful”) to guide user.  
8. Redirect users after login/logout to appropriate pages.  
9. Ensure logout clears session or token properly.  
10. (Optional) Protect against brute force — e.g. rate limiting or login attempt caps.

---

## 🧩 How It Fits in the Course Flow  
- Day 68 builds on previous backend and REST days (Days 66, 67) by adding **security & user identity** to your web applications. :contentReference[oaicite:2]{index=2}  
- It prepares you for **user-based features** on future days (e.g. Day 69 — adding users to blog, Day 70 — deployment). :contentReference[oaicite:3]{index=3}  

---

