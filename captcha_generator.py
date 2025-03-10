from captcha.image import ImageCaptcha
import random
import string

def generate_captcha(text_length=6, save_path='captcha.png'):
    # Ensure at least one letter and one number
    letters = random.choices(string.ascii_letters, k=text_length - 1)
    digit = random.choice(string.digits)
    captcha_text = ''.join(letters) + digit
    
    # Shuffle the characters to randomize the order
    captcha_text = ''.join(random.sample(captcha_text, len(captcha_text)))
    
    # Create an image captcha
    image_captcha = ImageCaptcha(width=280, height=90)
    image = image_captcha.generate_image(captcha_text)
    
    # Save the image
    image.save(save_path)
    
    print(f'CAPTCHA generated: {captcha_text}')
    print(f'Saved as: {save_path}')

if __name__ == '__main__':
    generate_captcha()

# Let me know if you’d like any more improvements! 🚀
