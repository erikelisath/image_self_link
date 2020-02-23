"""
Pelican plugin: image_self_link
===============================

Transforms images into self-connections. This allows to open images in their
original size. Links are opened in a new browser tab.

"""

from pelican import signals

from bs4 import BeautifulSoup

def test(sender):
    print(f'{sender} initialized')

def add_image_link(sender):
    if sender._content is not None:
        if '<img' in sender._content:
            print(f'Article found with <img> tag: "{sender.title}"')
            content = BeautifulSoup(sender._content, 'html.parser')

            for img in content.find_all('img'):
                if 'a' not in img.parent.name:
                    link = content.new_tag('a', href=img['src'], target='_blank')
                    img.wrap(link)
                    print(f'\033[FArticle found with <img> tag: "{sender.title}" - touched')

            sender._content = str(content)


def register():
    signals.content_object_init.connect(add_image_link)
