# Day 67 — Blog Capstone Part 3: RESTful Routing

## 📝 Overview  
On Day 67, you continue building your **Blog Capstone project**, focusing on **RESTful API routing** and enabling **editing functionality**. :contentReference[oaicite:1]{index=1}  
You integrate backend features so users can create, read, update, and delete blog posts via standard HTTP methods and templates. :contentReference[oaicite:2]{index=2}  

---

## 🎯 Goals & Deliverables  
- Expand the blog application with **edit and delete** capabilities for blog posts  
- Set up **RESTful routes** (GET, POST, PATCH/PUT, DELETE) to handle full CRUD operations  
- Use **SQLAlchemy** for database operations  
- Use **WTForms** for form validation and submission for editing/creating posts  
- Handle **timestamps / date fields** (e.g. `datetime`) to record post creation and modification  
- Use **Jinja templating** to render forms and updated content in templates  
- Add error handling (invalid post IDs, missing data, etc.)  
- Document newly added routes and functionality

---

## 🛠 Tools & Technologies  
- **Flask** (or Flask + extensions)  
- **Flask-WTForms** (or equivalent form library)  
- **SQLAlchemy** for ORM / database interactions  
- **Python’s datetime module** for timestamping  
- **Jinja2** templates (HTML)  
- A static CSS framework (e.g. Bootstrap) to style forms & pages  
- Tests or manual API/route validation via browser / tools (Postman)

---

## ✅ Tips & Best Practices  
1. Define routes clearly (e.g. `/post/<int:post_id>/edit`, `/post/<int:post_id>/delete`).  
2. Use **HTTP method checks** (e.g. `if request.method == "POST": ...`) to separate form display vs form submission.  
3. Pre-populate the edit form with existing post data.  
4. Validate input data before committing to the database.  
5. Use `datetime.now()` (or timezone-aware variant) to update a `last_modified` field.  
6. Redirect after a successful operation (POST-redirect-GET pattern).  
7. Return appropriate messages or error pages when operations fail (404, 400).  
8. Keep REST principles in mind: the route should reflect the resource and operation.

---

## 🧩 How It Fits in the Course Flow  
- This day deepens the **backend / full-stack** abilities by combining what you learned on Day 66 (REST API principles) with templating and data persistence. :contentReference[oaicite:3]{index=3}  
- It sets up for **authentication, user accounts, and security features** in subsequent days (e.g. Day 68). :contentReference[oaicite:4]{index=4}  

---