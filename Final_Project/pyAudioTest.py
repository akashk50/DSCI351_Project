import pyaudio

p = pyaudio.PyAudio()

print("Available devices:\n")
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print(f"{i}. {dev['name']} - Max Input Channels: {dev['maxInputChannels']}")
    if 'defaultSampleRate' in dev:
        print(f"    Default Sample Rate: {dev['defaultSampleRate']}\n")

p.terminate()
