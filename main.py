import streamlit as st
import tempfile
import os
from sow_backend import process_file_and_generate_sow

st.set_page_config(page_title="SoW Generator", layout="wide")

st.title("📄 Statement of Work (SoW) Generator")
st.markdown(
    "Upload your project proposal (PDF, PPTX, DOCX, or TXT), and get a professionally generated SoW."
)

# File upload section
uploaded_file = st.file_uploader(
    "Upload a proposal document", type=["pdf", "pptx", "docx", "txt"]
)

if uploaded_file is not None:
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_file_path = tmp_file.name

    st.success("✅ File uploaded successfully!")

    if st.button("🚀 Generate SoW"):
        with st.spinner("Generating Statement of Work... ⏳"):
            try:
                sow_text, download_url = process_file_and_generate_sow(temp_file_path)
                st.subheader("📜 Generated Statement of Work")
                st.text_area("Statement of Work", value=sow_text, height=500)
                st.markdown(f"[⬇️ Download SoW]({download_url})", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    # Clean up
    os.unlink(temp_file_path)
