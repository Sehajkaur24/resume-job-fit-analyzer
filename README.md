# 🧠 Resume–Job Fit Analyzer

An AI-powered web application that analyzes your resume against a job description to calculate a **Skill Match Score**, identify **missing skills**, and help improve resume alignment using NLP techniques.

---

## 📷 Demo Screenshot
<img width="520" height="813" alt="Screenshot 2025-07-28 101632" src="https://github.com/user-attachments/assets/ee957950-b39d-4d42-bdba-7b467831ad32" />

---

## 🚀 Live App

Try the app live here:  
🔗 https://resume-job-fit-analyzer-fbtj272hz7tj8iztpawarz.streamlit.app/

---

## 🔧 Tech Stack

| Tool          | Purpose                         |
|---------------|---------------------------------|
| `Streamlit`   | Frontend + deployment framework |
| `python-docx` | Extract text from DOCX files    |
| `pdfminer`    | Extract text from PDF files     |
| `scikit-learn`| TF-IDF vectorization and Cosine Similarity |
| `numpy`, `scipy` | Math and similarity metrics     |

---

## 💡 How to Use

1. 📄 Upload your **Resume** in `.pdf` or `.docx` format
2. 📃 Upload the **Job Description** in `.pdf` or `.docx` format
3. 🔍 The app will analyze both files
4. ✅ View your **Skill Match Score** and **Missing Skills**

📁 You can test with sample files:
- `sample_resume.docx`
- `sample_job_description.pdf`

---

## 📦 Installation (Optional: Run Locally)

```bash
git clone https://github.com/Sehajkaur24/resume-job-fit-analyzer.git
cd resume-job-fit-analyzer
pip install -r requirements.txt
streamlit run app.py
