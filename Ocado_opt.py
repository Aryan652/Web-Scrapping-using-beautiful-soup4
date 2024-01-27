from bs4 import BeautifulSoup
import requests
import pandas as pd

def req(url):
    return requests.get(url).text

def pharse(text):
    return BeautifulSoup(text, 'html.parser')

def soup(content, pharse, id = 'default value', func = 'default value'):# soup takes pharsed text first, element to be souped as second and class as third parameters
    if id == 'default value':
        return content.find_all(pharse)
    elif id!= 'default value' and func == 'default value':
        return content.find_all(pharse, class_=id )
    else:   # Use of func in this means if you want to just run find tag you can send any random text at last as string and program will run the find command
        return content.find(pharse, class_ = id )

# the below def takes wither only url or element also. If only url then value stored
## in form of string use soup def later, or using url with element then value is stored in form of array.

def scrap(url, elem ='default value', id = 'default value', func = 'default value'): 
    page = req(url)
    content = pharse(page)
    if elem=='default value' and id=='default value':

        return content
    elif id=='default value' and func == 'default value':
        return soup(content,elem)
    elif id!= 'default value' and func == 'default value':
        return soup(content, elem, id)
    else:
        return soup(content, elem, id, func)

# Note: after using decode func you must use soup def for collecting array
## This func return value in string format
def decode(content):
    section = content.decode_contents()
    return section

url = 'https://www.ocado.com/browse'

items = scrap(url, 'a', 'level-item-link')
i=0
j = 0
for item in items:
    url2 = 'https://www.ocado.com'+item.get('href')
    print( )
    print(i, item.text, ' : ',url2)
    i+=1

    ## FOR GETTING INFORMATION FOR SUB DIRECTOTRIES
    
    section = scrap(url2, 'ul', 'fops fops-regular fops-shelf', 'find') # this is array
    section2 = scrap(url2) # this is pharsed html
    decoded_section = decode(section)
    
    li_soups = soup(section2, 'li', 'fops-item fops-item--on_offer')
    for li in li_soups:
        a_soup = soup(li,'a')
        url3_arry=[] #### not in proper use right now
        h4_soup = soup(li, 'h4','fop-title')
        for a, h4 in zip(a_soup, h4_soup):
            addr = 'https://www.ocado.com'+ a.get('href')
            url3_arry.append(addr) #### this is not in proper use

            name =  h4.text
            print(' ')
            print(f'{name} : {addr}')
            
            try:
                table = scrap(addr, 'table', 'default value', 'find') # the table is extracted in same loop.
                df = pd.read_html(str(table))[0]
                df.to_excel(f'table{j}.xlsx', index = False)
                j += 1
            except:
                print('no table present')

        ### FOR GETTING TABLE FROM THE 3RD SUB DIRECTORIES.


print('looping ends now')
    