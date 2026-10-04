"""Contact page — links plus a mailto-based contact form (no backend/server needed)."""

import urllib.parse
import streamlit as st

from data.resume_data import PROFILE
from utils.ui import (
    apply_base_style,
    card_end,
    card_start,
    render_footer,
    render_sidebar_profile,
    section_header,
)

st.set_page_config(page_title="Contact — " + PROFILE["name"], page_icon="📬", layout="wide")
apply_base_style()
render_sidebar_profile(PROFILE)

section_header("📬", "Get In Touch", "Open to collaborations, speaking invitations, mentoring, and consulting.")

col1, col2 = st.columns([1, 1.2])

with col1:
    card_start()
    st.markdown("#### Direct Contact")
    st.markdown(f"📧 **Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})")
    st.markdown(f"📱 **Phone:** {PROFILE['phone']}")
    st.markdown(f"🎓 **Google Scholar:** [View profile]({PROFILE['scholar_url']})")
    st.markdown(f"📍 **Location:** {PROFILE['location']}")
    card_end()

with col2:
    card_start()
    st.markdown("#### Send a Message")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        reason = st.selectbox(
            "Reason for reaching out",
            ["Collaboration", "Speaking / Workshop Invitation", "Mentoring", "Consulting", "Other"],
        )
        message = st.text_area("Message", height=140)
        sent = st.form_submit_button("Prepare message", use_container_width=True)

        if sent:
            if not message.strip():
                st.warning("Please write a message before sending.")
            else:
                subject = urllib.parse.quote(f"Portfolio contact - {reason}")
                body = urllib.parse.quote(
                    f"Name: {name or 'Not provided'}\nEmail: {email or 'Not provided'}\n\n{message}"
                )
                mailto = f"mailto:{PROFILE['email']}?subject={subject}&body={body}"
                st.success("Your message is ready - click below to send it from your email client:")
                st.markdown(f"[✉️ Open Email Client]({mailto})")
    card_end()

render_footer(PROFILE)
