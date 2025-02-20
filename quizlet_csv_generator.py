import os
import csv
import re
import argparse

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
    parser = argparse.ArgumentParser(description="Generate a Quizlet CSV file from images.")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing images")
    
    args = parser.parse_args()
    
    # Generate output file name based on folder name
    folder_name = os.path.basename(args.folder_path)
    output_csv = os.path.join(args.folder_path, f"{folder_name}.csv")
    
    generate_quizlet_csv(args.folder_path, output_csv)
