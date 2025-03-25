import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

class AIMusicHelper:
    def __init__(self):
        self.api_key = os.getenv('KLUSTER_AI_API_KEY')
        
        # Use the OpenAI client with Kluster AI's base URL
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.kluster.ai/v1"
        )
        
        # Fallback to direct API requests if needed
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.api_url = "https://api.kluster.ai/v1/chat/completions"
        
    def analyze_mood(self, description):
        """Analyze the user's description and return musical parameters."""
        prompt = f"""
        You are an expert trance music producer. Analyze this music description and suggest appropriate musical parameters for trance music:
        "{description}"

        Consider these aspects:
        1. Emotional intensity (affects BPM and energy)
        2. Mood (affects scale and key)
        3. Energy level (affects drum patterns and bass)
        4. Atmosphere (affects pad and lead styles)

        Return a JSON with the following parameters:
        {{
            "key": <MIDI note number 60-71>,
            "scale": <"minor", "major", "harmonic_minor", or "phrygian">,
            "bpm": <120-160>,
            "duration": <4-32>,
            "lead_style": <"melodic", "rhythmic", or "atmospheric">,
            "pad_style": <"warm", "bright", or "dark">,
            "bass_style": <"punchy", "deep", or "melodic">,
            "drum_style": <"energetic", "progressive", or "minimal">,
            "energy_level": <1-10>,
            "atmosphere": <"dreamy", "uplifting", "dark", or "euphoric">,
            "explanation": "<brief explanation of the choices>"
        }}

        Guidelines:
        - For uplifting/energetic moods: Use major scales, higher BPM (145-150)
        - For darker/mysterious moods: Use minor or phrygian scales, lower BPM (130-135)
        - For dreamy/atmospheric: Use harmonic minor, medium BPM (140)
        - For classic trance: Use minor scale, 140 BPM
        """
        
        try:
            # Try first with the OpenAI client
            try:
                completion = self.client.chat.completions.create(
                    model="meta-llama-3-8b-instruct",  # Updated model name
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                
                # Extract the content from the response
                content = completion.choices[0].message.content
                
            except Exception as client_error:
                print(f"OpenAI client error: {str(client_error)}")
                
                # Fall back to direct API request
                data = {
                    "model": "meta-llama-3-8b-instruct",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                response = requests.post(self.api_url, headers=self.headers, json=data)
                response.raise_for_status()
                
                # Parse the API response
                result = response.json()
                content = result.get('choices', [{}])[0].get('message', {}).get('content', '{}')
            
            # Process the content
            try:
                # Try to parse the JSON response
                params = json.loads(content)
            except json.JSONDecodeError:
                # If parsing fails, extract JSON from the response text
                import re
                json_match = re.search(r'({.*})', content, re.DOTALL)
                if json_match:
                    try:
                        params = json.loads(json_match.group(1))
                    except:
                        # If all parsing fails, return default values
                        params = self._get_default_params()
                else:
                    # Default values if JSON can't be found
                    params = self._get_default_params()
            
            return params
            
        except Exception as e:
            print(f"Error in AI analysis: {str(e)}")
            return self._get_default_params()
            
    def _get_default_params(self):
        """Return default parameters for classic trance."""
        return {
            "key": 60,
            "scale": "minor",
            "bpm": 140,
            "duration": 8,
            "lead_style": "melodic",
            "pad_style": "warm",
            "bass_style": "punchy",
            "drum_style": "energetic",
            "energy_level": 7,
            "atmosphere": "uplifting",
            "explanation": "Default parameters for classic trance"
        } 