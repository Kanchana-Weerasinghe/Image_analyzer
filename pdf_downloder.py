
import requests


def download_pdf_files():
    download_url = f'https://1drv.ms/b/s!Anl9EgLWFWqQstJA_-Pk-LtDg0KAgw?e=3R8ArZ'
    response = requests.get(download_url)

    if response.status_code == 200:
        # Save the downloaded file
        with open('downloaded_file.pdf', 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully.')
    else:
        print(f'Error downloading file. Status code: {response.status_code}')
        print(response.text)

# %%