"""Home page - academic-style faculty profile for Dr. Akkem Yaganteeswarudu."""

from pathlib import Path

import streamlit as st

from data.resume_data import (
    AREAS_OF_INTEREST,
    BIOSKETCH_QUOTE,
    BIOSKETCH_TEXT,
    CERTIFICATIONS,
    CITATION_TIMELINE,
    CORE_COMPETENCIES,
    CORPORATE_TRAINING,
    EDUCATION,
    EXPERIENCE,
    KEY_NOTES,
    PATENTS,
    PROFILE,
    PUBLICATIONS,
    SCHOLAR_STATS,
)
from utils.ui import (
    apply_base_style,
    render_faculty_banner,
    render_footer,
    render_info_box,
    render_keynotes_box,
    render_photo_frame,
    render_pills,
    render_scholar_box,
    render_sidebar_profile,
    render_stat_tiles,
    section_header,
)

st.set_page_config(
    page_title=f"{PROFILE['name']} — Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_base_style()
render_sidebar_profile(PROFILE)

st.sidebar.markdown("**Navigate using the pages above** ⬆️")
st.sidebar.caption(
    "Home . Experience . Projects . Research . Teaching & Talks . Career Guide . Contact"
)

resume_path = Path(__file__).parent / PROFILE["resume_file"]
if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.sidebar.download_button(
            "⬇️ Download Resume (PDF)",
            data=f.read(),
            file_name="Akkem_Yaganteeswarudu_Resume.pdf",
            mime="application/pdf",
            width="stretch",
        )
else:
    st.sidebar.caption("💡 Add `assets/resume.pdf` to enable a resume download button here.")

# ---------------------------------------------------------------------------
# Name banner
# ---------------------------------------------------------------------------
render_faculty_banner(PROFILE)

# ---------------------------------------------------------------------------
# Photo + Information + Key Notes (left) | Stats + Biosketch + Interests (right)
# ---------------------------------------------------------------------------
left_col, right_col = st.columns([1, 2.4], gap="large")

with left_col:
    render_photo_frame(PROFILE)
    render_info_box(PROFILE)
    render_keynotes_box(KEY_NOTES)
    render_scholar_box(SCHOLAR_STATS)

with right_col:
    stat_tiles = [
        {"label": "Publications", "value": len(PUBLICATIONS)},
        {"label": "Professionals Trained", "value": "1,000+"},
        {"label": "Patents", "value": len(PATENTS)},
        {"label": "Flagship Projects", "value": sum(len(role["projects"]) for role in EXPERIENCE)},
    ]
    render_stat_tiles(stat_tiles)

    section_header("📝", "Introduction [Biosketch]")
    st.markdown(f'<div class="biosketch-quote">{BIOSKETCH_QUOTE}</div>', unsafe_allow_html=True)
    st.write(BIOSKETCH_TEXT)

    section_header("🎯", "Areas of Interest")
    aoi_cols = st.columns(2)
    for i, area in enumerate(AREAS_OF_INTEREST):
        aoi_cols[i % 2].markdown(f"- {area}")

    st.markdown("##### 📈 Citations by Year")
    st.bar_chart(CITATION_TIMELINE)

# ---------------------------------------------------------------------------
# Accordion sections — condensed highlights with links to the full pages
# ---------------------------------------------------------------------------
section_header("📂", "Profile Details", "Expand a section for a quick summary, or use the sidebar for full detail.")

with st.expander(f"🎓 Education Qualification  .  {len(EDUCATION)} degrees"):
    for edu in EDUCATION:
        st.markdown(
            f"**{edu['course']}** - {edu['institute']} ({edu['branch']})  \n"
            f"Score: {edu['score']}  |  Supervisor(s): {edu['supervisor']}"
        )
        st.markdown("---")

with st.expander(f"📄 Publications  ·  {len(PUBLICATIONS)} papers"):
    for pub in PUBLICATIONS:
        cite = f" . Cited by {pub['citations']}" if pub.get("citations") else ""
        st.markdown(f"**{pub['title']}**  \n{pub['venue']}{cite}  \n[{pub['url']}]({pub['url']})")
        st.markdown("---")
    st.page_link("pages/3_📚_Research.py", label="Open full Research page →", icon="📚")

with st.expander(f"💼 Professional Experience  ·  {len(EXPERIENCE)} roles"):
    for role in EXPERIENCE:
        st.markdown(f"**{role['role']}** - {role['company']}  ·  {role['duration']}")
    st.page_link("pages/1_💼_Experience.py", label="Open full Experience page →", icon="💼")

with st.expander(f"🧰 Core Competencies  .  {len(CORE_COMPETENCIES)} areas"):
    for comp in CORE_COMPETENCIES:
        st.markdown(f"**{comp['icon']} {comp['category']}**")
        render_pills(comp["skills"])

with st.expander(f"🏆 Patents  .  {len(PATENTS)} filings"):
    for patent in PATENTS:
        st.markdown(f"**{patent['title']}** — {patent['status']}  \n{patent['id']}")
        st.markdown("---")

with st.expander(f"🎖️ Certifications & Recognition  ·  {len(CERTIFICATIONS)} certifications"):
    for cert in CERTIFICATIONS:
        st.markdown(f"- ✅ {cert}")
    st.markdown("")
    for item in CORPORATE_TRAINING:
        st.markdown(f"- {item}")

with st.expander("🌟 Achievements"):
    st.markdown("- Automated 40% of routine Business Case Modelling at Deloitte, saving ~1,200 man-hours/year.")
    st.markdown("- Trained 1,000+ professionals with a 4.8/5.0 satisfaction score and 70% skill-adoption rate.")
    st.markdown("- Reviewed 1,00,000+ LLM training prompts, accelerating fine-tuning schedules by 2 months.")
    st.markdown("- 1,450+ Google Scholar citations across 13 peer-reviewed publications.")
    st.page_link("pages/5_🧭_Career_Guide.py", label="See the full Career Journey →", icon="🧭")

render_footer(PROFILE)
