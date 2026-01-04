# 🔁 LRU Cache Simulator (Python + Streamlit)

An interactive web application that demonstrates the working of a **Least Recently Used (LRU) Cache** using Python.  
This project visually shows how cache entries are added, accessed, and evicted based on the LRU policy.

---

## 🚀 Live Demo
👉 https://YOUR-APP-NAME.streamlit.app  
*(Replace with your actual Streamlit Cloud URL after deployment)*

---

## 🧠 What is LRU Cache?
**LRU (Least Recently Used) Cache** removes the item that has not been used for the longest time when the cache reaches its capacity.

LRU Cache is widely used in:
- Operating Systems
- Web Browsers
- Databases
- Backend Caching Systems

---

## 🛠 Tech Stack
- **Python**
- **Streamlit** (for interactive web UI)
- **Data Structures**
  - Dictionary (Hash Map)
  - List (to maintain usage order)

---

## ✨ Features
- Set cache capacity dynamically
- PUT operation to insert key-value pairs
- GET operation to retrieve values
- Automatic eviction of least recently used items
- Live visualization of cache state

---

## 🧩 Data Structures Used
| Data Structure | Purpose |
|---------------|---------|
| Dictionary    | O(1) access to cache items |
| List          | Track usage order (LRU → MRU) |

---

## ⚙️ How It Works
1. User sets cache capacity
2. PUT operation inserts or updates data
3. GET operation retrieves data and updates usage order
4. When capacity is exceeded, the **least recently used** item is removed

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install streamlit
