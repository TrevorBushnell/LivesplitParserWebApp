import streamlit as st
import matplotlib.pyplot as plt
from livesplit_parser import LivesplitData
import tempfile

st.title("Livesplit Parser Web App")

st.write("testing all library functions")
my_run = None

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_file_path = tmp_file.name
        
    my_run = LivesplitData(temp_file_path, time_key='RealTime')

    
    # Display the content or process it
# my_run = LivesplitData(uploaded_file, time_key="RealTime")

# st.write(my_run.num_attempts)
# st.write(my_run.platform_name)
# st.write(my_run.attempt_info_df)

if my_run is not None:
    num_reset_tab, completed_runs_v_time_tab, violin_splits_tab, completed_runs_lineplot_tab, completed_run_heatmap_tab = st.tabs(['Number of Resets', 'Completed Runs Over Time', 'Splits in Violin Graph', 'Completed Runs Lineplot', 'Completed Runs Heatmap'])
    with num_reset_tab:
        plt.clf()
        fig = my_run.plot_num_resets()
        st.pyplot(fig)
    with completed_runs_v_time_tab:
        plt.clf()
        fig = my_run.plot_completed_over_time()
        st.pyplot(fig)
    with violin_splits_tab:
        plt.clf()
        fig = my_run.plot_splits_violin_plot()
        st.pyplot(fig)
    with completed_runs_lineplot_tab:
        plt.clf()
        fig = my_run.plot_completed_runs_lineplot()
        st.pyplot(fig)
    with completed_run_heatmap_tab:
        plt.clf()
        fig = my_run.plot_completed_runs_heatmap()
        st.pyplot(fig)