import requests

cookies = {
    '__utmz': '29880764.1705426011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'PHPSESSID': '7512064085c0d2b8c7fc4f3cef630c3e',
    '__utma': '29880764.1875279189.1705426011.1709387820.1709394531.6',
    '__utmc': '29880764',
    '__utmt': '1',
    'books': '7512064085c0d2b8c7fc4f3cef630c3e',
    '__utmb': '29880764.9.10.1709394531',
}

headers = {
    'authority': 'rirabook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '__utmz=29880764.1705426011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=7512064085c0d2b8c7fc4f3cef630c3e; __utma=29880764.1875279189.1705426011.1709387820.1709394531.6; __utmc=29880764; __utmt=1; books=7512064085c0d2b8c7fc4f3cef630c3e; __utmb=29880764.9.10.1709394531',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

for i in range(99999999):
    params = {
        'addcart': str(f'{i}-50'),
    }

    response = requests.get('https://rirabook.com/process.php', params=params, cookies=cookies, headers=headers)

    print(response, i)