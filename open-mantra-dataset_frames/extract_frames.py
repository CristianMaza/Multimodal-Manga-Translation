import json
import os
from PIL import Image

# Path to the JSON file
json_file = "annotation.json"

# Load the JSON data
with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)
    
# Iterate over each book in the JSON data
for book in data:
    book_title = book["book_title"]
    
    # Iterate over each page in the book
    for page in book["pages"]:
        image_path = page["image_paths"]["ja"]
        
        # Extract the directory path from the image path
        directory = os.path.dirname(image_path)
        
        # Create the "frames" folder if it doesn't exist
        frames_folder = os.path.join(directory, "frames")
        os.makedirs(frames_folder, exist_ok=True)
        
        # Load the image
        image = Image.open(image_path)
        
        # Iterate over each frame in the page
        for frame_index, frame in enumerate(page["frame"]):
            x, y, w, h = frame["x"], frame["y"], frame["w"], frame["h"]
            
            # Crop the frame from the image
            cropped_frame = image.crop((x, y, x + w, y + h))
            
            # Save the cropped frame
            frame_filename = f"{os.path.splitext(os.path.basename(image_path))[0]}_frame_{frame_index}.jpg"
            frame_path = os.path.join(frames_folder, frame_filename)
            cropped_frame.save(frame_path)
        
        print(f"Processed {image_path}")

print("Frame extraction completed.")