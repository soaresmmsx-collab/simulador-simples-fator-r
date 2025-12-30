import streamlit as st
import hashlib

# usuários (exemplo)
USERS = {
    "max": hashlib.sha256("1234".encode()).hexdigest(),
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.title("🔐 Login")

    user = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if user in USERS and USERS[user] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success("Login realizado com sucesso")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos")

def logout():
    if st.sidebar.button("🚪 Sair"):
        st.session_state.clear()
        st.experimental_rerun()
