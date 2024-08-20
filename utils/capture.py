import cv2
import time
def cam():
    def capture_fresh_frame(camera):
        # Flush the camera buffer by reading multiple frames
        for _ in range(10):
            camera.read()
        
        # Now capture a fresh frame
        ret, frame = camera.read()
        if not ret:
            print("Error: Could not capture a fresh frame.")
            return None
        return frame

    # Initialize the camera
    camera = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not camera.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Capture the first image
    frame1 = capture_fresh_frame(camera)
    if frame1 is None:
        camera.release()
        exit()

    # Save the first image
    cv2.imwrite("image1.jpg", frame1)
    print("First image captured and saved as 'image1.jpg'")

    # Wait for 10 seconds
    print("Waiting for 10 seconds...")
    time.sleep(10)

    # Capture the second image
    frame2 = capture_fresh_frame(camera)
    if frame2 is None:
        camera.release()
        exit()

    # Save the second image
    cv2.imwrite("image2.jpg", frame2)
    print("Second image captured and saved as 'image2.jpg'")

    # Release the camera
    camera.release()

    print("Image capture complete.")