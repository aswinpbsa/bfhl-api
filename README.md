# BFHL API

A simple **Flask API** project built for assignment/demo purposes.  

## 🚀 Features
- Accepts input data (numbers, alphabets, special characters).
- Separates data into:
  - ✅ Alphabets (with capitalization check)
  - ✅ Numbers (even/odd separation)
  - ✅ Special characters
- Performs additional operations:
  - ✅ Concatenation of alphabets
  - ✅ Sum of numbers
- Returns JSON response with structured output.

---

## 📂 Project Structure
```
bfhl-api/
│── app.py              # Main Flask app
│── requirements.txt    # Dependencies
│── Procfile (optional) # For deployment on Heroku (if needed)
│── .gitignore          # Ignores venv, cache files
│── venv/               # Virtual environment (not pushed to GitHub)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/aswinpbsa/bfhl-api.git
cd bfhl-api
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/Scripts/activate   # On Windows (Git Bash/PowerShell)
# OR
source venv/bin/activate       # On Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
python app.py
```
The API will be running at:  
👉 `http://127.0.0.1:5000`

---

## 📡 API Usage

### POST `/bfhl`
**Request:**
```json
{
  "data": ["a","1","334","4","R","$"]
}
```

**Response:**
```json
{
  "alphabets": ["A", "R"],
  "concat_string": "Ra",
  "email": "john@xyz.com",
  "even_numbers": ["334", "4"],
  "is_success": true,
  "odd_numbers": ["1"],
  "roll_number": "ABCD123",
  "special_characters": ["$"],
  "sum": "339",
  "user_id": "john_doe_17091999"
}
```

---

## 🛠️ Requirements
- Python 3.8+
- Flask

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author
**Aswin PBSA**  
📌 [GitHub](https://github.com/aswinpbsa)
