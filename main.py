import cv2
import os

STORAGE_DIR = "data"

def preprocess(image):
    # stub for input preprocessing
    pass

def detect(image):
    # stub for model detection
    preprocess(image)
    pass

def store(image):
    if not os.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR, exist_ok=True)
    # stub for storage to data
    pass

if __name__ == "__main__":
  
    # define a video capture object
    vid = cv2.VideoCapture(0)
    
    while(True):
        ret, frame = vid.read()
        if ret:
            status, img = detect(frame)
            if status:
                store(img)
                
        # the 'q' button is set as the quitting button.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()