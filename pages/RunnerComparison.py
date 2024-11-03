import streamlit as st
import matplotlib.pyplot as plt
from livesplit_parser import LivesplitData
from livesplit_parser import RunnerData
import tempfile


runner_dict = RunnerData({})

uploaded_files = st.file_uploader(
    "Upload LLS files", accept_multiple_files=True
)
count = 1
for uploaded_file in uploaded_files:
    my_run = None
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_file_path = tmp_file.name
        
        my_run = LivesplitData(temp_file_path, time_key='RealTime')
    runner_dict.add_runner_data("runner"+str(count), my_run)