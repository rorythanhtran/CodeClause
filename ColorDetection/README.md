
## **About the Python Project**

This project creates a Python-based application that allows users to detect the name of a color by clicking on it in an image. The application works as follows:

1. **Dataset:** The project uses a dataset (`colors.csv`) containing 865 color names, along with their RGB and hex values.
2. **Color Matching:** The program calculates the distance between the clicked color's RGB values and the dataset values, selecting the closest match.
3. **Interactive Interface:** Users can load an image, click on any pixel, and instantly see the name of the corresponding color.

---

## **The Dataset**

- **Source:** [Colors Dataset](https://github.com/codebrainz/color-names/blob/master/output/colors.csv)
- **Details:**
  - Includes 865 colors.
  - Covers a wide range of RGB and hex values to provide accurate results.
---

## **Libraries uesed**

The following Python libraries are installed:
- **OpenCV:** For image processing.
- **Pandas:** For working with the dataset.
- **NumPy:** For efficient numeric computations.
- **Argparse:** For handling command-line arguments.

