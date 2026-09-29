import numpy as np
import scipy.io.wavfile as wavfile
import subprocess

sample_rate = 44100
total_duration = 32.0  # 32 seconds
total_samples = int(sample_rate * total_duration)

bpm = 75
beat_sec = 60.0 / bpm
step_sec = beat_sec / 2.0  # 8th notes

t = np.linspace(0, total_duration, total_samples, endpoint=False)

# Chords (Lofi Jazzy progression: Dmaj7 -> Bm7 -> Em7 -> A7)
# Frequencies
chords = [
    [146.83, 220.00, 277.18, 369.99],  # D3, A3, C#4, F#4 (Dmaj7)
    [123.47, 185.00, 220.00, 293.66],  # B2, F#3, A3, D4 (Bm7)
    [164.81, 246.94, 329.63, 392.00],  # E3, B3, E4, G4 (Em7)
    [110.00, 164.81, 220.00, 277.18],  # A2, E3, A3, C#4 (A7)
]

audio = np.zeros(total_samples, dtype=np.float32)

# 1. Warm electric piano pad chords
chord_duration = beat_sec * 4  # 1 measure per chord
for i, sample_idx in enumerate(range(0, total_samples, int(chord_duration * sample_rate))):
    chord = chords[(i) % len(chords)]
    dur_samples = min(int(chord_duration * sample_rate), total_samples - sample_idx)
    t_chunk = np.linspace(0, dur_samples / sample_rate, dur_samples, endpoint=False)
    
    # Envelope
    env = np.exp(-t_chunk * 0.4) * (1.0 - np.exp(-t_chunk * 30.0))
    chord_wave = np.zeros(dur_samples)
    for freq in chord:
        # warm sine with soft second harmonic
        tone = np.sin(2 * np.pi * freq * t_chunk) + 0.3 * np.sin(2 * np.pi * freq * 2 * t_chunk)
        chord_wave += tone * 0.25
    audio[sample_idx:sample_idx + dur_samples] += (chord_wave * env * 0.22).astype(np.float32)

# 2. Chill lofi hip-hop drum beat (Kick on 1 & 3.5, Snare on 2 & 4, subtle hi-hats)
step_samples = int(step_sec * sample_rate)
for step in range(int(total_duration / step_sec)):
    pos = step * step_samples
    if pos >= total_samples:
        break
    beat_in_bar = (step % 8)
    
    # Kick on 0 and 5
    if beat_in_bar in [0, 5]:
        k_dur = int(0.25 * sample_rate)
        if pos + k_dur < total_samples:
            t_k = np.linspace(0, 0.25, k_dur, endpoint=False)
            freq_k = 120.0 * np.exp(-t_k * 25.0) + 40.0
            phase_k = 2 * np.pi * np.cumsum(freq_k) / sample_rate
            kick = np.sin(phase_k) * np.exp(-t_k * 12.0) * 0.35
            audio[pos:pos + k_dur] += kick.astype(np.float32)

    # Soft Snare / Rimshot on 2 and 6
    if beat_in_bar in [2, 6]:
        s_dur = int(0.18 * sample_rate)
        if pos + s_dur < total_samples:
            t_s = np.linspace(0, 0.18, s_dur, endpoint=False)
            noise = (np.random.rand(s_dur) * 2 - 1) * np.exp(-t_s * 25.0) * 0.18
            body = np.sin(2 * np.pi * 180 * t_s) * np.exp(-t_s * 35.0) * 0.2
            snare = noise + body
            audio[pos:pos + s_dur] += snare.astype(np.float32)

    # Hi-hat on every 8th note with swing volume
    h_dur = int(0.06 * sample_rate)
    if pos + h_dur < total_samples:
        t_h = np.linspace(0, 0.06, h_dur, endpoint=False)
        hat = (np.random.rand(h_dur) * 2 - 1) * np.exp(-t_h * 75.0) * (0.05 if beat_in_bar % 2 == 0 else 0.035)
        audio[pos:pos + h_dur] += hat.astype(np.float32)

# 3. Subtle vinyl crackle / warmth
crackle = (np.random.rand(total_samples) * 2 - 1) * 0.008
# gentle pop spikes
pops = np.random.choice([0, 1], size=total_samples, p=[0.9997, 0.0003]) * (np.random.rand(total_samples) * 0.04)
audio += (crackle + pops).astype(np.float32)

# Master normalize & soft clip
max_val = np.max(np.abs(audio))
if max_val > 0:
    audio = audio / max_val * 0.88

int16_audio = (audio * 32767).astype(np.int16)
wavfile.write("/config/Desktop/BuildWithGemini/demo_recording/lofi_beat.wav", sample_rate, int16_audio)
print("lofi_beat.wav generated successfully!")
