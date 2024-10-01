from scipy.io import wavfile
import numpy as np


class SoundWaveFactory:
    _SAMPLING_RATE = 44100
    _DURATION_SECONDS = 5
    _SOUND_ARRAY_LEN = _SAMPLING_RATE * _DURATION_SECONDS
    _MAX_AMPLITUDE = 2 ** 13
    _NOTES = {
        '0': 0, 'e0': 20.60172, 'f0': 21.82676, 'f#0': 23.12465, 'g0': 24.49971, 'g#0': 25.95654, 'a0': 27.50000,
        'a#0': 29.13524,
        'b0': 30.86771, 'c0': 32.70320, 'c#0': 34.64783, 'd0': 36.70810, 'd#0': 38.89087,
        'e1': 41.20344, 'f1': 43.65353, 'f#1': 46.24930, 'g1': 48.99943, 'g#1': 51.91309, 'a1': 55.00000,
        'a#1': 58.27047,
        'b1': 61.73541, 'c1': 65.40639, 'c#1': 69.29566, 'd1': 73.41619, 'd#1': 77.78175,
        'e2': 82.40689, 'f2': 87.30706, 'f#2': 92.49861, 'g2': 97.99886, 'g#2': 103.8262, 'a2': 110.0000,
        'a#2': 116.5409,
        'b2': 123.4708, 'c2': 130.8128, 'c#2': 138.5913, 'd2': 146.8324, 'd#2': 155.5635,
        'e3': 164.8138, 'f3': 174.6141, 'f#3': 184.9972, 'g3': 195.9977, 'g#3': 207.6523, 'a3': 220.0000,
        'a#3': 233.0819,
        'b3': 246.9417, 'c3': 261.6256, 'c#3': 277.1826, 'd3': 293.6648, 'd#3': 311.1270,
        'e4': 329.6276, 'f4': 349.2282, 'f#4': 369.9944, 'g4': 391.9954, 'g#4': 415.3047, 'a4': 440.0000,
        'a#4': 466.1638,
        'b4': 493.8833, 'c4': 523.2511, 'c#4': 554.3653, 'd4': 587.3295, 'd#4': 622.2540,
        'e5': 659.2551, 'f5': 698.4565, 'f#5': 739.9888, 'g5': 783.9909, 'g#5': 830.6094, 'a5': 880.0000,
        'a#5': 932.3275,
        'b5': 987.7666, 'c5': 1046.502, 'c#5': 1108.731, 'd5': 1174.659, 'd#5': 1244.508,
        'e6': 1318.510, 'f6': 1396.913, 'f#6': 1479.978, 'g6': 1567.982, 'g#6': 1661.219, 'a6': 1760.000,
        'a#6': 1864.655,
        'b6': 1975.533, 'c6': 2093.005, 'c#6': 2217.461, 'd6': 2349.318, 'd#6': 2489.016,
        'e7': 2637.020, 'f7': 2793.826, 'f#7': 2959.955, 'g7': 3135.963, 'g#7': 3322.438, 'a7': 3520.000,
        'a#7': 3729.310,
        'b7': 3951.066, 'c7': 4186.009, 'c#7': 4434.922, 'd7': 4698.636, 'd#7': 4978.032,
    }

    def get_normed_sin(self, timeline, frequency):
        return self._MAX_AMPLITUDE * np.sin(2 * np.pi * frequency * timeline)

    def get_soundwave(self, timeline, note):
        return self.get_normed_sin(timeline, self._NOTES[note])

    def common_timeline(self):
        return np.linspace(0, self._DURATION_SECONDS, num=self._SOUND_ARRAY_LEN)

    def create_note(self, note="a4", name=None, timeline=None):
        if not timeline:
            timeline = self.common_timeline()

        sound_wave = self.get_soundwave(timeline, note).astype(np.int16)
        if name is None:
            file_name = f"{note}_sin.wav".replace("#", "s")
        else:
            file_name = f"{name}.wav"
        wavfile.write(file_name, self._SAMPLING_RATE, sound_wave)
        return sound_wave

    def read_waves(self, path):
        try:
            waves = wavfile.read(path)
            waves_data = waves[1]
            return waves_data
        except FileNotFoundError:
            print(f"{path} does not exist!")

    def get_waves_information(self, waves_dataset):
        sampling_rate = self._SAMPLING_RATE
        wave_length = len(waves_dataset)
        duration = wave_length / sampling_rate

        min_amplitude = np.min(waves_dataset)
        max_amplitude = np.max(waves_dataset)
        mean_amplitude = np.mean(waves_dataset)
        peak_to_peak_amp = max_amplitude - min_amplitude

        return dict({
            'sampling_rate': f"{sampling_rate / 1000} KHz",
            'wave_length': wave_length,
            'duration': duration,
            'min_amplitude': min_amplitude,
            'max_amplitude': max_amplitude,
            'mean_amplitude': mean_amplitude,
            'peak_to_peak_amplitude': peak_to_peak_amp
        })


if __name__ == '__main__':
    swf = SoundWaveFactory()
    swf.create_note('a4')
    swf.create_note('a1')
    swf.create_note('d7')
    waves_data_a4 = swf.read_waves('a4_sin.wav')
    waves_data_a1 = swf.read_waves('a4_sin.wav')
    waves_data_d7 = swf.read_waves('a4_sin.wav')

    waves_information = swf.get_waves_information(waves_data_a4)
    print(waves_information)
