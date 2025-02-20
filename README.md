# Web Scraper for Bollards and Utility Poles

This Python script scrapes images of bollards and utility poles from [GeoHints](https://geohints.com). The images are downloaded and saved with appropriate titles extracted from the webpage. I used it to create a Quizlet Set

## Features
- Extracts images from pages containing bollard and utility pole data.
- Saves images with meaningful filenames based on the country name found in the `<span>` tag.
- Handles duplicate titles by numbering them accordingly.
- Organizes images into separate directories for bollards and utility poles.

## Requirements

Ensure you have Python 3 installed along with the following dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script with:

```bash
python scraper.py
```

The script will automatically scrape the pages:
- `https://geohints.com/meta/bollards`
- `https://geohints.com/meta/utilityPoles`

### Output
- **Bollards images** will be saved in the `bollard_images/` directory.
- **Utility poles images** will be saved in the `pole_images/` directory.

## Code Structure

- `fetch_html(url)`: Fetches the webpage content.
- `parse_images(html, base_url)`: Extracts image URLs and assigns filenames.
- `download_images(images, output_folder)`: Downloads images to the specified folder.
- `scrape_and_download(url, output_folder)`: Orchestrates the full scraping and downloading process.

# Quizlet CSV Generator
The Script `quizlet_csv_generator` generates CSV files for Quizlet from images stored in a given folder. Each image filename (without extension and count) is used as the answer, and the image itself is referenced in the CSV. The output can be imported directly into Quizlet to create flashcard sets with images on the front and names on the back.

Usage
Place your images in a folder.
Update the script with the correct folder paths.
Run the script, and it will generate a CSV file with the format:
mathematica
Kopieren
Bearbeiten
Image, Answer
example.jpg, example
Import the generated CSV file into Quizlet.
Requirements
Python 3.x
No external dependencies (uses built-in os and csv modules)

## License
This project is open-source and available under the MIT License.


