# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key='YOUR_API_KEY')

response = app.scrape_url(url='https://tcf-canada.ca/expression-ecrite-mars-2023/', params={
	'formats': [ 'json' ],
})