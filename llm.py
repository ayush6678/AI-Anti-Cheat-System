import streamlit as st
import subprocess
from PIL import Image
from utils.groq1 import llamaAPPS
from utils.groq2 import llamaUSB
from utils.groq3 import llamaBLUE
from utils.groq4 import llamaSOUND
from utils.groq5 import llamaCAM
from utils.groq6 import llamaEXT
from utils.groq7 import llamaRESULT
from utils.google import count_chrome_tabs
from utils.processes import list_unique_active_processes_with_network_interface
from utils.usb import get_device_names
from utils.bluetooth import check_bluetooth_status
from utils.face_check import compare_images
from utils.capture import cam
from utils.extentions import get_chrome_extensions

st.title("Human-Less Proctoring System")

def clear_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')

def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)


if st.button("Check System compatibility"):
    clear_file("result.txt")
    #Apps check
    st.info("Applications Check")
    apps=[count_chrome_tabs(),list_unique_active_processes_with_network_interface()]
    st.write(apps[0])
    st.write("Apps running on your system:")
    for i in apps[1]:
        st.write(i)
    op1=llamaAPPS(apps[0],apps[1])
    st.write(op1)
    append_to_file("result.txt", op1)

    #Devices check
    st.info("Devices Check")
    devices=get_device_names()
    st.write("The following devices are connected to your USB ports:")
    for dev in devices["USB"]:
        st.write(dev)
    st.write("The following HDMI devices are connected:")
    for dev in devices["HDMI"]:
        st.write(dev)
    op2=llamaUSB(devices)
    st.write(op2)
    append_to_file("result.txt", op2)

    #Bluetooth Check
    st.info("Bluetooth Check")
    bluetooth=check_bluetooth_status()
    st.write(bluetooth)
    op3=llamaBLUE(bluetooth)
    st.write(op3)
    append_to_file("result.txt", op3)

    #Sound Check
    st.info("Sound Check...")
    subprocess.run(['python3', 'utils/speech.py'], capture_output=True, text=True)
    sound_info=""
    with open("volume_output.txt","r") as f:
        sound_info=f.read()
    st.text(sound_info)
    op4=llamaSOUND(sound_info)
    st.write(op4)
    append_to_file("result.txt", op4)

    #Camera Check
    st.info("Camera Check")
    st.write("Capturing images")
    cam()

    image_path1 = "image1.jpg"
    image_path2 = "image2.jpg"

    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)


    output=compare_images(image_path1,image_path2)
    similarity=output[0]
    ppl1=output[1]
    ppl2=output[2]

    st.image(img1, caption='Uploaded Image 1', use_column_width=True)
    st.write("Number of people: "+str(ppl1))
    st.image(img2, caption='Uploaded Image 2', use_column_width=True)
    st.write("Number of people: "+str(ppl2))
    st.write("Similarity Score: "+ str(similarity*100))

    op5=llamaCAM(similarity,ppl1,ppl2)
    st.write(op5)
    append_to_file("result.txt", op5)

    #Extentions Check
    st.info("Extentions Check")
    extentions=get_chrome_extensions()
    st.write("The following extentions are installed on your browser:")
    for ext in extentions:
        st.write(ext["name"])
    op6=llamaEXT(extentions)
    st.write(op6)
    append_to_file("result.txt", op6)

    with open("result.txt","r") as f:
        st.info("Analyzing Results:")
        st.write(llamaRESULT(f.read()))
