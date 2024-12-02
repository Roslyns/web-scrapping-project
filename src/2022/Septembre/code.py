# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key='YOUR_API_KEY')

response = app.scrape_url(url='https://tcf-canada.ca/expression-ecrite-september-2022/', params={
	'formats': [ 'json' ],
})