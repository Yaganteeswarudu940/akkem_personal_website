"""Career journey timeline + a mentoring-style guide for AI/ML careers."""

import streamlit as st

from data.resume_data import CAREER_ADVICE, CAREER_FAQ, CAREER_MILESTONES, PROFILE
from utils.ui import (
    apply_base_style,
    card_end,
    card_start,
    render_footer,
    render_sidebar_profile,
    render_timeline,
    section_header,
)

st.set_page_config(page_title="Career Guide — " + PROFILE["name"], page_icon="🛣️", layout="wide")
apply_base_style()
render_sidebar_profile(PROFILE)

section_header("🛣️", "Career Journey", "From Software Engineer to Ph.D. researcher to enterprise AI leader.")
card_start()
render_timeline(CAREER_MILESTONES)
card_end()

section_header("💡", "Career Advice", "Lessons distilled from 15+ years of building, teaching, and mentoring in AI.")
advice_cols = st.columns(2)
for i, advice in enumerate(CAREER_ADVICE):
    with advice_cols[i % 2]:
        card_start()
        st.markdown(f"#### {advice['icon']} {advice['title']}")
        st.write(advice["body"])
        card_end()

section_header("❓", "Frequently Asked Questions", "Questions I most often get from mentees and workshop attendees.")
for item in CAREER_FAQ:
    with st.expander(item["q"]):
        st.write(item["a"])

section_header("📩", "Ask a Question")
card_start()
st.write(
    "Have a career question that isn't answered above? Send it directly — I read every message "
    "and try to reply personally."
)
with st.form("career_question_form", clear_on_submit=True):
    name = st.text_input("Your name")
    question = st.text_area("Your question", height=110)
    submitted = st.form_submit_button("Prepare email")
    if submitted:
        if not question.strip():
            st.warning("Please write a question before sending.")
        else:
            import urllib.parse

            subject = urllib.parse.quote("Career question from portfolio site")
            body = urllib.parse.quote(f"From: {name or 'Anonymous'}\n\n{question}")
            mailto = f"mailto:{PROFILE['email']}?subject={subject}&body={body}"
            st.success("Click below to open your email client with this message pre-filled:")
            st.markdown(f"[ Send this question to {PROFILE['email']}]({mailto})")
card_end()

render_footer(PROFILE)
