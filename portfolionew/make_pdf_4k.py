import sys
from PIL import Image

def upscale_to_4k(img):
    # Standard 4K width is 3840 pixels
    target_width = 3840
    # Calculate new height to maintain aspect ratio
    w_percent = (target_width / float(img.size[0]))
    target_height = int((float(img.size[1]) * float(w_percent)))
    
    # Resize using high-quality Lanczos filter
    try:
        resample_filter = Image.Resampling.LANCZOS
    except AttributeError:
        resample_filter = Image.LANCZOS # For older versions of PIL
        
    return img.resize((target_width, target_height), resample_filter)

def main():
    image1_path = r"C:\Users\jaswanth.g\.gemini\antigravity\brain\a25db90e-a998-46bf-8004-b4f20d77a23d\media__1773956690425.jpg"
    image2_path = r"C:\Users\jaswanth.g\.gemini\antigravity\brain\a25db90e-a998-46bf-8004-b4f20d77a23d\media__1773956690396.jpg"
    output_pdf_path = r"C:\Users\jaswanth.g\Desktop\portfolionew\JaswanthG_Resume.pdf"
    
    img1 = Image.open(image1_path).convert('RGB')
    img2 = Image.open(image2_path).convert('RGB')
    
    # Upscale to 4K resolution
    img1_4k = upscale_to_4k(img1)
    img2_4k = upscale_to_4k(img2)
    
    # Save as PDF with high resolution (300 DPI)
    img1_4k.save(output_pdf_path, save_all=True, append_images=[img2_4k], resolution=300.0)
    print("Successfully generated 4K PDF!")

if __name__ == "__main__":
    main()
