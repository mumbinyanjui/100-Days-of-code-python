# 🏗️ Day 71 – Building Advanced User Features: Comments & Likes System

**Goal:**  
Enhance the functionality of your Flask-based web app by adding user interactions such as **comments**, **likes**, and **post engagement tracking**. This continues from Day 70’s deployed project, focusing on improving user experience and backend logic.

---

## 🚀 What You’ll Build
Today, you’ll implement a **comment and like system** that allows registered users to:
1. Comment on posts or items in your app.
2. Like or unlike content dynamically.
3. See the number of likes and comments per post.
4. Ensure only authenticated users can interact.

---

## 🧠 Concepts Covered
- **Flask-WTF Forms** for handling comment input.  
- **Flask-Login** authentication integration with new routes.  
- **SQLAlchemy relationships** (one-to-many and many-to-many).  
- **Jinja2 templating** for rendering dynamic UI updates.  
- Handling **POST and GET** requests in Flask routes.

---

## 🛠️ Steps
1. **Set up your database models**  
   - Add `Comment` and `Like` tables.
   - Create relationships between `User`, `Post`, and `Comment`.

2. **Update Flask routes**  
   - Add `/comment/<post_id>` and `/like/<post_id>` endpoints.
   - Handle comment form submissions and like toggles.

3. **Modify templates**  
   - Display existing comments below posts.
   - Add buttons for “Like ❤️” and “Unlike 💔”.

4. **Add authentication checks**  
   - Only logged-in users can comment or like.
   - Redirect unauthenticated users to the login page.

5. **Test locally and redeploy**  
   - Use your CI/CD pipeline or manual redeployment from Day 70.
   - Test across devices.

---

## 🧩 Example Code Snippet
```python
@app.route("/comment/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    new_comment = Comment(
        text=request.form.get("comment"),
        author=current_user,
        post_id=post_id
    )
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for("show_post", post_id=post_id))
