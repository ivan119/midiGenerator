import streamlit as st
from trance_generator import TranceGenerator
from ai_music_helper import AIMusicHelper
import os

# Set page config
st.set_page_config(
    page_title="Trance Generator",
    page_icon="🎵",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 10px;
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 15px 32px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    .main {
        background-color: #0E1117;
    }
    .stSelectbox, .stSlider, .stCheckbox {
        background-color: #262730;
    }
    .stMarkdown {
        color: #FAFAFA;
    }
    .stTextArea {
        background-color: #262730;
    }
    .ai-suggestion {
        background-color: #1E1E2E;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎵 Trance Generator")
st.markdown("Generate trance music elements for Ableton Live 12")

# AI Prompt Section
st.subheader("🤖 AI Music Assistant")
st.markdown("""
    Describe the mood or feeling you want in your music. For example:
    - "I want an uplifting, energetic track with a dreamy atmosphere"
    - "Create a dark and mysterious trance with deep bass"
    - "Make a euphoric, classic trance track"
""")

user_description = st.text_area(
    "Your description:",
    height=100
)

if st.button("🎵 Generate from Description"):
    try:
        with st.spinner("Analyzing your description..."):
            ai_helper = AIMusicHelper()
            params = ai_helper.analyze_mood(user_description)
            
            if params:
                # Display AI analysis in a nice format
                st.markdown("### 🎯 AI Analysis")
                st.markdown(f"""
                    <div class="ai-suggestion">
                        <p><strong>Atmosphere:</strong> {params['atmosphere']}</p>
                        <p><strong>Energy Level:</strong> {params['energy_level']}/10</p>
                        <p><strong>Explanation:</strong> {params['explanation']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Update the UI with AI suggestions
                st.session_state.key = params["key"]
                st.session_state.scale = params["scale"]
                st.session_state.bpm = params["bpm"]
                st.session_state.duration = params["duration"]
                st.session_state.lead_style = params["lead_style"]
                st.session_state.pad_style = params["pad_style"]
                st.session_state.bass_style = params["bass_style"]
                st.session_state.drum_style = params["drum_style"]
                
                st.success("🎉 AI has analyzed your description!")
            else:
                st.error("❌ Could not analyze description. Please try again.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Main controls
st.subheader("🎼 Basic Settings")
col1, col2 = st.columns(2)

with col1:
    # Key selection
    key_options = {
        "C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, "F": 65,
        "F#": 66, "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71
    }
    selected_key = st.selectbox("Key", list(key_options.keys()), 
                              index=list(key_options.values()).index(st.session_state.get('key', 60)))
    key = key_options[selected_key]
    
    # Scale selection
    scale = st.selectbox("Scale", ["minor", "major", "harmonic_minor", "phrygian"],
                        index=["minor", "major", "harmonic_minor", "phrygian"].index(st.session_state.get('scale', 'minor')))

with col2:
    # BPM selection
    bpm = st.slider("BPM", min_value=120, max_value=160, 
                   value=st.session_state.get('bpm', 140), step=5)
    
    # Duration selection
    duration = st.slider("Duration (bars)", min_value=4, max_value=32, 
                        value=st.session_state.get('duration', 8), step=4)

# Track selection
st.subheader("🎚️ Tracks")
generate_lead = st.checkbox("Lead", value=True)
generate_pad = st.checkbox("Pad", value=True)
generate_bass = st.checkbox("Bass", value=True)
generate_drums = st.checkbox("Drums", value=True)

# Generate button
if st.button("🎵 Generate MIDI Track"):
    try:
        with st.spinner("Generating..."):
            generator = TranceGenerator(bpm=bpm)
            
            if generate_lead:
                generator.generate_lead(key=key, duration=duration, scale_name=scale)
            if generate_pad:
                generator.generate_pad(key=key, duration=duration, scale_name=scale)
            if generate_bass:
                generator.generate_bassline(key=key-24, duration=duration, scale_name=scale)
            if generate_drums:
                generator.generate_drums(duration=duration)
            
            filename = "trance_track.mid"
            generator.save(filename)
            
            with open(filename, "rb") as file:
                st.download_button(
                    label="📥 Download MIDI File",
                    data=file,
                    file_name=filename,
                    mime="audio/midi"
                )
            
            st.success("🎉 Ready for Ableton Live 12!")
            
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Simple tips
st.markdown("---")
st.markdown("""
    💡 **Quick Tips**
    - Use minor scale for classic trance
    - 140 BPM is traditional trance speed
    - Add effects in Ableton for best results
""") 