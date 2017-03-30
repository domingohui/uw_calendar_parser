To learn about web scraping and HTML parsing, 
I'm using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) 
to get a list of course codes from academic plans of my university such as 
[this](https://ugradcalendar.uwaterloo.ca/page/MATH-Bachelor-of-Computer-Science-1).

### To use

Install dependencies
```shell-script
pip install -r requirements.txt
```

Run
```shell-script
python parse.py [url]
```

Or call it as a module import
```python
from parse import parse_html

parse(your_url)
```
which will return a list of codes
