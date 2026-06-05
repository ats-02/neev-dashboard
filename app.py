import streamlit as st
import base64
import os

# Global configuration - must be called FIRST and ONLY here
st.set_page_config(
    page_title="UNO MINDA HPDC Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# LOCAL LOGO ENCODER PIPELINE
# ---------------------------------------------------------
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    # Fallback placeholder if the image file is missing from data/ directory
    return "https://placehold.co"

# Fetch local image string safely
logo_base64 = get_base64_image("data/logo.png")

# ---------------------------------------------------------
# UNO MINDA CORPORATE THEME STYLING (Premium CSS Architecture)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Global Background and Typography */
    .stApp {
        background-color: #fcfdfe;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Executive Brand Header Header Box */
    .brand-container {
        background: linear-gradient(135deg, #0A2540 0%, #0056B3 100%);
        padding: 2rem 2.5rem;
        border-radius: 8px;
        color: white;
        margin-bottom: 2.5rem;
        box-shadow: 0 4px 12px rgba(10, 37, 64, 0.08);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .text-pane {
        flex-grow: 1;
    }
    .logo-pane img {
        max-height: 55px;
        background-color: rgba(255, 255, 255, 0.95);
        padding: 8px 14px;
        border-radius: 6px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    .brand-title {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin: 0 !important;
        padding-bottom: 0.25rem;
        color: #ffffff !important;
    }
    .brand-subtitle {
        font-size: 1.05rem !important;
        opacity: 0.85;
        font-weight: 400;
        margin: 0 !important;
        letter-spacing: 0.5px;
        color: #ffffff !important;
    }
    
    /* Section Indicators */
    .section-header {
        color: #0A2540;
        border-left: 4px solid #0056B3;
        padding-left: 14px;
        margin-top: 2rem;
        margin-bottom: 1.25rem;
        font-weight: 600;
        font-size: 1.3rem;
    }
    
    /* Technical Grid Cards */
    .feature-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        border-top: 3px solid #0056B3;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        height: 100%;
    }
    .feature-title {
        color: #0A2540;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    .feature-desc {
        color: #4a5568;
        font-size: 0.875rem;
        line-height: 1.5;
    }
    
    /* Sidebar Overrides for Corporate Presentation */
    section[data-testid="stSidebar"] {
        background-color: #0A2540 !important;
    }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] p {
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] .st-emotion-cache-16296g2 {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# EXECUTIVE HEADER HERO BANNER WITH BRAND LOGO EMBED
# ---------------------------------------------------------
st.markdown(f"""
    <div class="brand-container">
        <div class="text-pane">
            <h1 class="brand-title">UNO MINDA DIGITAL FACTORY</h1>
            <p class="brand-subtitle">Enterprise IoT Manufacturing Intelligence & Process Control Platform</p>
        </div>
        <div class="logo-pane">
            <img src="{logo_base64}" alt="Uno Minda Logo">
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PROJECT MISSION STATEMENT
# ---------------------------------------------------------
st.markdown('<div class="section-header">NEEV Project Initiative</div>', unsafe_allow_html=True)
st.markdown("""
Design & Implementation of an **In-House High-Density IoT Architecture** 
tailored explicitly for real-time edge telemetry tracking across Injection Moulding 
and High-Pressure Die Casting (HPDC) machinery complexes.
""")

st.divider()

# ---------------------------------------------------------
# TECHNICAL PLATFORM FEATURE CARDS GRID
# ---------------------------------------------------------
st.markdown('<div class="section-header">Core Operational Modules</div>', unsafe_allow_html=True)

# 3-Column dynamic card grid deployment
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Real-Time Monitoring</div>
            <div class="feature-desc">Continuous high-frequency edge data pipelines processing cycle parameters instantly.</div>
        </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Golden Zone Analytics</div>
            <div class="feature-desc">Statistical process validation comparing tool telemetry against precise engineering limits.</div>
        </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-title">AI Root Cause Detection</div>
            <div class="feature-desc">Automated physics-based diagnostic matrix identifying gas porosity and short fill risks.</div>
        </div>
    """, unsafe_allow_html=True)

# Space buffer row
st.write("")

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Predictive Maintenance</div>
            <div class="feature-desc">Plunger system tool wear curves tracking remaining operational lifespans safely.</div>
        </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Factory Copilot</div>
            <div class="feature-desc">Natural language engine querying active machinery logs and standard operating procedures (SOPs).</div>
        </div>
    """, unsafe_allow_html=True)

with row2_col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Management Impact</div>
            <div class="feature-desc">Enterprise OEE metrics, green energy savings matrices, and 3-phase digital twin tracking.</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# NAVIGATION FOOTER
# ---------------------------------------------------------
st.info("System Ready. Please select an operational module from the sidebar navigation menu to load specific telemetry views.")
