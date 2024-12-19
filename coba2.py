import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Welcome to Maxim", page_icon="🌟", layout="wide")

# Header dengan Navigasi
st.markdown(
    """
    <style>
        /* Header */
        .header {
            background-color: #000000;
            color: white;
            padding: 15px 0px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 0px;
        }
        /* Navigation */
        .nav {
            display: flex;
            justify-content: center;
            gap: 25px;
            padding: 10px;
            font-size: 18px;
            background-color: #000000;
            color: white;
        }
        .nav a {
            text-decoration: none;
            color: white;
            transition: color 0.3s;
        }
        .nav a:hover {
            color: #00BFFF;
        }
    </style>
    <div class="header">MAXIM</div>
    <div class="nav">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#portfolio">Portfolio</a>
        <a href="#team">Team</a>
        <a href="#contact">Contact</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Bagian Hero Section
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns([3, 2])

with col1:
    st.image("https://via.placeholder.com/800x500", use_column_width=True, caption="Office Setup")

with col2:
    st.markdown(
        """
        <h1 style="color: #444444; font-size: 48px;">Welcome to Maxim</h1>
        <p style="color: #666666; font-size: 20px;">
            We are a team of talented designers making websites with Bootstrap.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.button("GET STARTED", key="get_started")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2024 Maxim. All Rights Reserved.</p>", unsafe_allow_html=True)
