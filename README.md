# Image Downloader 
This script reads a CSV file containing a list of image URLs and attempts to download each image from those URLs. The images are stored in a local directory called "image". If any image URLs fail to download, the row number and URL are written to a file called "error_log.txt" and added to a list of skipped URLs. At the end of the script, if there were any skipped URLs, it will print a message indicating which rows they were on.

## Requirements
- Python 3
- `csv` module
- `os` module
- `requests` module

## Usage

To use the script, place it in the same directory as the CSV file and run it using Python 3. The CSV file should have a column called "image_url" containing the URLs of the images to be downloaded. The script will also use an optional "image_name" column to set the file name of the downloaded images. If the "image_name" column is not present or is empty, the original file name and extension will be used.

The script will create a "image" directory to store the downloaded images, if it doesn't already exist. If any image URLs fail to download, the row number and URL will be written to a "error_log.txt" file, and a message indicating which rows the skipped URLs were on will be printed at the end of the script.

**Command:**
```commandline
python downloadIMGbyCSV.py
```

### Example
- You can refer to the attached links.csv file for an example of the format of the CSV file.

Given the following CSV file:
```
image_url,image_name
https://example.com/image1.jpg,image_name1
https://example.com/image2.jpg,
https://example.com/image3.jpg,image_name3
```
Running the script will result in the following:

- The image at `https://example.com/image1.jpg` will be downloaded and saved to the "image" directory as "image_name1.jpg".
- The image at `https://example.com/image2.jpg` will be downloaded and saved to the "image" directory as "image2.jpg".
- The image at `https://example.com/image3.jpg` will be downloaded and saved to the "image" directory as "image_name3.jpg".