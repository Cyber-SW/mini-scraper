#Mini Scraper - Programmiert von Shawn Wolter

from lxml import html
import requests

run = True
page = requests.get("https://developer.mozilla.org/de/docs/Web/API/Document")
tree = html.fromstring(page.content)

#AUFGABE 1
underlinedWords = tree.xpath(
    '/html/body/div[1]/div//a[@class="page-not-created"]/code/text()')
print("AUFGABE 1:", underlinedWords)

#AUFGABE 2
experimentalWords = tree.xpath(
    '/html/body/div[1]/div//abbr[@class="icon icon-experimental"]/preceding-sibling::a[@class="page-not-created"]/code/text()')
print("AUFGABE 2:", experimentalWords)

#AUFGABE 3
print("Gib eine Zahl zwischen 1 und 8 ein, um eine der vorangegangenen Ausgaben erneut auszugeben.")
while True:
    number = input("Zahl eingeben: ")
    print("AUFGABE 3:", underlinedWords[int(number) - 1])
    if run == False:
        break
