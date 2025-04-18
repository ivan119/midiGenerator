# Trance Generator v0.1

A powerful MIDI generator for creating trance music elements, featuring an AI-powered assistant that helps translate your musical ideas into MIDI patterns. Uses Kluster AI's Meta-Llama-3.1-8B model for intelligent music parameter suggestions.

## Features

- 🤖 AI Music Assistant that analyzes your descriptions and suggests musical parameters
- 🎵 Generate MIDI patterns for:
  - Lead melodies
  - Pad sounds
  - Basslines
  - Drum patterns
- 🎼 Customizable parameters:
  - Key and scale selection
  - BPM control (120-160)
  - Duration settings
  - Track selection
- 🎚️ MIDI output compatible with Ableton Live 12
- 🧠 Powered by Kluster AI's Meta-Llama-3.1-8B model

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trance-generator.git
cd trance-generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Kluster AI API key:
```
KLUSTER_AI_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to http://localhost:8501

3. Use the AI Assistant to describe your desired mood, or manually adjust the parameters

4. Generate and download MIDI files for use in Ableton Live 12

## Project Structure

```
trance-generator/
├── app.py              # Main Streamlit application
├── trance_generator.py # MIDI generation logic
├── ai_music_helper.py  # AI integration with Kluster AI
├── requirements.txt    # Project dependencies
└── .env               # Environment variables (create this)
```

## Requirements

- Python 3.8+
- Kluster AI API key
- Dependencies listed in requirements.txt

## License

MIT License - see LICENSE file for details

## Version History

- v0.1 (2025-03-25)
  - Initial release
  - Basic MIDI generation
  - AI-powered parameter suggestions using Kluster AI
  - Streamlit interface

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
3. Layer multiple instances of the generator for more complex arrangements