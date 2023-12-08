

#----------------------------------------------# Goal #----------------------------------------------#
# Build a game based around contract bridge safety plays using the listed example on bridgehands.com #
#----------------------------------------------------------------------------------------------------#


import urllib.request
import codecs
from bs4 import BeautifulSoup


htmls = []

for hcp in range(1,10):
    url = f'https://www.bridgehands.com/S/Suit_Combination_{hcp}.htm'
    
    fp = urllib.request.urlopen(url=url)
    mybytes = fp.readlines()

    output = ""

    for line in mybytes:
        decoded = codecs.decode(line, "ISO-8859-1")
        output += decoded

    fp.close()

    htmls.append(output)

counter = 0
hands = []

for i in range(len(htmls)):
    document = BeautifulSoup(htmls[i], 'html.parser')
    temp = document.find_all('tr')
    temp2 = []  ## temp2 will be a list of all the hands of HCP i to be used
    for item in temp:
        if item.td.contents == "&nbsp;":
            continue
        try:
            a = int(item.td.b.contents[0])
        except:
            continue

        temp2.append(item)

    counter += len(temp2)
    hands += temp2
    print(f'{i+1} HCP held by opps: ',len(temp2))

print(counter)
print(hands)