"""Flagship projects — a filterable card gallery pulled from the experience data."""

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

st.set_page_config(page_title="Projects - " + PROFILE["name"], page_icon="🚀", layout="wide")
apply_base_style()
render_sidebar_profile(PROFILE)

section_header("🚀", "Flagship Projects", "Selected work spanning Agentic AI, GenAI, healthcare, and industrial ML.")

all_projects = []
for role in EXPERIENCE:
    for project in role["projects"]:
        all_projects.append({**project, "company": role["company"]})

all_tech = sorted({tech for p in all_projects for tech in p["tech"]})
tech_filter = st.multiselect("Filter by technology", options=all_tech, default=[])

search = st.text_input("🔍 Search projects", placeholder="e.g. LangGraph, Healthcare, Flask")

filtered = all_projects
if tech_filter:
    filtered = [p for p in filtered if any(t in p["tech"] for t in tech_filter)]
if search:
    q = search.lower()
    filtered = [
        p
        for p in filtered
        if q in p["name"].lower()
        or q in p["client"].lower()
        or any(q in t.lower() for t in p["tech"])
        or any(q in pt.lower() for pt in p["points"])
    ]

st.caption(f"Showing {len(filtered)} of {len(all_projects)} projects")

cols = st.columns(2)
for i, project in enumerate(filtered):
    with cols[i % 2]:
        card_start()
        st.markdown(f"#### {project['name']}")
        st.markdown(f"**Client:** {project['client']} .  **Company:** {project['company']}")
        render_pills(project["tech"], variant="tech")
        st.markdown("")
        for point in project["points"][:4]:
            st.markdown(f"- {point}")
        if len(project["points"]) > 4:
            with st.expander("Show more"):
                for point in project["points"][4:]:
                    st.markdown(f"- {point}")
        card_end()

if not filtered:
    st.warning("No projects match those filters - try clearing the search or technology filter.")

render_footer(PROFILE)
