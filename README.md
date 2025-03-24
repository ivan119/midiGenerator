# Trance Generator

A powerful MIDI generator for creating trance music elements at 140 BPM. This tool generates lead melodies, pads, basslines, and drum patterns that are typical in trance music.

## Features

- Generates complete trance tracks with:
  - Lead melodies with variations
  - Evolving pad sounds with chord progressions
  - Driving basslines
  - Standard trance drum patterns
- Supports multiple scales:
  - Minor
  - Major
  - Harmonic Minor
  - Phrygian
- Includes common trance chord progressions
- Adjustable BPM (default 140)
- MIDI file output compatible with Ableton Live 12
- User-friendly web interface

## Installation

1. Make sure you have Python 3.8 or higher installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface (Recommended)

1. Start the web interface:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Use the interface to:
   - Select the key and scale
   - Choose which tracks to generate
   - Adjust the duration and BPM
   - Generate and download the MIDI file

### Command Line

Alternatively, you can run the generator directly from the command line:
```bash
python trance_generator.py
```

This will generate a MIDI file named `trance_track.mid` with the following tracks:
- Track 1: Lead melody
- Track 2: Pad chords
- Track 3: Bassline
- Track 4: Drums

## Importing to Ableton Live 12

1. Open Ableton Live 12
2. Drag and drop the generated `trance_track.mid` file into your project
3. Each track will be imported as a separate MIDI track
4. Assign your preferred VST instruments to each track:
   - Lead: Lead synth (e.g., Serum, Sylenth1)
   - Pad: Pad synth (e.g., Omnisphere, Massive)
   - Bass: Bass synth (e.g., Serum, Spire)
   - Drums: Drum rack or sampler

## Customization

You can modify the following parameters in the code:
- Key (default: 60 - Middle C)
- Duration (default: 4 bars)
- Scale (default: minor)
- BPM (default: 140)

## Tips for Best Results

1. Use high-quality VST instruments for the best sound
2. Add effects typical to trance:
   - Reverb on leads and pads
   - Delay on leads
   - Sidechain compression on pads and leads from the kick
   - EQ to carve out space for each element
3. Layer multiple instances of the generator for more complex arrangements #   m i d i G e n e r a t o r  
 