from PIL import Image, ImageDraw, ImageFont
import os

# Create assets folder if it doesn't exist
os.makedirs("assets", exist_ok=True)

CELL = 20  # image size

# --- Apple (Red circle with green leaf) ---
img = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.ellipse([2, 4, CELL-2, CELL-1], fill="red")           # apple body
draw.rectangle([9, 0, 11, 5], fill="green")                  # stem
img.save("assets/apple.png")
print("✅ apple.png created")

# --- Snake Head (Bright green with eyes) ---
img = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rectangle([1, 1, CELL-2, CELL-2], fill=(0, 200, 0))    # green head
draw.ellipse([4, 4, 8, 8], fill="white")                     # left eye
draw.ellipse([12, 4, 16, 8], fill="white")                   # right eye
draw.ellipse([5, 5, 7, 7], fill="black")                     # left pupil
draw.ellipse([13, 5, 15, 7], fill="black")                   # right pupil
img.save("assets/snake_head.png")
print("✅ snake_head.png created")

# --- Snake Body (Darker green) ---
img = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rectangle([1, 1, CELL-2, CELL-2], fill=(0, 150, 0))    # dark green body
img.save("assets/snake_body.png")
print("✅ snake_body.png created")

print("\n🎉 All assets created in /assets folder!")