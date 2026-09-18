from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root {
  --bg: #06111F;
  --bg-deep: #050D18;
  --sidebar: #0A192B;
  --surface: #0D1C2E;
  --surface-2: #10243A;
  --surface-hover: #142B45;
  --line: #1D3550;
  --line-strong: #2A4767;
  --text: #EAF2FF;
  --muted: #8FA6C1;
  --blue: #3488FF;
  --blue-soft: #153A67;
  --green: #25D99A;
  --red: #FF6577;
  --yellow: #F5C84C;
}
html, body, [class*="css"] {
  font-family: Pretendard, "Noto Sans KR", "Apple SD Gothic Neo", sans-serif;
  color-scheme: dark;
}
.stApp {
  color: var(--text);
  background:
    radial-gradient(circle at 72% -10%, rgba(32, 100, 170, .16), transparent 30%),
    linear-gradient(145deg, var(--bg-deep) 0%, var(--bg) 56%, #071524 100%);
}
.block-container {
  max-width: 1500px;
  padding: 1.8rem 2rem 4rem;
}
header[data-testid="stHeader"] {
  background: rgba(6, 17, 31, .86);
  border-bottom: 1px solid rgba(29, 53, 80, .7);
  backdrop-filter: blur(16px);
}
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #10243B 0%, #091727 52%, #0A192B 100%);
  border-right: 1px solid var(--line);
}
section[data-testid="stSidebar"] > div { padding-top: .9rem; }
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
  color: #AFC2D9;
}
[data-testid="stSidebar"] .stRadio > label { display: none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] { gap: .42rem; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  min-height: 48px;
  padding: .72rem .86rem;
  border: 1px solid transparent;
  border-radius: 10px;
  transition: all .16s ease;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
  background: rgba(52, 136, 255, .09);
  border-color: rgba(52, 136, 255, .15);
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  background: linear-gradient(90deg, rgba(52, 136, 255, .28), rgba(52, 136, 255, .10));
  border-color: rgba(52, 136, 255, .28);
  box-shadow: inset 3px 0 0 #4292FF;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) p {
  color: #62A6FF;
  font-weight: 750;
}
h1, h2, h3, h4 {
  color: var(--text) !important;
  letter-spacing: -.035em;
}
h1 { font-weight: 800; }
h2, h3 { font-weight: 750; }
p, li { line-height: 1.62; }
[data-testid="stMarkdownContainer"] p { color: #D4E0EF; }
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p { color: var(--muted) !important; }
[data-testid="stMetric"] {
  min-height: 118px;
  padding: 18px 20px;
  background: linear-gradient(145deg, rgba(16, 36, 58, .98), rgba(10, 27, 45, .98));
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, .18);
}
[data-testid="stMetricLabel"] p { color: #A8BBD1 !important; font-weight: 650; }
[data-testid="stMetricValue"] {
  color: var(--text);
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}
[data-testid="stMetricDelta"] svg { display: none; }
[data-testid="stVerticalBlockBorderWrapper"] {
  overflow: hidden;
  background: linear-gradient(145deg, rgba(14, 31, 50, .98), rgba(9, 24, 40, .98));
  border-color: var(--line) !important;
  border-radius: 14px !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, .17);
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
  border-color: var(--line-strong) !important;
}
.stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {
  min-height: 2.75rem;
  color: #DCEAFF;
  background: #112943;
  border-color: #2A4767;
  border-radius: 9px;
  font-weight: 720;
}
.stButton > button:hover, .stFormSubmitButton > button:hover, .stDownloadButton > button:hover {
  color: #FFFFFF;
  background: #183758;
  border-color: #3C6A99;
}
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"] {
  color: white;
  background: linear-gradient(135deg, #2477E8, #3488FF);
  border-color: #3488FF;
  box-shadow: 0 7px 18px rgba(52, 136, 255, .22);
}
.stTextInput input, .stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div,
.stDateInput div[data-baseweb="input"] {
  color: #EAF2FF !important;
  background: #10243A !important;
  border-color: #274461 !important;
  border-radius: 10px !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder { color: #7189A5; }
.stTabs [data-baseweb="tab-list"] {
  gap: 5px;
  border-bottom: 1px solid var(--line);
}
.stTabs [data-baseweb="tab"] {
  padding: 10px 14px;
  color: #8FA6C1;
  background: transparent;
  border-radius: 8px 8px 0 0;
}
.stTabs [aria-selected="true"] {
  color: #66A9FF !important;
  background: rgba(52, 136, 255, .10);
}
.stDataFrame {
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 12px;
}
[data-testid="stExpander"] {
  background: rgba(13, 28, 46, .82);
  border-color: var(--line) !important;
  border-radius: 11px !important;
}
[data-testid="stAlert"] {
  color: #D9E8F7;
  background: #102944;
  border-color: #26517B;
}
hr { border-color: var(--line) !important; }
a { color: #67AAFF !important; }
.planx-brand {
  display: flex;
  align-items: center;
  gap: 11px;
  margin: 6px 0 28px;
  padding: 5px 4px;
}
.planx-brand-mark {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #72B1FF;
  background: linear-gradient(145deg, rgba(52,136,255,.30), rgba(52,136,255,.08));
  border: 1px solid rgba(75,151,255,.32);
  border-radius: 10px;
  font-size: 19px;
  font-weight: 850;
}
.planx-brand-title {
  color: #F1F6FF;
  font-size: 19px;
  line-height: 1.1;
  font-weight: 820;
  letter-spacing: -.03em;
}
.planx-brand-sub {
  margin-top: 3px;
  color: #7790AD;
  font-size: 10px;
}
.planx-hero {
  position: relative;
  padding: 8px 0 18px;
  margin-bottom: 8px;
  background: transparent;
  border: 0;
  box-shadow: none;
}
.planx-eyebrow {
  margin-bottom: 7px;
  color: #5A9FFF;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
}
.planx-hero h1 {
  margin: 0;
  color: #F3F7FF !important;
  font-size: 34px;
  line-height: 1.18;
}
.planx-hero p {
  max-width: 760px;
  margin: 8px 0 0;
  color: #8FA6C1 !important;
  font-size: 15px;
}
.planx-card {
  min-height: 120px;
  padding: 19px 20px;
  background: linear-gradient(145deg, #10243A, #0B1C2E);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 12px 30px rgba(0,0,0,.17);
}
.planx-card-title { margin-bottom: 8px; color: #A5B8CE; font-size: 12px; font-weight: 680; }
.planx-card-value { color: #F1F6FF; font-size: 25px; font-weight: 820; letter-spacing: -.03em; }
.planx-card-note { margin-top: 7px; color: #25D99A; font-size: 12px; }
.planx-empty {
  padding: 22px;
  color: #8FA6C1;
  background: rgba(13, 28, 46, .82);
  border: 1px dashed #2B4868;
  border-radius: 13px;
}
.planx-source {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 8px;
  color: #9AB0C9;
  background: #10243A;
  border: 1px solid #274461;
  border-radius: 999px;
  font-size: 10px;
}
.planx-status-ok { color: #35E0A6; background: rgba(37,217,154,.10); border-color: rgba(37,217,154,.35); }
.planx-status-wait { color: #F5C84C; background: rgba(245,200,76,.10); border-color: rgba(245,200,76,.32); }
.planx-status-bad { color: #FF7585; background: rgba(255,101,119,.10); border-color: rgba(255,101,119,.32); }
@media (max-width: 900px) {
  .block-container { padding: 1.2rem 1rem 3rem; }
  .planx-hero h1 { font-size: 29px; }
  [data-testid="stMetric"] { min-height: 100px; padding: 14px 15px; }
}
@media (max-width: 640px) {
  .planx-hero h1 { font-size: 26px; }
  .planx-card { min-height: 100px; padding: 14px; }
  .planx-card-value { font-size: 22px; }
}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">▥</div>
  <div>
    <div class="planx-brand-title">StockDash</div>
    <div class="planx-brand-sub">Better Investments.</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "PLANX INVESTMENT OS"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#EAF2FF">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
