import sys
import os

# این کد مسیر فعلی برنامه را به پایتون معرفی می‌کند تا پوشه‌های core و agents را پیدا کند
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# حالا بقیه importها را قرار دهید
import streamlit as st
from core.brain import Brain
from agents.pedagogy_agent import PedagogyAgent
# ... بقیه کدها

import streamlit as st
from core.brain import Brain
from agents.pedagogy_agent import PedagogyAgent
from agents.research_agent import ResearchAgent
from agents.design_agent import AdvancedDesignAgent
from agents.quiz_agent import QuizAgent
from utils.doc_generator import DocGenerator
import openai

st.set_page_config(page_title="SmartTeacher AI", layout="wide")
st.title("🎓 SmartTeacher AI")
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
    client = openai.OpenAI(api_key=api_key)
    st.success("✅ متصل به سرور هوشمند")
    
    # نمونه سازی از کلاس‌ها
    pedagogy = PedagogyAgent(client)
    quiz = QuizAgent(client)
    research = ResearchAgent(client)
    design = AdvancedDesignAgent(client)
    doc_gen = DocGenerator()

    tab1, tab2, tab3, tab4 = st.tabs(["📝 طرح درس", "❓ آزمون", "📊 پاورپوینت", "🔍 پژوهش"])

    with tab1:
        sub = st.text_input("درس")
        gr = st.selectbox("پایه", ["هفتم", "هشتم", "نهم"])
        top = st.text_input("موضوع")
        if st.button("تولید"):
            res = pedagogy.generate_content(sub, gr, top, "طرح درس")
            st.write(res)
            fn = doc_gen.save_as_word(res, "lesson.docx")
            st.download_button("📥 دانلود", open(fn, "rb"), file_name=fn)

    with tab2:
        st.write("بخش آزمون آماده است...")

else:
    st.warning("لطفاً API Key را در تنظیمات (Secrets) وارد کنید.")
