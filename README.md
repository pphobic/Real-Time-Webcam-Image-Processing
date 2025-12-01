# Real-time Webcam Gradient and Edge Detection

This project is a Python application that captures video from a webcam and applies various real-time gradient and edge detection operations to the video stream.

## Features

*   **Real-time Video Processing:** Applies image processing effects to a live webcam feed.
*   **Multiple Effects:** Supports several gradient and edge detection techniques:
    *   Original webcam feed
    *   Sobel gradient in the x-direction
    *   Sobel gradient in the y-direction
    *   Magnitude of the Sobel gradient
    *   Sobel with thresholding for edge detection
    *   Laplacian of Gaussian (LoG) edge detection
*   **Adjustable Smoothing:** Allows for real-time adjustment of the Gaussian blur smoothing parameter.

## Requirements

To run the Python script, you will need to have the following installed:

*   Python 3.8+
*   OpenCV (`opencv-python`)
*   NumPy

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file containing `opencv-python` and `numpy`)*

## Usage

To run the application, execute the following command in your terminal:

```bash
python lab5_task1.py
```

A window will open displaying the webcam feed.

## Controls

The application uses the following keys to control the displayed video effect:

*   **`o`**: Show the original webcam frame.
*   **`x`**: Show the Sobel gradient in the x-direction.
*   **`y`**: Show the Sobel gradient in the y-direction.
*   **`m`**: Show the magnitude of the Sobel gradient.
*   **`s`**: Show the result of Sobel with thresholding.
*   **`l`**: Apply the Laplacian of Gaussian (LoG) edge detector.
*   **`+`**: Increase the smoothing parameter (sigma).
*   **`-`**: Decrease the smoothing parameter (sigma).
*   **`q`**: Quit the program.

## Executable

This repository also includes a pre-compiled executable file, `mini_project.exe`, located in the `dist` directory. This allows you to run the application on Windows without needing to have Python or any dependencies installed.

To use the executable, simply navigate to the `dist` directory and run the `mini_project.exe` file.
