from PIL import Image, ImageFilter

def smooth_remove_bg():
    img = Image.open('passports_white.jpg').convert("RGBA")
    mask = Image.new("L", img.size, 0)
    
    pixels = img.load()
    mask_pixels = mask.load()
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            # Stricter threshold
            if r > 180 and g > 180 and b > 180:
                mask_pixels[x, y] = 0
            else:
                mask_pixels[x, y] = 255
                
    # Blur the mask to feather the edges
    mask = mask.filter(ImageFilter.GaussianBlur(radius=2.5))
    
    img.putalpha(mask)
    img.save('passports_transparent.png', 'PNG')

smooth_remove_bg()
print("Saved beautifully feathered transparent PNG")
