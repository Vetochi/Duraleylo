import random
import requests
import bs4


def get_cover():
    array_covers = ['https://www.generatormix.com/random-album-generator']
    print(random.choice(array_covers))
    cov = requests.get(random.choice(array_covers))
    print(cov)
    soup = bs4.BeautifulSoup(cov.content, "html.parser")
    result_find = soup.select('#output > div > div.thumbnail-col-3.tile-block-inner.marg-top.first > img')
    result_find_name = soup.select('#output > div > div.thumbnail-col-3.tile-block-inner.marg-top.first > div > h3')[0]
    result_find_artist = soup.select('#output > div > div.thumbnail-col-3.tile-block-inner.marg-top.first > div > p.text-right.pull-right > strong')[0]
    return {
        "artist": result_find_artist.text,
        "name": result_find_name.text,
        "img": result_find[0]['src']
    }