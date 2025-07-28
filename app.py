import streamlit as st
import docx
from pdfminer.high_level import extract_text
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Page Config ---
st.set_page_config(
    page_title="Resume-Job Description Matcher",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="🤝"
)

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
        color: #333;
    }
    .main {
        padding: 20px;
    }
    h1, h2, h3 {
        color: #264653;
    }
    .stButton>button {
        background-color: #2a9d8f;
        color: white;
        padding: 0.5em 1em;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #21867a;
        color: white;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #777;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("https://img.icons8.com/ios-filled/100/resume.png", width=80)
st.sidebar.title("About")
st.sidebar.info("""
This tool helps you analyze how well your resume matches a job description by using keyword-based similarity analysis.
            
**Upload your resume and the job description to get:**
- A skill match score
- Missing keywords
""")


# --- Helper Functions ---
def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file)

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    full_text = [para.text for para in doc.paragraphs]
    return '\n'.join(full_text)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def calculate_skill_match(resume_text, job_description_text):
    if not resume_text or not job_description_text:
        return 0.0, []
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100
    resume_words = set(resume_text.split())
    job_words = set(job_description_text.split())
    missing_skills = sorted(list(job_words - resume_words))
    return similarity, missing_skills

# --- Main App ---
st.title("Resume-Job Description Matcher")
st.markdown("Upload your resume and the job description to get a **skill match score** and see any **missing keywords** to improve your resume.")

st.subheader("📄 Upload Documents")

resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
job_description_file = st.file_uploader("Upload the Job Description (PDF or DOCX)", type=["pdf", "docx"])

resume_raw_text = ""
job_description_raw_text = ""

if resume_file:
    with st.spinner("Processing Resume..."):
        if resume_file.type == "application/pdf":
            resume_raw_text = extract_text_from_pdf(resume_file)
        elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_raw_text = extract_text_from_docx(resume_file)
        else:
            st.error("Unsupported resume file type. Please upload a PDF or DOCX.")

if job_description_file:
    with st.spinner("Processing Job Description..."):
        if job_description_file.type == "application/pdf":
            job_description_raw_text = extract_text_from_pdf(job_description_file)
        elif job_description_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            job_description_raw_text = extract_text_from_docx(job_description_file)
        else:
            st.error("Unsupported job description file type. Please upload a PDF or DOCX.")

if st.button("🔍 Analyze Match"):
    if resume_raw_text and job_description_raw_text:
        st.subheader("📊 Analysis Results")

        cleaned_resume = clean_text(resume_raw_text)
        cleaned_jd = clean_text(job_description_raw_text)

        match_score, missing_skills = calculate_skill_match(cleaned_resume, cleaned_jd)

        st.markdown(f"""
        <div style='font-size: 22px; padding: 10px; border-radius: 10px; background-color: #e6f4ea; color: #264653;'>
             <strong>Skill Match Score:</strong> <span style='color: green;'>{match_score:.2f}%</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("🔎 Missing Skills/Keywords")

        if missing_skills:
            st.warning("Your resume is missing the following key terms from the job description:")
            st.markdown("**`" + "`, `".join(missing_skills) + "`**")
            st.info("Add these relevant keywords to improve your match!")
        else:
            st.success("Great job! Your resume includes all key terms from the job description.")
    else:
        st.warning("Please upload **both** the resume and job description to proceed.")

# --- Footer ---
st.markdown("<div class='footer'>© 2025 ResumeMatcher Pro | All rights reserved.</div>", unsafe_allow_html=True)
