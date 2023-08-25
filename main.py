import pytesseract
from textextraction import extract_text

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    image_path = 'download.png'
    

    custom_config = r"--oem 3 --psm 11 -c tessedit_char_whitelist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz., ' -c preserve_interword_spaces=1"
    
    # Extract text using the module's function
    extracted_text = extract_text(image_path, custom_config)

    # Remove line breaks and extra spaces
    extracted_text = ' '.join(extracted_text.split())
    

    print(extracted_text)

