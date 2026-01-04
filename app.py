import streamlit as st

# ---------------- LRU CACHE IMPLEMENTATION ---------------- #

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            lru = self.order.pop(0)
            del self.cache[lru]
        self.cache[key] = value
        self.order.append(key)


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="LRU Cache Simulator", layout="centered")

st.title("🔁 LRU Cache Simulator")
st.write("Interactive demonstration of Least Recently Used (LRU) Cache")

capacity = st.number_input(
    "Enter Cache Capacity",
    min_value=1,
    step=1,
    value=2
)

# Initialize cache only once
if "cache" not in st.session_state or st.session_state.capacity != capacity:
    st.session_state.cache = LRUCache(capacity)
    st.session_state.capacity = capacity

key = st.text_input("Enter Key")
value = st.text_input("Enter Value")

col1, col2 = st.columns(2)

with col1:
    if st.button("PUT"):
        if key == "" or value == "":
            st.warning("Please enter both key and value")
        else:
            st.session_state.cache.put(key, value)
            st.success(f"Inserted ({key}, {value}) into cache")

with col2:
    if st.button("GET"):
        if key == "":
            st.warning("Please enter a key")
        else:
            result = st.session_state.cache.get(key)
            if result == -1:
                st.error("Key not found in cache")
            else:
                st.info(f"Value for key '{key}' is: {result}")

st.divider()
st.subheader("📦 Current Cache State (Least → Most Recent)")
st.write(st.session_state.cache.order)
st.subheader("🔍 Cache Key-Value Pairs")
st.write(st.session_state.cache.cache)
