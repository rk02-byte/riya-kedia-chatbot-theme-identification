import streamlit as st
import requests

API_URL = "https://riya-document-research-theme-7iie.onrender.com/api"

st.set_page_config(page_title="Document Theme Chatbot", layout="centered")

st.title("Document Theme Identifier Chatbot")

st.markdown("Upload PDFs or images and ask questions. Get cited answers and cross-document themes.")

#Upload File
st.subheader("Step 1: Upload Document (PDF or Image)")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file:
    # File size check: Streamlit Cloud is sensitive to large uploads
    if uploaded_file.size > 2 * 1024 * 1024:
        st.error("File too large. Please upload a file under 2MB.")
        st.stop()

    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    with st.spinner("Uploading and processing file..."):
        try:
            res = requests.post(f"{API_URL}/upload/", files=files, timeout=40)
            if res.status_code == 200:
                st.success(f"Uploaded: {uploaded_file.name}")
                upload_data = res.json()
                st.write("Text preview:")
                st.write(upload_data["text_preview"])
                st.write(f"Chunks stored: {upload_data['chunks_stored']}")
            else:
                st.error("Upload failed.")
                st.write("Status:", res.status_code)
                st.write("Response:", res.text)
        except requests.exceptions.RequestException as e:
            st.error("Upload failed due to network or timeout.")
            st.exception(e)

# Step 2: Ask a question
st.subheader("Step 2: Ask a Research Question")

query = st.text_input("Enter your question (e.g., What penalties are mentioned?)")

if query:
    with st.spinner("Searching relevant chunks..."):
        try:
            res = requests.get(f"{API_URL}/search/", params={"query": query}, timeout=30)
            if res.status_code == 200:
                search_data = res.json()
                st.success("Found related chunks:")
                chunks = []
                for result in search_data["results"]:
                    st.markdown(f"**Doc ID:** `{result['doc_id']}` — Chunk `{result['chunk_index']}`")
                    st.write(result["chunk_text"])
                    chunks.append(result["chunk_text"])
            else:
                st.error("Search failed.")
                st.write("Status:", res.status_code)
                st.write("Response:", res.text)
        except requests.exceptions.RequestException as e:
            st.error("Search request failed.")
            st.exception(e)

    # Step 3: Generate themes (optional)
    if st.button("🧠 Generate Themes"):
        if not chunks:
            st.warning("No chunks available to analyze.")
        else:
            with st.spinner("Identifying themes..."):
                try:
                    theme_res = requests.post(f"{API_URL}/theme/", json=chunks, timeout=60)
                    if theme_res.status_code == 200:
                        theme_data = theme_res.json().get("themes", {})
                        st.subheader("Identified Themes")
                        for key, theme in theme_data.items():
                            st.markdown(f"### {theme['title']}")
                            st.write(theme["summary"])
                            st.markdown("**Excerpts:**")
                            for excerpt in theme["chunks"]:
                                st.code(excerpt)
                    else:
                        st.error("Theme generation failed.")
                        st.write("Status:", theme_res.status_code)
                        st.write("Response:", theme_res.text)
                except requests.exceptions.RequestException as e:
                    st.error("Theme extraction failed.")
                    st.exception(e)
