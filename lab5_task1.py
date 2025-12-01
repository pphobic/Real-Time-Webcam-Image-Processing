import cv2
import numpy as np

def main():
    # Create a window to display the video
    cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)

    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Initial mode
    mode = 'o'
    sigma = 3

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (0, 0), sigma)

        output_frame = None

        if mode == 'o':
            output_frame = frame
        elif mode == 'x':
            # Sobel gradient in x-direction
            sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            output_frame = cv2.convertScaleAbs(sobel_x)
        elif mode == 'y':
            # Sobel gradient in y-direction
            sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
            output_frame = cv2.convertScaleAbs(sobel_y)
        elif mode == 'm':
            # Magnitude of Sobel gradient
            sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
            magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
            output_frame = cv2.convertScaleAbs(magnitude)
        elif mode == 's':
            # Sobel + thresholding
            sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
            magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
            _, thresholded = cv2.threshold(cv2.convertScaleAbs(magnitude), 100, 255, cv2.THRESH_BINARY)
            output_frame = thresholded
        elif mode == 'l':
            # Laplacian of Gaussian (LoG)
            log = cv2.Laplacian(blurred, cv2.CV_64F, ksize=3)
            output_frame = cv2.convertScaleAbs(log)

        # Display the output frame
        if output_frame is not None:
            cv2.imshow('Webcam', output_frame)

        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('o'):
            mode = 'o'
        elif key == ord('x'):
            mode = 'x'
        elif key == ord('y'):
            mode = 'y'
        elif key == ord('m'):
            mode = 'm'
        elif key == ord('s'):
            mode = 's'
        elif key == ord('l'):
            mode = 'l'
        elif key == ord('+'):
            sigma += 1
            print(f"Sigma increased to: {sigma}")
        elif key == ord('-'):
            sigma = max(1, sigma - 1)
            print(f"Sigma decreased to: {sigma}")


    # Release the webcam and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
