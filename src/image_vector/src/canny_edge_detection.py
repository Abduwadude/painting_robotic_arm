#!/usr/bin/env python3
import cv2
import os

def canny_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    return edges

def save_images(original, edges, output_folder='output'):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Save the original image
    original_path = os.path.join(output_folder, 'original_photo.jpg')
    cv2.imwrite(original_path, original)
    print(f"Original photo saved: {original_path}")

    # Save the edge-detected image
    edges_path = os.path.join(output_folder, 'edge_detected_photo.jpg')
    cv2.imwrite(edges_path, edges)
    print(f"Edge-detected photo saved: {edges_path}")

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Original', frame)

        # Check for the 'Enter' key press
        key = cv2.waitKey(1) & 0xFF
        if key == 13:  # ASCII code for Enter key
            # Apply Canny edge detection
            edges = canny_edge_detection(frame)

            # Display the edges
            cv2.imshow('Canny Edge Detection', edges)

            # Save the original and edge-detected images
            save_images(frame, edges)

        # Check for the 'Esc' key press to exit the loop
        elif key == 27:
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

