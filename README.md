# 🍽️ The Digital Waiter

The Digital Waiter is a Django-based web application that simulates a restaurant ordering system. It demonstrates the Model-View-Template (MVT) architecture by allowing users to browse a menu, select items via a form, and generate a bill with calculated totals stored in a database.

## 🚀 Features

* **Dynamic Menu:** Fetches food items (Burgers, Pasta, etc.) from a generic database.
* **Order Processing:** Calculates total cost based on server-side logic (secure from HTML manipulation).
* **Database Integration:** Stores every order with a timestamp and total price in SQLite.
* **Admin Panel:** A GUI for the restaurant owner to add/edit menu items.
* **Responsive Design:** Styled with Bootstrap 5 for a card-based layout.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, Bootstrap 5
* **Database:** SQLite (Lightweight Relational DB)

## ⚙️ How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone <YOUR_REPO_URL_HERE>
    cd digital_waiter
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Database**
    Since the database file is excluded from Git for security, you must generate it:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create an Admin User**
    To access the backend interface:
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/` to order food.

## 🔐 Admin Access

To manage the menu items (add food, change prices), go to `http://127.0.0.1:8000/admin`.

* **Username:** `[admin]`
* **Password:** `[admin]`

---
*Created as a Django Portfolio Project.*
