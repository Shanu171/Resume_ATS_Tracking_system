from dotenv import load_dotenv

load_dotenv()


import streamlit as st 
import os 
import pdf2image 
from PIL import Image
import google.generativeai as genai 
import io
import base64




genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def  get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content([input,pdf_content,prompt])
    return response.text 



def input_pdf_setup(uploaded_file):
    ## Convert PDF to image
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        # Get the first page as an image
        first_page = images[0]

        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Create a dict for the first page
        pdf_part = {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
        }
        return pdf_part
    else:
        raise FileNotFoundError("No file uploaded")
## Streamlit APP 

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:",key = "input")
uploaded_file= st.file_uploader("Upload Your  Resume in PDF...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell me about the Resume")

#submit2 = st.button("How can I Improvise my Skills")

submit3 = st.button("Percentage Match")


input_prompt1 = """
You are an experienced HR professional with expertise in technical domains, 
including Data Science, Full Stack Java Development, Full Stack Web Development, 
Big Data Engineering, Data Engineering, Data Analysis, and Data Science.
Your task is to evaluate the provided resume against the job description for roles in these domains.
Provide a detailed professional assessment on whether the candidate’s profile aligns with the specified role. 
Highlight both the strengths and weaknesses of the candidate in relation to the job requirements. 
Focus on their technical skills, relevant experience, and any missing qualifications or keywords that may 
affect their suitability for the role.

"""


input_prompt3 = """
You are a highly skilled ATS (Applicant Tracking System) evaluator with deep expertise in technical fields such as Data Science, Full Stack Java Development, Full Stack Web Development, Big Data Engineering, Data Engineering, and Data Analysis. You also possess a strong understanding of ATS functionalities.

Your task is to analyze the provided resume in comparison to the job description. Calculate the percentage match between the resume and the job description. 

In your output:
1. Begin by providing the overall match percentage.
2. List any key skills, keywords, or qualifications present in the job description that are missing in the resume. Ensure these are detailed and categorized (e.g., technical skills, certifications, or experience).
3. Conclude with actionable recommendations for improving the resume to better align with the job description.

"""

if  submit1: 
    if uploaded_file is  not None:
        pdf_content =   input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)

    else:
        st.write("Please upload the Resume")

elif submit3:
    if uploaded_file is  not None:
        pdf_content =   input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the Resume")






