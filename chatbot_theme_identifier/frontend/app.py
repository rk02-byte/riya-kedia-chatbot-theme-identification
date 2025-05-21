import streamlit as st
import requests

API_URL = "https://riya-document-research-theme-7iie.onrender.com"

st.set_page_config(page_title="Document Theme Chatbot", layout="centered")

st.title("Document Theme Identifier Chatbot")

st.markdown("Upload documents and ask questions. Get cited answers and themes.")

# File uploader
st.subheader("Step 1: Upload Documents")
uploaded_file = st.file_uploader("Upload PDF or Image", type=["pdf", "png", "jpg", "jpeg"])
if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    with st.spinner("Uploading and processing..."):
        res = requests.post(f"{API_URL}/upload/", files=files)
    if res.status_code == 200:
        st.success(f"Uploaded: {uploaded_file.name}")
        st.json(res.json())
    else:
        st.error("Upload failed.")

# Question
st.subheader("Step 2: Ask a Research Question")
query = st.text_input("Enter your query (e.g., What penalties were mentioned?)")
if query:
    with st.spinner("Searching documents..."):
        res = requests.get(f"{API_URL}/search/", params={"query": query})
    if res.status_code == 200:
        search_data = res.json()
        st.success("Top matching chunks:")
        chunks = []
        for item in search_data["results"]:
            st.markdown(f"**Doc ID:** `{item['doc_id']}` — Chunk `{item['chunk_index']}`")
            st.write(item["chunk_text"])
            chunks.append(item["chunk_text"])

        # Optional: Show theme synthesis
        if st.button("Generate Themes from Results"):
            with st.spinner("Identifying themes..."):
                theme_res = requests.post(f"{API_URL}/theme/", json=chunks)
            if theme_res.status_code == 200:
                st.subheader("Themes Identified:")
                theme_data = theme_res.json().get("themes", {})
                for key, theme in theme_data.items():
                    st.markdown(f"### {theme['title']}")
                    st.write(theme["summary"])
                    st.markdown("**Chunk Excerpts:**")
                    for c in theme["chunks"]:
                        st.code(c)
            else:
                st.error("Theme extraction failed.")
    else:
        st.error("Search failed.")
