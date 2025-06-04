import streamlit as st
import time


def local_css(file_name: str) -> None:
    """Load local CSS file for custom styling."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

st.title("Pomodoro App - Web Version")
st.write("Work in focused bursts with customisable breaks")

work_minutes = st.number_input(
    "Work duration (minutes)", min_value=1, max_value=60, value=25
)
break_minutes = st.number_input(
    "Break duration (minutes)", min_value=1, max_value=30, value=5
)
cycles = st.number_input(
    "Number of cycles", min_value=1, max_value=10, value=1
)

if st.button("Start"):
    for cycle in range(int(cycles)):
        st.subheader(f"\nCycle {cycle + 1} - Work")
        work_seconds = int(work_minutes * 60)
        progress = st.progress(0)
        timer_placeholder = st.empty()
        for remaining in range(work_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_placeholder.header(f"⏳ {mins:02d}:{secs:02d}")
            progress.progress((work_seconds - remaining) / work_seconds)
            time.sleep(1)
        st.success("🔔 Work session complete! Take a break!")

        st.subheader(f"Break {cycle + 1}")
        break_seconds = int(break_minutes * 60)
        progress = st.progress(0)
        timer_placeholder = st.empty()
        for remaining in range(break_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_placeholder.header(f"⏳ {mins:02d}:{secs:02d}")
            progress.progress((break_seconds - remaining) / break_seconds)
            time.sleep(1)
        st.success("⏰ Break is over!")

    st.balloons()
