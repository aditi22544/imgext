import cv2
import pytesseract

def preprocess_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Resize the image (optional, but can improve accuracy)
    image = cv2.resize(image, (800, 600))
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Apply noise reduction using Gaussian blur
    blurred_image = cv2.GaussianBlur(binary_image, (3, 3), 0)
    
    # Enhance contrast using histogram equalization
    equalized_image = cv2.equalizeHist(blurred_image)
    return equalized_image

    
 
    
def extract_text(image_path, custom_config):
    preprocessed_image = preprocess_image(image_path)
    extracted_text = pytesseract.image_to_string(preprocessed_image, config=custom_config)
    return extracted_text



