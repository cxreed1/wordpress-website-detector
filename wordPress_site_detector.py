import csv
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# File Select
def selectFile():
    Tk().withdraw()
    filename = askopenfilename(title='Select URL txt file',filetypes=(('text files', '*.txt'),))
    print(f"Filename: {filename} Selected")
    return filename


# Extract all urls
def getUrls():
    filename = selectFile()
    with open(filename) as file:
        rows_n = file.readlines()
        rows = [line.replace('\n', '') for line in rows_n if len(line)>0]
        print(f"Total of {len(rows)} Url detected!")
        return rows

# Write File
def writeFile(url, status):
    with open('wordPress_site_detector.txt', 'a') as file:
        file.write(f"{url} \t {status}\n")


# wordPress_site_detector Function
def wpDetect(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10).text
        if "wp-content" in response:
            writeFile(url, '[OK]')
            print(f"{url} [OK] This is a Wordpress website")
        else:
            writeFile(url, '[NotWP]')
            print(f"{url} [NotWP] This is not a Wordpress website")
    except:
        writeFile(url, 'ERROR')
        print(f"{url}  Connection Error")

def main():
    urls = getUrls()
    for link in urls:
        wpDetect(link)


if __name__ == "__main__":
    main()
    print('completed')
    input()
