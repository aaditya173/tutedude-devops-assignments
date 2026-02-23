# Task-2 of Assignment-3

## 📦 1. Create a Virtual Environment

Create a virtual environment named `venv`:

```bash
python -m venv venv
```

---

## 🔐 2. Activate the Virtual Environment

### On Linux / Mac:

```bash
source venv/bin/activate
```

### On Windows:

```bash
venv\Scripts\activate
```

After activation, your terminal should display:

```
(venv)
```

---

## 📥 3. Install Project Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install **Flask**, **pymongo**, **python-dotenv**, and other dependencies.

---

## ⚙️ 4. Setup Environment Variables (.env File)

This project uses environment variables for configuration.

### Step 1: Copy the example file

Rename the provided `.env.example` file to `.env`:

On Linux / Mac:

```bash
cp .env.example .env
```

On Windows:

```bash
copy .env.example .env
```

Or manually create a new file named:

```
.env
```

---

### Step 2: Update the values inside `.env`

Open the `.env` file and update the values:

```
MONGO_URI=your_mongodb_connection_string
DATABASE_NAME=your_database_name
COLLECTION_NAME=your_collection_name
```

⚠️ Important:

* Do not add spaces around `=`
* Do not use quotes
* Make sure `.env` is in the project root directory (same level as `app.py`)

---

## ▶️ 5. Run the Application

Start the Flask application:

```bash
python app.py
```

---

## 🌐 6. Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

You should now see the application running successfully 🎉

---
