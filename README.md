# ATS Tracking System

The ATS Tracking System is a web-based application designed to assist job seekers in optimizing their resumes for Applicant Tracking Systems (ATS). Built using the Google Gemini model (gemini-1.5-flash-latest) and Streamlit, the platform offers users an intuitive and efficient way to improve their chances of landing their desired job.

Features

1. ATS Score Analysis

Users can:

Upload their resume.

Copy-paste the job description of the position they are applying for.

Receive an ATS score, which indicates how well their resume aligns with the job description.

2. Resume Insights

Upload your resume to get a brief analysis.

Receive insights into key strengths, areas of improvement, and alignment with common hiring trends.

Technology Stack

Frontend: Streamlit for creating an interactive web interface.

LLM: Google Gemini model (gemini-1.5-flash-latest) for advanced natural language processing.

Getting Started

Prerequisites

Python 3.9 or above

Google Cloud credentials to access the Gemini model

Installation

Clone the repository:

git clone https://github.com/yourusername/ats-tracking-system.git
cd ats-tracking-system

Install required dependencies:

pip install -r requirements.txt

Set up your Google Cloud credentials to enable access to the Gemini model.

Running the Application

Start the Streamlit app:

streamlit run app.py

Open the provided local URL in your browser to interact with the application.

How to Use

Launch the application.

Navigate to the ATS Score Analysis section:

Upload your resume (in PDF or DOCX format).

Copy-paste the job description.

Click "Analyze" to view the ATS score and suggestions.

Navigate to the Resume Insights section:

Upload your resume.

View a detailed summary and feedback about your resume.

File Structure

.
├── app.py                 # Main Streamlit application file
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
├── .env                   # API Key's

