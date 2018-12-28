import requests
from urllib.parse import urljoin, urlparse, urlencode
from lxml import html

addr = "2945 Irvington Rd, Falls Church, VA, 22042-1607"
'''
https://www.google.com/search?q=2945+Irvington+Rd%2C+Falls+Church%2C+VA%2C+22042-1607&oq=2945+Irvington+Rd%2C+Falls+Church%2C+VA%2C+22042-1607&aqs=chrome..69i57j69i60l2.766j0j7&sourceid=chrome&ie=UTF-8
'''

url = f"https://www.google.com/search?q={addr}"
print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
r = requests.get(url=url, headers=headers)

tree = html.fromstring(r.text)

streetview_url = urljoin('https://www.google.com/search', tree.xpath('//div[@class="dirs"]/div[2]/a/img/@src')[0])
print(streetview_url)

raw_roadmap = tree.xpath('//div[@class="dirs"]/div[3]/a/div[1]/@style')[0]
print(raw_roadmap)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
r = requests.get(url=streetview_url, headers = headers, stream=True)

save_file_name = '1.png'
with open(save_file_name, "wb") as png:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            png.write(chunk)
