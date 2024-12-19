import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SkinRenew",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Create a navigation bar
selected = option_menu(
    menu_title=None,  # No title
    options=["Home", "DetAcne", "About", "Contact"],  # Menu options
    icons=["house", "camera", "file", "phone"],  # Icons for menu items
    menu_icon="cast",  # Menu icon
    default_index=0,  # Default selected item
    orientation="horizontal",  # Horizontal menu
)


# Display content based on selected menu
if selected == "Home":
    # Header Section
    st.title("Welcome to My Awesome App!")
    st.subheader("Your tagline goes here 🚀")
    st.write("This is the main landing page.")
    
    # Bagian Hero Section
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])

    with col1:
        st.image("https://via.placeholder.com/800x500", caption="Office Setup")

    with col2:
        st.markdown(
            """
            <h1 style="color: #444444; font-size: 48px;">Welcome to SkinRenew</h1>
            <p style="color: #666666; font-size: 20px;">
                We are a team of talented designers making websites with Bootstrap.
            </p>
            """,
            unsafe_allow_html=True,
        )
        st.button("GET STARTED", key="get_started")
    
    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align:center;'>© 2024 SkinRenew. All Rights Reserved.</p>", unsafe_allow_html=True)
    
elif selected == "DetAcne":
    st.title("Welcome to Page 1")
    st.write("Here is the content of Page 1.")
elif selected == "About":
    st.title("Welcome to Page 2")
    st.write("Here is the content of Page 2.")
    
    # Image Section
    st.image(
        "https://via.placeholder.com/800x400.png?text=Landing+Page+Image",
        caption="Your amazing product or app",
    )
elif selected == "Contact":
    st.title("Welcome to Page 2")
    st.write("Here is the content of Page 2.")