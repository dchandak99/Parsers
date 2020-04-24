from bs4 import BeautifulSoup


tei_doc = 'sample.tei.xml'
with open(tei_doc, 'r') as tei:
    soup = BeautifulSoup(tei, 'lxml')


soup.title


soup.title.getText()


soup.abstract


soup.abstract.getText(separator=' ', strip=True)


abstract_text = soup.abstract.getText(separator=' ', strip=True)
'movement' in abstract_text.lower(), 'ecology' in abstract_text.lower(), 'computer' in abstract_text.lower()




def read_tei(tei_file):
    with open(tei_file, 'r') as tei:
        soup = BeautifulSoup(tei, 'lxml')
        return soup
    raise RuntimeError('Cannot generate a soup from the input')



def elem_to_text(elem, default=''):
    if elem:
        return elem.getText()
    else:
        return default



# +
from dataclasses import dataclass

@dataclass
class Person:
    firstname: str
    middlename: str
    surname: str

turing_author = Person(firstname='Alan', middlename='M', surname='Turing')

f"{turing_author.firstname} {turing_author.surname} authored many influential publications in computer science."

# -





class TEIFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.soup = read_tei(filename)
        self._text = None
        self._title = ''
        self._abstract = ''

    @property
    def doi(self):
        idno_elem = self.soup.find('idno', type='DOI')
        if not idno_elem:
            return ''
        else:
            return idno_elem.getText()

    @property
    def title(self):
        if not self._title:
            self._title = self.soup.title.getText()
        return self._title

    @property
    def abstract(self):
        if not self._abstract:
            abstract = self.soup.abstract.getText(separator=' ', strip=True)
            self._abstract = abstract
        return self._abstract

    @property
    def authors(self):
        authors_in_header = self.soup.analytic.find_all('author')

        result = []
        for author in authors_in_header:
            persname = author.persname
            if not persname:
                continue
            firstname = elem_to_text(persname.find("forename", type="first"))
            middlename = elem_to_text(persname.find("forename", type="middle"))
            surname = elem_to_text(persname.surname)
            person = Person(firstname, middlename, surname)
            result.append(person)
        return result
    
    @property
    def text(self):
        divs_text = []
        if not self._text:
            
            for div in self.soup.body.find_all("div")[1:]:
                # div is neither an appendix nor references, just plain text.
                if not div.get("type"):
                    div_text = div.get_text(separator=' ', strip=True)
                    divs_text.append(div_text)

            plain_text = " ".join(divs_text)
            self._text = divs_text
        return self._text



tei = TEIFile('sample.tei.xml')
f"The authors of the paper entitled '{tei.title}' are {tei.authors}"


tei.text

head_datas = [head.get_text() for head in soup.find_all('head')]
head_datas

soup.find_all('h1')

soup.find_all('div')[2]

# +
divs_text=[]
for div in soup.body.find_all("div")[1:]:
    # div is neither an appendix nor references, just plain text.
    if not div.get("type"):
        div_text = div.get_text(separator=' ', strip=True)
        divs_text.append(div_text)
        #rint(divs_text)



# -

div_text.split(' ')[0]

divs_text

soup.find_all('div')[2]

soup.prettify()

tei_doc = 'sample.tei.xml'
with open(tei_doc, 'r') as tei:
    soup1 = BeautifulSoup(tei, 'xml')

soup1.find_all('head')

headings=[]
for div in soup1.body.find_all("head"):
    # div is neither an appendix nor references, just plain text.
    try:
        if not div.get("type"):
            div_text = div.get_text(separator=' ', strip=True)
            headings.append((div_text, div['n']))
        #rint(divs_text)
    except KeyError:
        headings.append(div_text)
        pass
headings

# +
d={}
j=0
for i in range(len(divs_text)):
    j=j+1
    if(type(headings[i])==tuple):
        if(headings[i][1].split('.')[0] not in d.keys()):
            d[headings[i][1].split('.')[0]]=[divs_text[i]]
        else:
            d[headings[i][1].split('.')[0]].append(divs_text[i])
    
    else:
        #print(divs_text[i])
        d[str(j)]=[divs_text[i]]
        
d
# -

type((1,2))==tuple

for i in range(len(divs_text)):
    x=divs_text[i]
    y=headings[i][0]
    
    print(x.split(' ')[0:len(y.split(' '))])
    print(y)


final=[]
for i in divs_text:




#d={}
if(2 not in d.keys()):
    d[2]=[1]
else:
    d[2].append(2)
d

# +
#for div in soup1.body.find_all("head"):
#    print(type(div))
#    print(div.name)
#    print(div['n'])
# -


