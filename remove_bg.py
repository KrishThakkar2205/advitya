import sys
from PIL import Image

def remove_white_bg(input_path, output_path, threshold=220):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Check if the pixel is close to white
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Replace with transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(output_path, "PNG")

remove_white_bg("passports_white.jpg", "passports_transparent.png", threshold=210)
print("Saved passports_transparent.png")
