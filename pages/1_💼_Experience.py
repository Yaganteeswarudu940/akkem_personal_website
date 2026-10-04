"""Work experience — chronological roles with expandable project detail."""

import streamlit as st

from data.resume_data import EXPERIENCE, PROFILE
from utils.ui import (
    apply_base_style,
    card_end,
    card_start,
    render_footer,
    render_pills,
    render_sidebar_profile,
    section_header,
)

st.set_page_config(page_title="Experience -" + PROFILE["name"], page_icon="💼", layout="wide")
apply_base_style()
render_sidebar_profile(PROFILE)

section_header("💼", "Work Experience", "15+ years across product engineering, applied ML, and enterprise GenAI.")

companies = sorted({role["company"] for role in EXPERIENCE})
selected = st.multiselect("Filter by company", options=companies, default=[])

for role in EXPERIENCE:
    if selected and role["company"] not in selected:
        continue

    card_start()
    st.markdown(f"### {role['role']}")
    st.markdown(f"**{role['company']}** .  {role['duration']} .  {role['location']}")

    if role["highlights"]:
        st.markdown("")
        for h in role["highlights"]:
            st.markdown(f"- {h}")

    for project in role["projects"]:
        with st.expander(f"📌 {project['name']}  —  {project['client']}"):
            render_pills(project["tech"], variant="tech")
            st.markdown("")
            for point in project["points"]:
                st.markdown(f"- {point}")
    card_end()

render_footer(PROFILE)
