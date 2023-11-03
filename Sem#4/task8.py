# Программа, скачивает страницы из
# списка URL-адресов и сохраняет их в отдельные файлы.

# import threading
# from multiprocessing import Process
import asyncio
import aiohttp

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]

# def url_parse(url):
#     """This func parses an URL into an HTML"""
#     url_src = requests.get(url)
#     html_name = url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#     try:
#         with open(html_name, 'w', encoding='utf-8') as new_html:
#             new_html.write(url_src.text)
#             print(f'Новый документ {html_name} готов!')
#     except Exception as error:
#         print((f'Возникла ошибка {error}! Разбирайся!'))
#
# def thr():
#     """Starts threading"""
#     threads = []
#     for url in urls:
#         thread = threading.Thread(target=url_parse, args=[url, ])
#         threads.append(thread)
#         thread.start()
#     for t in threads:
#         t.join()
#
# thr()

async def url_parse(url):
    """This func parses an URL into an HTML"""
    async with aiohttp.ClientSession() as work:
        async with work.get(url) as session:
            url_src = await session.text()
            html_name = url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            try:
                with open(html_name, 'w', encoding='utf-8') as new_html:
                    new_html.write(url_src)
                    print(f'Новый документ {html_name} готов!')
            except Exception as error:
                print((f'Возникла ошибка {error}! Разбирайся!'))

async def asnco():
    """Starts asyncio"""
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(url_parse(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(asnco)
