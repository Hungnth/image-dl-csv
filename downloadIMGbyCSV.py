import csv
import os
import requests

# Create the "image" directory if it doesn't already exist
if not os.path.exists("image"):
    os.makedirs("image")

# Initialize an empty list to store the row numbers of any URLs that couldn't be downloaded
skipped_urls = []

# Open the CSV file and create a reader object
with open("links.csv", "r") as csv_file:
    # Read the first line of the CSV file (the column names)
    column_names = next(csv_file).strip().split(",")
    # Create a DictReader object using the column names as field names
    reader = csv.DictReader(csv_file, fieldnames=column_names)
    # Count the number of rows in the CSV file
    num_rows = sum(1 for row in reader)
    # Reset the file pointer to the beginning of the file
    csv_file.seek(0)
    # Skip the first row (the column names)
    next(reader)
    # Open a file to store the URLs that couldn't be downloaded
    with open("error_log.txt", "w") as log_file:
        # Iterate over the rows of the CSV file
        for i, row in enumerate(reader):
            # Get the URL of the image
            url = row["image_url"]
            # Make a GET request to the URL
            response = requests.get(url)
            # If the request was not successful, write the row number and URL to the log file
            # and add the row number to the list of skipped URLs
            if not response.ok:
                log_file.write(f"{i + 1}, {url}\n")
                print(f"Error: Could not download image from URL {url}")
                skipped_urls.append(i + 1)
                continue
            # Extract the original file name and extension from the URL
            file_name, file_ext = os.path.splitext(url.split("/")[-1])
            # If the CSV file has an "image_name" column, use it to set the file name
            # otherwise, use the original file name
            if "image_name" in row:
                if row["image_name"]:
                    file_name = row["image_name"]
            else:
                file_name = file_name
            # Append the file extension to the file name
            file_name += file_ext
            # Write the image data to a file in the "image" directory
            with open(os.path.join("image", file_name), "wb") as f:
                f.write(response.content)
            # Print a progress message
            print(f"Downloaded image {i + 1} of {num_rows}: {file_name}")

# If there were any URLs that couldn't be downloaded, print a message indicating which rows they were on
if len(skipped_urls) > 0:
    print(f"Skipped URLs at row(s): {', '.join(str(i) for i in skipped_urls)}")
