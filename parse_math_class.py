
import requests
import os
from bs4 import BeautifulSoup


def create_math_directory():
    home_directory = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(home_directory + '/Math391_Notes'):  # if file does not exist then make it
        os.makedirs(home_directory + '/Math391_Notes')

    os.chdir(home_directory + '/Math391_Notes/')
    # return home_directory + '/Math391_Notes'


def parse_pdf():
    url = 'https://sites.google.com/site/summeryunyang/teaching'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    payload = soup.find_all("div", {"class": "sites-attachments-name"})  # cointains all the sites to sites but its mix with html
    pdf_links = []
    pdf_title = []
    for website in payload:
        # if website.a:
            # google_url.append(website.a.get('href'))
        pdf_title.append(website.a.text)

    for link in soup.find_all('a'):
        get_href = link.get('href')
        try:
            if get_href.startswith('/site/summeryunyang/teaching'):
                pdf_links.append(get_href)
        except Exception:
            pass
    url_and_title = list(zip(pdf_links, pdf_title))
    return url_and_title


def download_pdf(parsed_pdf):
    for pdf_file, pdf_title in parsed_pdf:
        pdf_file = 'http://sites.google.com' + pdf_file
        response = requests.get(pdf_file)
        with open(pdf_title, 'wb',) as f:
             # for chunk in response.iter_content(chunk_size=15000):
            f.write(response.content)
        print('downloading {}'.format(pdf_title))
    print('should be done')


def main():
    math_folder = create_math_directory()
    pdf = parse_pdf()
    download_pdf(pdf)


if __name__ == "__main__":
    main()
