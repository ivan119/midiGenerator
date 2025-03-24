from midiutil import MIDIFile
import numpy as np
from typing import List, Tuple
import random

class TranceGenerator:
    def __init__(self, bpm: int = 140):
        self.bpm = bpm
        self.midi = MIDIFile(4)  # 4 tracks: lead, pad, bass, drums
        self.midi.addTempo(0, 0, self.bpm)
        
        # Define scales
        self.scales = {
            'minor': [0, 2, 3, 5, 7, 8, 10],  # Natural minor
            'major': [0, 2, 4, 5, 7, 9, 11],  # Major
            'harmonic_minor': [0, 2, 3, 5, 7, 8, 11],  # Harmonic minor
            'phrygian': [0, 1, 3, 5, 7, 8, 10],  # Phrygian (common in trance)
        }
        
        # Common trance chord progressions (in roman numerals)
        self.chord_progressions = [
            ['i', 'vi', 'III', 'VII'],  # Classic trance progression
            ['i', 'VII', 'VI', 'VII'],  # Uplifting trance
            ['i', 'III', 'VII', 'VI'],  # Progressive trance
        ]

    def get_scale_notes(self, root_note: int, scale_name: str) -> List[int]:
        """Generate notes in the specified scale."""
        scale = self.scales[scale_name]
        return [root_note + interval for interval in scale]

    def generate_lead(self, key: int = 60, duration: int = 4, scale_name: str = 'minor') -> None:
        """Generate a trance lead pattern with variations."""
        track = 0
        channel = 0
        time = 0
        base_volume = 100
        
        scale_notes = self.get_scale_notes(key, scale_name)
        
        # Lead patterns (in sixteenth notes)
        patterns = [
            [1, 0, 1, 0, 1, 0, 1, 0],  # Straight pattern
            [1, 0, 0, 1, 1, 0, 0, 1],  # Syncopated
            [1, 1, 0, 0, 1, 1, 0, 0],  # Double notes
        ]
        
        for bar in range(duration):
            pattern = random.choice(patterns)
            for step in range(len(pattern)):
                if pattern[step]:
                    note = random.choice(scale_notes)
                    # Add some velocity variation
                    velocity = base_volume + random.randint(-10, 10)
                    self.midi.addNote(track, channel, note, time, 0.25, velocity)
                time += 0.25

    def generate_pad(self, key: int = 60, duration: int = 4, scale_name: str = 'minor') -> None:
        """Generate evolving pad sounds."""
        track = 1
        channel = 1
        time = 0
        base_volume = 80
        
        scale_notes = self.get_scale_notes(key, scale_name)
        
        # Generate chord progression
        progression = random.choice(self.chord_progressions)
        
        for bar in range(duration):
            chord_idx = bar % len(progression)
            chord_degree = progression[chord_idx]
            
            # Convert roman numeral to actual notes
            if chord_degree == 'i':
                chord = [scale_notes[0], scale_notes[2], scale_notes[4]]
            elif chord_degree == 'III':
                chord = [scale_notes[2], scale_notes[4], scale_notes[6]]
            elif chord_degree == 'VI':
                chord = [scale_notes[5], scale_notes[0], scale_notes[2]]
            elif chord_degree == 'VII':
                chord = [scale_notes[6], scale_notes[1], scale_notes[3]]
            
            # Add chord with slight velocity variation
            for note in chord:
                velocity = base_volume + random.randint(-5, 5)
                self.midi.addNote(track, channel, note, time, 4, velocity)
            time += 4

    def generate_bassline(self, key: int = 36, duration: int = 4, scale_name: str = 'minor') -> None:
        """Generate a driving trance bassline."""
        track = 2
        channel = 2
        time = 0
        base_volume = 110
        
        scale_notes = self.get_scale_notes(key, scale_name)
        
        # Bassline patterns
        patterns = [
            [1, 0, 1, 0, 1, 0, 1, 0],  # Straight
            [1, 0, 0, 1, 1, 0, 0, 1],  # Syncopated
            [1, 1, 0, 0, 1, 1, 0, 0],  # Double notes
        ]
        
        for bar in range(duration):
            pattern = random.choice(patterns)
            for step in range(len(pattern)):
                if pattern[step]:
                    # Use root note and fifth for bass
                    note = random.choice([scale_notes[0], scale_notes[4]])
                    velocity = base_volume + random.randint(-5, 5)
                    self.midi.addNote(track, channel, note, time, 0.25, velocity)
                time += 0.25

    def generate_drums(self, duration: int = 4) -> None:
        """Generate basic trance drum pattern."""
        track = 3
        channel = 9  # MIDI channel 10 (0-based) for drums
        time = 0
        
        # Drum notes (GM standard)
        kick = 36
        snare = 38
        hihat = 42
        clap = 39
        
        # Basic trance drum pattern
        kick_pattern = [1, 0, 0, 0, 1, 0, 0, 0]  # Kick on 1 and 5
        snare_pattern = [0, 0, 1, 0, 0, 0, 1, 0]  # Snare on 3 and 7
        hihat_pattern = [1, 1, 1, 1, 1, 1, 1, 1]  # Continuous hihat
        
        for bar in range(duration):
            for step in range(8):
                if kick_pattern[step]:
                    self.midi.addNote(track, channel, kick, time, 0.25, 100)
                if snare_pattern[step]:
                    self.midi.addNote(track, channel, snare, time, 0.25, 90)
                if hihat_pattern[step]:
                    self.midi.addNote(track, channel, hihat, time, 0.25, 80)
                time += 0.25

    def generate_full_track(self, key: int = 60, duration: int = 4, scale_name: str = 'minor') -> None:
        """Generate a complete trance track with all elements."""
        self.generate_lead(key, duration, scale_name)
        self.generate_pad(key, duration, scale_name)
        self.generate_bassline(key - 24, duration, scale_name)  # One octave lower
        self.generate_drums(duration)

    def save(self, filename: str = "trance_pattern.mid") -> None:
        """Save the MIDI file."""
        with open(filename, "wb") as output_file:
            self.midi.writeFile(output_file)

def main():
    # Example usage
    generator = TranceGenerator(bpm=140)
    
    # Generate a track in A minor (key 57)
    generator.generate_full_track(key=57, duration=8, scale_name='minor')
    
    # Save the MIDI file
    generator.save("trance_track.mid")
    print("Generated trance track saved as 'trance_track.mid'")

if __name__ == "__main__":
    main() 