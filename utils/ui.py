"""Shared visual building blocks for every page of the portfolio.
 
Theme: an academic "faculty profile" look (navy headings, orange accent
underline, light lavender banner, blue stat tiles) — keeping the CSS and
small HTML helpers here means every page looks consistent and a single
edit updates the whole site.
"""
 
from __future__ import annotations
 
import base64
from pathlib import Path
 
import streamlit as st
 
ROOT_DIR = Path(__file__).resolve().parent.parent
 
BADGE_COLORS = {
    "navy": ("#1B2A66", "rgba(27, 42, 102, 0.12)"),
    "orange": ("#C2560C", "rgba(232, 112, 42, 0.16)"),
    "green": ("#146C43", "rgba(20, 108, 67, 0.14)"),
    "teal": ("#0F766E", "rgba(14, 165, 164, 0.14)"),
}
 
BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
 
html, body, [class*="css"]  {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
 
/* Tighten the default top padding */
.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1140px;
}
 
/* Hide default Streamlit chrome we don't need */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
 
/* ---------- Faculty banner (top name strip) ---------- */
.faculty-banner {
    background: linear-gradient(120deg, #EAF0FC 0%, #F3EFFC 60%, #EAF4FB 100%);
    border: 1px solid rgba(27, 42, 102, 0.08);
    border-radius: 16px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.4rem;
}
.faculty-banner h1 {
    color: #16215C !important;
    font-size: 2.1rem;
    font-weight: 800;
    margin: 0 0 0.2rem 0;
}
.faculty-banner .faculty-subtitle {
    color: #3B4878;
    font-size: 1.02rem;
    font-weight: 500;
}
 
/* ---------- Photo frame (rectangular portrait) ---------- */
.photo-frame {
    width: 100%;
    aspect-ratio: 4 / 5;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid rgba(27, 42, 102, 0.15);
    box-shadow: 0 6px 18px rgba(16, 25, 63, 0.10);
    background: linear-gradient(145deg, #1B2A66, #2F6FAE);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 1rem;
}
.photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
 
/* ---------- Stat tiles ---------- */
.stat-tile-row { display: flex; gap: 0.7rem; flex-wrap: wrap; margin-bottom: 1.2rem; }
.stat-tile {
    flex: 1 1 120px;
    border-radius: 12px;
    padding: 1rem 0.8rem;
    text-align: center;
}
.stat-tile.dark { background: #2F6FAE; color: #FFFFFF; }
.stat-tile.light { background: #DCEAFA; color: #16215C; }
.stat-tile .stat-value { font-size: 1.7rem; font-weight: 800; line-height: 1.1; }
.stat-tile .stat-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    opacity: 0.9;
    margin-top: 0.25rem;
}
 
/* ---------- Info / Key Notes side boxes ---------- */
.side-box {
    background: #FFFFFF;
    border: 1px solid rgba(27, 42, 102, 0.12);
    border-radius: 12px;
    padding: 1.1rem 1.2rem;
    margin-bottom: 1rem;
}
.side-box-title {
    color: #D9641E;
    font-weight: 800;
    font-size: 1.0rem;
    margin-bottom: 0.6rem;
}
.side-box .field { font-size: 0.88rem; margin-bottom: 0.35rem; line-height: 1.4; }
.side-box .field b { color: #16215C; }
 
.keynote-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    font-size: 0.86rem;
    padding: 0.3rem 0;
    border-bottom: 1px dashed rgba(27, 42, 102, 0.12);
}
.keynote-row:last-child { border-bottom: none; }
.keynote-label { color: #334066; }
 
.badge-count {
    display: inline-block;
    min-width: 1.6rem;
    text-align: center;
    padding: 0.08rem 0.5rem;
    border-radius: 999px;
    font-weight: 800;
    font-size: 0.8rem;
}
 
/* ---------- Scholar citation box ---------- */
.scholar-box { background: #F8FAFD; }
.scholar-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin-top: 0.4rem; }
.scholar-table th { text-align: left; color: #6B7280; font-weight: 600; padding: 0.2rem 0.3rem; }
.scholar-table td { padding: 0.25rem 0.3rem; color: #16215C; font-weight: 700; }
.scholar-table .metric-name { color: #D9641E; font-weight: 700; }
 
/* ---------- Section headers with orange underline ---------- */
.section-header {
    margin: 1.7rem 0 0.9rem 0;
}
.section-header .icon { font-size: 1.3rem; margin-right: 0.4rem; }
.section-header h2 {
    display: inline;
    color: #16215C;
    margin: 0;
    font-size: 1.4rem;
    font-weight: 800;
}
.section-header .underline-bar {
    width: 64px;
    height: 4px;
    background: #E8702A;
    border-radius: 2px;
    margin-top: 0.45rem;
}
.section-caption {
    color: #6B7280;
    margin-top: 0.3rem;
    margin-bottom: 0.6rem;
    font-size: 0.95rem;
}
.biosketch-quote {
    font-style: italic;
    color: #3B4878;
    border-left: 3px solid #E8702A;
    padding-left: 0.9rem;
    margin: 0.5rem 0 1rem 0;
}
 
/* ---------- Cards ---------- */
.oh-card {
    background: var(--background-color, #FFFFFF);
    border: 1px solid rgba(27, 42, 102, 0.12);
    border-radius: 14px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 10px rgba(16, 25, 63, 0.04);
}
.oh-card h3, .oh-card h4 {
    margin-top: 0;
    color: #16215C;
}
 
/* ---------- Pills / tags ---------- */
.pill-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.35rem 0 0.2rem 0; }
.pill {
    display: inline-block;
    padding: 0.28rem 0.75rem;
    border-radius: 999px;
    background: rgba(27, 42, 102, 0.08);
    color: #16215C;
    font-size: 0.82rem;
    font-weight: 600;
    white-space: nowrap;
}
.pill.tech {
    background: rgba(232, 112, 42, 0.12);
    color: #C2560C;
}
 
/* ---------- Timeline ---------- */
.timeline { border-left: 3px solid rgba(27, 42, 102, 0.20); margin-left: 0.6rem; padding-left: 1.4rem; }
.timeline-item { position: relative; padding-bottom: 1.5rem; }
.timeline-item::before {
    content: '';
    position: absolute;
    left: -1.86rem;
    top: 0.25rem;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #E8702A;
    border: 3px solid rgba(232, 112, 42, 0.25);
}
.timeline-year {
    font-weight: 800;
    color: #16215C;
    font-size: 0.95rem;
}
.timeline-event { color: var(--text-color, inherit); font-size: 0.95rem; margin-top: 0.15rem; }
 
/* ---------- Publication / patent rows ---------- */
.pub-row {
    padding: 0.85rem 0;
    border-bottom: 1px solid rgba(27, 42, 102, 0.10);
}
.pub-row:last-child { border-bottom: none; }
.pub-title { font-weight: 700; font-size: 1.0rem; color: #16215C; }
.pub-venue { color: #6B7280; font-size: 0.88rem; margin-top: 0.15rem; }
 
/* ---------- Expander (accordion) accent ---------- */
div[data-testid="stExpander"] {
    border: 1px solid rgba(27, 42, 102, 0.14) !important;
    border-top: 3px solid #E8702A !important;
    border-radius: 10px !important;
}
 
/* ---------- Footer ---------- */
.oh-footer {
    text-align: center;
    color: #9CA3AF;
    font-size: 0.85rem;
    margin-top: 2.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(27, 42, 102, 0.10);
}
</style>
"""
 
 
def apply_base_style() -> None:
    st.markdown(BASE_CSS, unsafe_allow_html=True)
 
 
def _avatar_inner_html(profile: dict) -> str:
    photo_path = ROOT_DIR / profile.get("photo_file", "")
    if photo_path.exists():
        data = base64.b64encode(photo_path.read_bytes()).decode()
        ext = photo_path.suffix.lstrip(".") or "jpg"
        return f'<img src="data:image/{ext};base64,{data}" alt="profile photo"/>'
    return profile.get("initials", "AY")
 
 
def render_faculty_banner(profile: dict) -> None:
    st.markdown(
        f"""
        <div class="faculty-banner">
            <h1>{profile['name']}</h1>
            <div class="faculty-subtitle">{profile['title']} · {profile['subtitle']} ·  {profile['location']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
 
# def render_photo_frame(profile: dict) -> None:
#     inner = _avatar_inner_html(profile)
#     st.markdown(f'<div class="photo-frame">{inner}</div>', unsafe_allow_html=True)
 
def render_photo_frame(profile):
    photo_path = Path(__file__).resolve().parent.parent / "assets" / "akkem.jpeg"

    if photo_path.exists():
        st.image(
            str(photo_path),
            width="stretch",
        )
    else:
        st.markdown(
            """
            <div class="photo-placeholder">
                AY
            </div>
            """,
            unsafe_allow_html=True,
        )

 
def render_stat_tiles(metrics: list[dict]) -> None:
    tiles = "".join(
        f'<div class="stat-tile {"dark" if i % 2 == 0 else "light"}">'
        f'<div class="stat-value">{m["value"]}</div><div class="stat-label">{m["label"]}</div></div>'
        for i, m in enumerate(metrics)
    )
    st.markdown(f'<div class="stat-tile-row">{tiles}</div>', unsafe_allow_html=True)
 
 
def render_info_box(profile: dict) -> None:
    st.markdown(
        f"""
        <div class="side-box">
            <div class="side-box-title">Information</div>
            <div class="field"><b>Designation:</b> {profile['title']}</div>
            <div class="field"><b>Email:</b> {profile['email']}</div>
            <div class="field"><b>Phone:</b> {profile['phone']}</div>
            <div class="field"><b>Location:</b> {profile['location']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
 
def render_keynotes_box(items: list[dict]) -> None:
    rows = []
    for item in items:
        text_color, bg_color = BADGE_COLORS.get(item.get("color", "navy"), BADGE_COLORS["navy"])
        rows.append(
            f'<div class="keynote-row"><span class="keynote-label">{item["label"]}</span>'
            f'<span class="badge-count" style="color:{text_color}; background:{bg_color};">'
            f'{item["value"]}</span></div>'
        )
    st.markdown(
        f'<div class="side-box"><div class="side-box-title">Key Notes</div>{"".join(rows)}</div>',
        unsafe_allow_html=True,
    )
 
 
def render_scholar_box(stats: dict) -> None:
    st.markdown(
        f"""
        <div class="side-box scholar-box">
            <div class="side-box-title">  Cited By (Google Scholar)</div>
            <table class="scholar-table">
                <tr><th></th><th>All</th><th>Since 2021</th></tr>
                <tr><td class="metric-name">Citations</td><td>{stats['citations_all']}</td>
                    <td>{stats['citations_since2021']}</td></tr>
                <tr><td class="metric-name">h-index</td><td>{stats['h_index_all']}</td>
                    <td>{stats['h_index_since2021']}</td></tr>
                <tr><td class="metric-name">i10-index</td><td>{stats['i10_all']}</td>
                    <td>{stats['i10_since2021']}</td></tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(f"[View full Google Scholar profile ↗]({stats['profile_url']})")
 
 
def section_header(icon: str, title: str, caption: str | None = None) -> None:
    st.markdown(
        f"""
        <div class="section-header">
            <span class="icon">{icon}</span><h2>{title}</h2>
            <div class="underline-bar"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if caption:
        st.markdown(f'<div class="section-caption">{caption}</div>', unsafe_allow_html=True)
 
 
def pills(items: list[str], variant: str = "default") -> str:
    css_class = "pill tech" if variant == "tech" else "pill"
    chips = "".join(f'<span class="{css_class}">{item}</span>' for item in items)
    return f'<div class="pill-row">{chips}</div>'
 
 
def render_pills(items: list[str], variant: str = "default") -> None:
    st.markdown(pills(items, variant), unsafe_allow_html=True)
 
 
def card_start(extra_style: str = "") -> None:
    st.markdown(f'<div class="oh-card" style="{extra_style}">', unsafe_allow_html=True)
 
 
def card_end() -> None:
    st.markdown("</div>", unsafe_allow_html=True)
 
 
def render_timeline(items: list[dict], year_key: str = "year", event_key: str = "event") -> None:
    # Built as single-line HTML fragments: joined multi-line/indented fragments get
    # misread as Markdown indented code blocks instead of raw HTML.
    rows = "".join(
        f'<div class="timeline-item"><div class="timeline-year">{item[year_key]}</div>'
        f'<div class="timeline-event">{item[event_key]}</div></div>'
        for item in items
    )
    st.markdown(f'<div class="timeline">{rows}</div>', unsafe_allow_html=True)
 
 
def render_footer(profile: dict) -> None:
    st.markdown(
        f"""
        <div class="oh-footer">
            Built with Streamlit · {profile['name']} © 2026 ·
            <a href="mailto:{profile['email']}" style="color:#E8702A;">{profile['email']}</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
 
def render_sidebar_profile(profile: dict) -> None:
    avatar_html = _avatar_inner_html(profile)
    st.sidebar.markdown(
        f"""
        <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
            <div style="width:88px; height:88px; border-radius:50%; margin:0 auto; overflow:hidden;
                 background:rgba(27,42,102,0.10); border:2px solid rgba(27,42,102,0.25);
                 display:flex; align-items:center; justify-content:center;
                 font-size:1.9rem; font-weight:800; color:#16215C;">{avatar_html}</div>
            <div style="font-weight:800; margin-top:0.6rem; font-size:1.02rem; color:#16215C;">{profile['name']}</div>
            <div style="color:#6B7280; font-size:0.85rem;">{profile['title']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        f"""
        <div style="text-align:center; font-size:0.85rem; margin-bottom:0.8rem;">
             <a href="mailto:{profile['email']}">{profile['email']}</a><br/>
             <a href="{profile['scholar_url']}" target="_blank">Google Scholar</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.divider()
