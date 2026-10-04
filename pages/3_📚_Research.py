"""Publications, patents, and Ph.D. thesis — the research side of the profile."""

import streamlit as st

from data.resume_data import CORPORATE_TRAINING, PATENTS, PHD_THESIS, PROFILE, PUBLICATIONS, SCHOLAR_STATS
from utils.ui import (
    apply_base_style,
    card_end,
    card_start,
    render_footer,
    render_pills,
    render_sidebar_profile,
    section_header,
)

st.set_page_config(page_title="Research — " + PROFILE["name"], page_icon="🔬", layout="wide")
apply_base_style()
render_sidebar_profile(PROFILE)

section_header(
    "🔬",
    "Publications & Patents",
    f"{SCHOLAR_STATS['citations_all']:,}+ citations across journals, conferences, and granted patents.",
)

tab_pubs, tab_patents, tab_thesis = st.tabs(["📚 Publications", "📜 Patents", "🎓 Ph.D. Thesis"])

with tab_pubs:
    search = st.text_input("🔍 Search publications", placeholder="e.g. SHAP, crop recommendation, GAN")
    pubs = PUBLICATIONS
    if search:
        q = search.lower()
        pubs = [p for p in pubs if q in p["title"].lower() or q in p["venue"].lower()]
    st.caption(f"{len(pubs)} of {len(PUBLICATIONS)} publications")

    card_start()
    for pub in pubs:
        st.markdown(
            f"""
            <div class="pub-row">
                <div class="pub-title">{pub['title']}</div>
                <div class="pub-venue">{pub['venue']}</div>
                <a href="{pub['url']}" target="_blank">{pub['url']}</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    card_end()

with tab_patents:
    for patent in PATENTS:
        card_start()
        status_color = "#16A34A" if "Granted" in patent["status"] else "#D97706"
        st.markdown(
            f"#### {patent['title']}  "
            f"<span style='font-size:0.75rem; font-weight:700; color:{status_color};'>"
            f" . {patent['status']}</span>",
            unsafe_allow_html=True,
        )
        st.markdown(f"**{patent['id']}**")
        st.markdown(f"Inventors: {patent['inventors']}")
        if patent.get("note"):
            st.caption(patent["note"])
        card_end()

with tab_thesis:
    card_start()
    st.markdown(f"### {PHD_THESIS['title']}")
    st.markdown(f"**Status:** {PHD_THESIS['status']}  .  **Supervisors:** {PHD_THESIS['supervisors']}")
    st.write(PHD_THESIS["summary"])
    render_pills(PHD_THESIS["tech"], variant="tech")
    st.markdown("#### Key Technical Contributions")
    for c in PHD_THESIS["contributions"]:
        st.markdown(f"- {c}")
    card_end()

section_header("🎖️", "Scientific & Editorial Leadership")
card_start()
for item in CORPORATE_TRAINING:
    st.markdown(f"- {item}")
card_end()

render_footer(PROFILE)
