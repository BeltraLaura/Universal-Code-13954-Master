import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_transformation_suite(input_path):
    # Load the source image representing UC 13954
    img = cv2.imread(input_path)
    if img is None:
        return "Error: Image not found."
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img_rgb.shape

    # --- 1. MIRROR TRANSFORMATION (Symmetry Math) ---
    # Reflection across the 'Spine' vertical axis
    mirrored = cv2.flip(img_rgb, 1)

    # --- 2. ANAGLYPH 3D (Parallax Math) ---
    # Shifting the Red channel by d pixels to simulate depth perception
    d = 15 
    anaglyph = img_rgb.copy()
    anaglyph[:, :-d, 0] = img_rgb[:, d:, 0]  # Red shift
    # G and B channels remain at original coordinates

    # --- 3. TOPOGRAPHIC 3D SURFACE (Luminance Mapping) ---
    # Treating intensity as the Z-axis (Mathematical Foundations)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scale = 0.1 # Downsample for computational efficiency
    small_gray = cv2.resize(gray, (0,0), fx=scale, fy=scale)
    
    y_range, x_range = small_gray.shape
    X, Y = np.meshgrid(np.arange(x_range), np.arange(y_range))
    Z = small_gray

    # --- COMBINING INTO ONE OUTPUT CANVAS ---
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('Mathematical Transformations: UC 13954 Framework', fontsize=16)

    # Subplot 1: Mirrored
    ax1 = fig.add_subplot(131)
    ax1.imshow(mirrored)
    ax1.set_title("1. Bilateral Symmetry (Mirror)")
    ax1.axis('off')

    # Subplot 2: Anaglyph
    ax2 = fig.add_subplot(132)
    ax2.imshow(anaglyph)
    ax2.set_title("2. Parallax Depth (Anaglyph)")
    ax2.axis('off')

    # Subplot 3: Topography
    ax3 = fig.add_subplot(133, projection='3d')
    surf = ax3.plot_surface(X, Y, Z, cmap='viridis', antialiased=True)
    ax3.set_title("3. Intensity Topography (Z-Axis)")
    ax3.view_init(elev=30, azim=225)

    plt.tight_layout()
    plt.savefig('combined_transformations.png', dpi=300)
    plt.show()

# Execution
generate_transformation_suite('1000017056.jpg')
