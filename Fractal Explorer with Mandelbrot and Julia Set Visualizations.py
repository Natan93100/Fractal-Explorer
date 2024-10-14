import numpy as np
import matplotlib.pyplot as plt

#FractalMath Module (Calculates Fractals)

class FractalMath:
    def __init__(self, max_iter=1000, threshold=2):
        self.max_iter = max_iter
        self.threshold = threshold

    def mandelbrot(self, c):
        """Calculate the escape time for Mandelbrot set."""
        z = 0
        n = 0
        while abs(z) <= self.threshold and n < self.max_iter:
            z = z*z + c
            n += 1
        return n

    def julia(self, z, c):
        """Calculate the escape time for Julia set."""
        n = 0
        while abs(z) <= self.threshold and n < self.max_iter:
            z = z*z + c
            n += 1
        return n

#FractalVisualization Module (Plots Fractals)

class FractalVisualization:
    def __init__(self, width=800, height=800, xlim=(-2, 2), ylim=(-2, 2)):
        self.width = width
        self.height = height
        self.xlim = xlim
        self.ylim = ylim
        self.fractal_math = FractalMath()

    def generate_mandelbrot(self):
        """Generate the Mandelbrot set image."""
        image = np.zeros((self.height, self.width))
        for x in range(self.width):
            for y in range(self.height):
                # Map pixel position to complex plane
                real = self.xlim[0] + (x / self.width) * (self.xlim[1] - self.xlim[0])
                imag = self.ylim[0] + (y / self.height) * (self.ylim[1] - self.ylim[0])
                c = complex(real, imag)
                image[y, x] = self.fractal_math.mandelbrot(c)
        return image

    def generate_julia(self, c):
        """Generate the Julia set image for a fixed complex number c."""
        image = np.zeros((self.height, self.width))
        for x in range(self.width):
            for y in range(self.height):
                # Map pixel position to complex plane
                real = self.xlim[0] + (x / self.width) * (self.xlim[1] - self.xlim[0])
                imag = self.ylim[0] + (y / self.height) * (self.ylim[1] - self.ylim[0])
                z = complex(real, imag)
                image[y, x] = self.fractal_math.julia(z, c)
        return image

    def plot_fractal(self, image, title="Fractal", cmap='inferno'):
        """Plot the fractal image."""
        plt.imshow(image, cmap=cmap, extent=(self.xlim[0], self.xlim[1], self.ylim[0], self.ylim[1]))
        plt.colorbar()
        plt.title(title)
        plt.show()
#FractalAnalysis Module (Performs Statistical Analysis)

class FractalAnalysis:
    def __init__(self, image):
        self.image = image

    def average_escape_time(self):
        """Calculate the average escape time of the fractal image."""
        return np.mean(self.image)

    def max_escape_time(self):
        """Find the maximum escape time in the image."""
        return np.max(self.image)

    def summary(self):
        print(f"Average escape time: {self.average_escape_time()} iterations")
        print(f"Maximum escape time: {self.max_escape_time()} iterations")

#Main Application (User Interaction and Fractal Exploration)

def main():
    print("Welcome to the Fractal Explorer!")

    # User chooses fractal type
    fractal_type = input("Choose fractal (Mandelbrot/Julia): ").lower()

    # Initialize visualization
    visualization = FractalVisualization()

    if fractal_type == "mandelbrot":
        print("Generating Mandelbrot set...")
        mandelbrot_image = visualization.generate_mandelbrot()
        visualization.plot_fractal(mandelbrot_image, title="Mandelbrot Set")

        # Analysis
        analysis = FractalAnalysis(mandelbrot_image)
        analysis.summary()

    elif fractal_type == "julia":
        real = float(input("Enter the real part of the constant c: "))
        imag = float(input("Enter the imaginary part of the constant c: "))
        c = complex(real, imag)
        print(f"Generating Julia set for c = {c}...")
        julia_image = visualization.generate_julia(c)
        visualization.plot_fractal(julia_image, title=f"Julia Set for c = {c}")

        # Analysis
        analysis = FractalAnalysis(julia_image)
        analysis.summary()

    else:
        print("Unknown fractal type. Please choose Mandelbrot or Julia.")


if __name__ == "__main__":
    main()
