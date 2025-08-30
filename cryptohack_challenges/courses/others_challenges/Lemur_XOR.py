import sys
from PIL import Image
import numpy as np

img1, img2, out = sys.argv[1], sys.argv[2], sys.argv[3]

im1 = Image.open(img1).convert("RGBA")
im2 = Image.open(img2).convert("RGBA").resize(im1.size)

# Conversion en tableaux NumPy (octets 8 bits)
a1, a2 = np.array(im1, np.uint8), np.array(im2, np.uint8)

rgb_xor = np.bitwise_xor(a1[..., :3], a2[..., :3])
alpha = a1[..., 3]

# Reconstruction de l'image (RVB + alpha) et sauvegarde
out_img = np.dstack([rgb_xor, alpha]).astype(np.uint8)
Image.fromarray(out_img, "RGBA").save(out)

print(f"XOR termine {out}")
