# Webform Flask App

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Codereverse12/webform.git
cd webform
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Database Setup & Migrations

This project uses **Flask-Migrate** to handle database migrations.

> 💡 You do **not** need to run `flask db init` — the `migrations/` folder is already included in this repository.

### Apply migrations to the database
```bash
flask db upgrade
```

---

## ▶️ Running the App

Run the Flask development server:

```bash
flask run
```

The app will be available at:
```
http://127.0.0.1:5000
```