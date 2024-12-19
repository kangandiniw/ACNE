import os
import streamlit as st


model_path = "model/acne_nonacne/model.savedmodel"
if os.path.exists(model_path):
    st.success(f"Model directory exists at: {model_path}")
else:
    st.error(f"Model directory does not exist: {model_path}")

saved_model_file = os.path.join(model_path, "saved_model.pb")
if os.path.exists(saved_model_file):
    st.success(f"SavedModel file exists at: {saved_model_file}")
else:
    st.error(f"SavedModel file not found: {saved_model_file}")
