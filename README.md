# 🍽️ Food Ordering POS Backend

A production-ready **REST API backend** for a Food Ordering Point-of-Sale (POS) system built with **FastAPI** and **SQLAlchemy**. Supports full item and variant management with a built-in **audit logging system** that tracks every field-level change made to the data.

---

## 🚀 Live Demo

> 🔗 **[Live API on Render →](https://your-app-name.onrender.com/docs)**
> *(Replace this link after deploying to Render.com)*

After running locally, visit: **http://localhost:8000/docs**
FastAPI provides interactive Swagger UI — test all endpoints directly in the browser.

---

## ✨ Features

- 📦 **Item Management** — Create and update menu items with name, brand, category, product code, and branch
- 🔀 **Variant Management** — Each item supports multiple variants (e.g., sizes, flavors) with individual pricing and stock
- 📋 **Audit Logging** — Every field change is automatically recorded with the old value, new value, who made the change, and a timestamp
- ⚡ **FastAPI** — High-performance async API with automatic validation and interactive docs
- 🗃️ **SQLAlchemy ORM** — Clean database layer with relationship handling between items and variants
- 🔗 **RESTful Design** — Standard HTTP methods (GET, POST, PUT) with proper status codes and error handling

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## 📁 Project Structure

```
food-ordering-pos-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app, route definitions
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── crud.py          # Database operations (Create, Read, Update)
│   ├── audit.py         # Audit log helper — tracks field-level changes
│   └── database.py      # Database engine and session setup
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Data Models

### Item
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | String | Item name |
| brand | String | Brand name |
| category | String | Category (e.g., Beverages, Snacks) |
| product_code | String | Unique product identifier |
| branch_id | Integer | Branch the item belongs to |

### Variant
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| item_id | Integer | Foreign key → Item |
| variant_name | String | Variant label (e.g., Large, Spicy) |
| selling_price | Float | Customer-facing price |
| cost_price | Float | Internal cost price |
| quantity | Integer | Stock quantity |
| properties | JSON | Flexible key-value attributes |

### AuditLog
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| user | String | Who made the change |
| entity_type | String | "Item" or "Variant" |
| entity_id | Integer | ID of the changed record |
| field_name | String | Which field was changed |
| old_value | String | Value before the change |
| new_value | String | Value after the change |
| timestamp | DateTime | When the change occurred |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check — confirms server is running |
| POST | `/items` | Create a new menu item |
| PUT | `/items/{item_id}` | Update fields of an existing item |
| POST | `/variants` | Create a new variant for an item |
| PUT | `/variants/{variant_id}` | Update fields of an existing variant |
| GET | `/audit-logs` | Retrieve all audit logs (latest first) |

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/VishnuMohanp-10/food-ordering-pos-backend.git
cd food-ordering-pos-backend
```

### 2. Create a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

### 5. Open API docs in browser

```
http://localhost:8000/docs
```

---

## 🧪 Example API Usage

### Create an Item
```http
POST /items
Content-Type: application/json

{
  "name": "Classic Burger",
  "brand": "BurgerHub",
  "category": "Main Course",
  "product_code": "BH-001",
  "branch_id": 1
}
```

### Create a Variant
```http
POST /variants
Content-Type: application/json

{
  "item_id": 1,
  "variant_name": "Large",
  "selling_price": 299.00,
  "cost_price": 150.00,
  "quantity": 50,
  "properties": {"size": "large", "spice_level": "medium"}
}
```

### Update an Item (triggers audit log)
```http
PUT /items/1
Content-Type: application/json

{
  "name": "Classic Burger - Special Edition"
}
```

### View Audit Logs
```http
GET /audit-logs
```

**Sample response:**
```json
[
  {
    "id": 1,
    "user": "admin",
    "entity_type": "Item",
    "entity_id": 1,
    "field_name": "name",
    "old_value": "Classic Burger",
    "new_value": "Classic Burger - Special Edition",
    "timestamp": "2025-01-15T10:30:00"
  }
]
```

---

## 🔍 How Audit Logging Works

Every time an item or variant is **updated**, the system:
1. Compares the old field value with the new value
2. If they differ, records a new `AuditLog` entry with full before/after details
3. Stores who made the change, what entity was changed, and when

This gives a complete **change history** for every item and variant in the system — useful for tracking price changes, stock adjustments, or any data corrections.

---

## 📌 Requirements

```
fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
```

---

## 👨‍💻 Author

**Vishnu Mohan P**  
Python & FastAPI Backend Developer  
[GitHub](https://github.com/VishnuMohanp-10) · [LinkedIn](https://linkedin.com/in/vishnu-mohan-p/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
