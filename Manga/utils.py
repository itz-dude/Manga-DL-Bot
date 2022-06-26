from bs4 import BeautifulSoup
import requests 
import re
from telegraph import Telegraph 
from pykeyboard import InlineKeyboard, InlineButton

def search(query, page=1):  
  try:
    mangalink = f"https://gogomanga.fun/page/{page}/"
    response = requests.get(mangalink, params={"s": query})
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    source_url = soup.find_all('div', attrs={'class': 'bsx'})
    res_search_list = []
    for links in source_url:
      title = links.find('div', attrs={'class': 'tt'}).text.strip()
      mangaId = links.find('a')['href'].split('/')[-2]
      res_search_list.append({
        "title": title,
        "mangaid":mangaId
      })
    return res_search_list
  except requests.exceptions.ConnectionError:
    return "Request Error"



def detail(mangaid):  
  try:
    mangalink = f"https://gogomanga.fun/manga/{mangaid}"
    response = requests.get(mangalink)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    title = soup.title
    imageurl = soup.find('img', class_="attachment- size- wp-post-image")['src']   
    chapters = []
    chap_url = soup.find_all('div', attrs={'class': 'eph-num'})
    chap_url.reverse()
    chapternum = 1
    for chap in chap_url:
      chapter = chap.a.get("href")
      chapters.append({
        "url": chapter.split('/')[-2],
        "num": chapternum
      })
      chapternum = chapternum + 1
    res_search_list = {
        "title":title,
        "imageurl":imageurl,
        "url": mangalink,
        "chapter": chapters
      }
    return res_search_list
  except requests.exceptions.ConnectionError:
    "Check the host's network Connection"


def chapter(mangalink):  
  try:
    response = requests.get(f"https://gogomanga.fun/{mangalink}")
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    imageurl = []
    url = soup.find_all('img', attrs={'class': 'size-full'})
    for x in url:
      imageurl.append(x['src'])
    return imageurl, soup.title
  except requests.exceptions.ConnectionError:
    return "Check the host's network Connection"



def searchkeyboard(res):
  key = InlineKeyboard(row_width=1)
  for x in res[:6]:
    button = InlineButton(
      text=x['title'],
      callback_data=f"mangainfo{x['mangaid']}"
    )
    key.add(button)
  return key



def chapkeyboard(res):
  key = InlineKeyboard(row_width=1)
  re = []
  re.append(res[0])
  re.append(res[-1])
  for x in re:
    if x == re[0]:
      t = "First Chapter" + x['url'].replace("-", " ")
    else:
      t = "Last Chapter" + x['url'].replace("-", " ")
    button = InlineButton(
      text=t,
      callback_data=f"chaptermanga{x['url']}"
    )
    key.add(button)
  return key


def telegra(manga):
  try:
    tel = Telegraph()
    tel.create_account(short_name="TechZ Manga Bot")
    chap, title = chapter(manga)
    f = "<img src='{}'>"
    cont = "<br>".join(f.format(im) for im in chap)
    page = tel.create_page(title=title, html_content=cont)
    return title, page
  except:
    return None