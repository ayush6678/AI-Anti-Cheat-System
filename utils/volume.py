import pulsectl

def get_current_volume():
    with pulsectl.Pulse('volume-getter') as pulse:
        sink_inputs = pulse.sink_input_list()
        if sink_inputs:
            sink_input = sink_inputs[0]
            volume = sink_input.volume.value_flat
            return volume
        else:
            print("No sink inputs found. Using default volume level.")
            return 0.5  # Default volume level if no sink inputs are found

if __name__ == "__main__":
    volume_level = get_current_volume()
    print(f"Current volume level: {volume_level * 100:.2f}%")