from selenium import webdriver
import time
from soundcloud_downloader import SoundCloudDownloader

# 1) get urls
# 2) download files
# 3) ???
# 4) add tags
# 5) profit


def download_file(url):
    """
    Downloads soundcloud track given url
    :param url: url of soundcloud track
    :return:
    """
    sc_downloader = SoundCloudDownloader()
    sc_downloader.download(url)


def get_playlist_urls(url, driver):
    """
    Get playlist urls
    :param url: Url of soundcloud playlist
    :param driver: webdriver instance
    :return: List of soundcloud track urls
    """

    driver.get(url)

    old_height = 0
    height = driver.find_element_by_tag_name('body').size['height']

    urls = []

    while height > old_height:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        old_height = height
        height = driver.find_element_by_tag_name('body').size['height']

    for el in [driver.find_elements_by_class_name('trackItem__trackTitle')[0]]:
        urls.append(el.get_attribute('href'))

    return urls


def main():
    driver = webdriver.Chrome()
    urls = get_playlist_urls(
        'https://soundcloud.com/royaltyfreemusic-nocopyrightmusic/sets/creative-commons-music', driver)
    for url in urls:
        download_file(url)


if __name__ == '__main__':
    main()
