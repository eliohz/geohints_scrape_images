import os
import csv
import re

def generate_quizlet_csv(folder_path, output_csv):
    """
    Creates a CSV file for Quizlet with image names as answers.
    The images are taken from the specified folder.
    """
    entries = []
    
    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            # Remove the file extension
            name_without_ext = os.path.splitext(filename)[0]
            # Remove numbers from the filename
            name_without_numbers = re.sub(r'\d+', '', name_without_ext).strip()
            entries.append([filename, name_without_numbers])
    
    # Save as CSV
    with open(output_csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Image", "Answer"])
        writer.writerows(entries)
    
    print(f"CSV file created: {output_csv}")

if __name__ == "__main__":
    # Example: Create CSVs for two folders
    folder1 = "path/to/folder1"  # Replace with actual path
    folder2 = "path/to/folder2"  # Replace with actual path
    
    generate_quizlet_csv(folder1, "quizlet_1.csv")
    generate_quizlet_csv(folder2, "quizlet_2.csv")
