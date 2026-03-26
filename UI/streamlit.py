import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("Взаимодействие с нейросетью 🤖")
st.write(f"Подключено к API: `{API_URL}`")
user_input = st.text_area("Введите текст для обработки:", "Привет! Как дела?")

if st.button("Отправить в нейросеть"):
    try:
        response = requests.post(
            f"{API_URL}/predict", 
            json={"text": user_input}
        )
        
        if response.status_code == 200:
            st.success("Ответ получен:")
            st.write(response.json())
        else:
            st.warning(f"API вернул ошибку: {response.status_code}")
            
    except requests.exceptions.RequestException:
        st.error("Ошибка подключения! Убедитесь, что сервер FastAPI запущен.")