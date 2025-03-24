import streamlit as st
from trance_generator import TranceGenerator
import os

# Set page config
st.set_page_config(
    page_title="Trance Generator",
    page_icon="🎵",
    layout="wide"
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
        padding: 10px 24px;
        border-radius: 5px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    .main {
        background-color: #0E1117;
    }
    .stSelectbox {
        background-color: #262730;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎵 Trance Generator")
st.markdown("""
    Generate trance music elements at 140 BPM. Create lead melodies, pads, basslines, and drum patterns 
    that are typical in trance music. Import the generated MIDI file into Ableton Live 12 for further production.
""")

# Create two columns for controls
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎼 Musical Parameters")
    
    # Key selection
    key_options = {
        "C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, "F": 65,
        "F#": 66, "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71
    }
    selected_key = st.selectbox("Key", list(key_options.keys()))
    key = key_options[selected_key]
    
    # Scale selection
    scale = st.selectbox("Scale", ["minor", "major", "harmonic_minor", "phrygian"])
    
    # Duration selection
    duration = st.slider("Duration (bars)", min_value=4, max_value=32, value=8, step=4)

with col2:
    st.subheader("🎚️ Track Settings")
    
    # Track toggles
    generate_lead = st.checkbox("Generate Lead", value=True)
    generate_pad = st.checkbox("Generate Pad", value=True)
    generate_bass = st.checkbox("Generate Bass", value=True)
    generate_drums = st.checkbox("Generate Drums", value=True)
    
    # BPM selection
    bpm = st.slider("BPM", min_value=120, max_value=160, value=140, step=5)

# Generate button
if st.button("Generate MIDI Track"):
    try:
        # Create generator instance
        generator = TranceGenerator(bpm=bpm)
        
        # Generate selected tracks
        if generate_lead:
            generator.generate_lead(key=key, duration=duration, scale_name=scale)
        if generate_pad:
            generator.generate_pad(key=key, duration=duration, scale_name=scale)
        if generate_bass:
            generator.generate_bassline(key=key-24, duration=duration, scale_name=scale)
        if generate_drums:
            generator.generate_drums(duration=duration)
        
        # Save the file
        filename = "trance_track.mid"
        generator.save(filename)
        
        # Provide download button
        with open(filename, "rb") as file:
            st.download_button(
                label="Download MIDI File",
                data=file,
                file_name=filename,
                mime="audio/midi"
            )
        
        st.success("MIDI track generated successfully! 🎉")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Tips section
st.markdown("---")
st.subheader("💡 Tips for Best Results")
st.markdown("""
1. **VST Instruments**
   - Lead: Use Serum, Sylenth1, or Spire for classic trance leads
   - Pad: Try Omnisphere or Massive for lush pads
   - Bass: Serum or Spire work great for trance basslines
   - Drums: Use a drum rack with high-quality samples

2. **Effects Chain**
   - Lead: Add reverb and delay for space
   - Pad: Use reverb and chorus for movement
   - Bass: Add subtle distortion and compression
   - Sidechain compress pads and leads from the kick

3. **Arrangement Tips**
   - Layer multiple instances for more complex arrangements
   - Use automation for filter sweeps and effects
   - Add risers and impacts for transitions
""") 