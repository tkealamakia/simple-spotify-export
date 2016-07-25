import requests
import re
import HTMLParser

file = open('spotify.txt', 'r')
target = open('googlePlay.txt', 'w')
html_parser = HTMLParser.HTMLParser()
albumre = re.compile(ur'"name":(["\'])(?:(?=(\\?))\2.)*?\1,"type":"album')
titlere = re.compile(ur'track-name">(.*?)<\/span>')
artistre = re.compile(ur'creator-name">(.*?)<\/span>')

for line in file:
  song = requests.get(line).text
  title = titlere.search(song).group(0)[12:-7]
  artist = artistre.search(song).group(0)[14:-7]
  album = albumre.search(song).group(0)[8:-15]
  line = title + "~" + artist + "~" + album
  line = html_parser.unescape(line)
  line = line.encode('utf-8')
  target.write(line)

target.close()
file.close()
