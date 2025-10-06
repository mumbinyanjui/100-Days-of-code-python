# Day 69 — Blog Capstone Project Part 4: Adding Users

## 📝 Overview  
On Day 69, you extend your blog application by integrating **user accounts**. You’ll allow multiple users to register, log in, and create blog posts under their own identities. You’ll also manage **user-to-post relationships**, enforce **ownership constraints**, and enhance your application’s structure and security. :contentReference[oaicite:1]{index=1}

---

## 🎯 Goals & Deliverables  
- Implement **user registration** with unique credentials (e.g. email/username + password).  
- Allow **login / logout** for users (if not already done in Day 68).  
- Associate blog **posts with users** (author relationship) in the database.  
- Ensure that **only the author** of a post can **edit** or **delete** it.  
- Update templates (front end) to:
  - Display the author’s name on posts  
  - Show or hide “Edit” / “Delete” buttons based on user’s identity  
- Add **protection** so that unauthorized users can’t access restricted routes (e.g. editing posts not theirs).  
- Update your **README or documentation** to reflect the new routes and features.

---

## 🛠 Tools & Technologies  
- **Flask**  
- **Flask-Login** (or your chosen session/auth framework)  
- **Werkzeug** password hashing (`generate_password_hash`, `check_password_hash`)  
- **SQLAlchemy** ORM to model `User` and `Post` tables and their relationship  
- **Flask-WTF / WTForms** for registration and login forms  
- **Jinja2 templates** (conditional rendering based on `current_user`)  
- **Blueprints** or modular structure (optional but useful)  

---

## ✅ Tips & Best Practices  
1. Define a `User` model with fields like `id`, `username`/`email`, `password_hash`, and a relationship to `Post`.  
2. In the `Post` model, include a foreign key field `author_id` pointing to the `User` model.  
3. Use `@login_required` (or similar) to guard routes like creating, editing, or deleting posts.  
4. Before editing/deleting, check that `current_user.id == post.author_id`; otherwise abort or redirect.  
5. Use Flask-Login’s `current_user` in templates to conditionally show UI elements (e.g. show “Edit” only if user is author).  
6. Use `flash` messages to inform users (“You do not have permission to edit this post”, etc.).  
7. After operations (create/edit/delete), redirect to avoid re-submission (POST-redirect-GET pattern).  
8. Sanitize and validate all user input (even from forms) — don’t trust front-end only checks.  
9. Keep UI intuitive — e.g. show “My Posts” or dashboard listing only the logged-in user’s posts.

---

## 🧩 How It Fits in the Course Flow  
- Day 69 builds directly upon Day 68’s authentication setup by connecting user identity to content. :contentReference[oaicite:2]{index=2}  
- It sets the stage to deploy a multi-user blog (e.g. on Heroku) on the next day (Day 70). :contentReference[oaicite:3]{index=3}  

---

## 📌 Sample Route Table (with Users)

| HTTP Method | Path                            | Purpose                                         |
|-------------|----------------------------------|-------------------------------------------------|
| GET         | `/register`                       | Show user registration form                     |
| POST        | `/register`                       | Handle registration submission                  |
| GET         | `/login`                          | Show login form                                  |
| POST        | `/login`                          | Authenticate and login user                      |
| GET / POST  | `/logout`                         | Log out the user                                 |
| GET         | `/posts/new`                       | Show form to create a blog post                  |
| POST        | `/posts/new`                       | Create new blog post associated with user        |
| GET         | `/posts/<int:id>/edit`            | Show form to edit post (if current user is author) |
| POST / PATCH| `/posts/<int:id>/edit`            | Submit updates to the post                       |
| POST / DELETE| `/posts/<int:id>/delete`         | Delete the post (only if current user is author) |
| GET         | `/posts`                           | List all posts (with authors shown)              |
| GET         | `/posts/<int:id>`                  | View individual post (show post and author)      |

---


