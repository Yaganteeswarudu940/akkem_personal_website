"""Teaching experience, corporate training, and invited talks."""

import pandas as pd
import streamlit as st

from data.resume_data import INVITED_TALKS, PROFILE, TEACHING
from utils.ui import (
    apply_base_style,
    card_end,
    card_start,
    render_footer,
    render_pills,
    render_sidebar_profile,
    section_header,
)

st.set_page_config(page_title="Teaching & Talks — " + PROFILE["name"], page_icon="👨‍🏫", layout="wide")
apply_base_style()
render_sidebar_profile(PROFILE)

section_header("👨‍🏫", "Teaching & Academic Contributions")

card_start()
st.markdown(f"### {TEACHING['role']}")
st.markdown(f"**{TEACHING['duration']}**")
render_pills(TEACHING["subjects"])
st.markdown("")
st.markdown(f"💡 {TEACHING['note']}")
card_end()

section_header("🎤", "Invited Talks & Workshops", "Knowledge transfer to 250+ students and professionals across institutions.")

df = pd.DataFrame(INVITED_TALKS).rename(
    columns={"date": "Date", "host": "Host / Audience", "topic": "Topic", "impact": "Outcome"}
)
st.dataframe(df, use_container_width=True, hide_index=True)

render_footer(PROFILE)
