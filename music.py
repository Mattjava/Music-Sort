import numpy as np
import simpleaudio as sa
import time

base = 440

max_num = 0

def find_max(arr: list[int]):
    global max_num
    max_num= arr[0]
    
    for num in arr:
        max_num = max(max_num, num)
    max_num = max_num + 1
    print(max_num)

note_dict = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G'
}

freq_map = {
    'A': base,
    'B': base * 2 ** (2 / 12),
    'C': base * 2 ** (3 / 12),
    'D': base * 2 ** (5 / 12),
    'E': base * 2 ** (7 / 12),
    'F': base * 2 ** (8 / 12),
    'G': base * 2 ** (10 / 12)
}

sample_rate = 44100
T = 1
t = np.linspace(0, T, int(T * sample_rate), False)

def play_array(arr: list[int]):
    processed_arr = [num * 7 // max_num for num in arr]
    note_arr = [note_dict[num % 7] for num in processed_arr]
    freq_arr = [freq_map[note] for note in note_arr]

    stack = [np.sin(freq * t * 2 * np.pi) for freq in freq_arr]

    audio = np.hstack(tup=tuple(stack))

    audio *= 32767 / np.max(np.abs(audio))

    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    
    print(arr)

    play_obj.wait_done()
    
    time.sleep(0.5)
