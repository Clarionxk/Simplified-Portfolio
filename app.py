from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Portfolio | Alvin 'Zeilver' Poh"
PAGE_ICON = ":random:"
NAME = "Alvin Poh"
DESCRIPTION = """
 Digital Marketer, Growth Hacker, Youtube Brand Manager, Co-founder of Axiverse Guilld (Axie Infinity) 
 """
EMAIL = "zeilver.plays@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UConKNdIzNLUNdondCtpFQYA/",
    "LinkedIn": "https://linkedin.com",
    "Github": "https://github.com",
    "Instagram":  "https://www.instagram.com/altricks/"

}
PROJECTS = {

    "✅ YouTube Brand Manager - Managing Over 7 Popular Youtube Channels and helping maintaining their Quality and Growth": "https://youtube.com",
    "✅ Digital Marketer with hundreds of satisfied customers and clients over the world ": "https://facebook.com",
    "✅ Cryptocurrency Trader and Investor with Millions of Successful Deals and trades": "https://binance.com",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=240)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 💾 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",


    )
    st.write("📝", EMAIL)


# --- SOCIAL LINKS ---
st.write ("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS --
st.write("#")
st.subheader("Experience")
st.write(
    """
    - ✅ YouTube Brand Manager - Managing Over 7 Popular Youtube Channels 
    - ✅ Digital Marketer with hundreds of satisfied customers and clients over the world 
    - ✅ Cryptocurrency Trader and Investor with Millions of Successful Deals and trades
    
    """

)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(

    """
    - 🤖 AI Prompt Expert: Can Utilize Any AI Tool to achieve the best Result Available.
    - 📊 Data Visualization: Experienced with Google Sheets, Docs, MS Excel and Word
    - 🌐 Social Media Marketing: Facebook, Youtube, Instagram, and TikTok
    
    """
)

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- Job 1
st.write("🎮", "**Business Consultant | Xepher Esports Group**")
st.write("03/2023")
st.write("""
- ▶ Experienced Business Consultant with a proven track record of driving organizational growth and optimizing business processes. With 3 years of industry experience, I have successfully partnered with diverse clients across various sectors to deliver strategic insights, innovative solutions, and measurable results
- ▶ My expertise lies in conducting comprehensive business assessments, identifying areas of improvement, and developing tailored strategies to enhance operational efficiency and profitability.
- ▶ As a trusted advisor, I have collaborated with senior executives and cross-functional teams to implement change management initiatives, streamline workflows, and foster a culture of continuous improvement. My strong communication and interpersonal skills have enabled me to build relationships and effectively communicate complex concepts to stakeholders at all levels.
""")


# --- Projects ---

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

































