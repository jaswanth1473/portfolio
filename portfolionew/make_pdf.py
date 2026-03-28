import subprocess
import sys

def create_pdf():
    try:
        import PIL
    except ImportError:
        print("Installing Pillow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        
    from PIL import Image

    image1_path = r"C:\Users\jaswanth.g\.gemini\antigravity\brain\a25db90e-a998-46bf-8004-b4f20d77a23d\media__1773955933130.jpg"
    image2_path = r"C:\Users\jaswanth.g\.gemini\antigravity\brain\a25db90e-a998-46bf-8004-b4f20d77a23d\media__1773956164929.jpg"
    output_pdf_path = r"C:\Users\jaswanth.g\Desktop\portfolionew\JaswanthG_Resume.pdf"

    print("Opening images...")
    image1 = Image.open(image1_path).convert('RGB')
    image2 = Image.open(image2_path).convert('RGB')

    print("Saving to PDF...")
    image1.save(output_pdf_path, save_all=True, append_images=[image2])
    print("Successfully generated PDF!")

if __name__ == "__main__":
    create_pdf()
