.PHONY: setup test scrape-support scrape-api

# One-command setup for a fresh machine: install the package (with dev + token
# extras) and the Chromium browser Playwright drives. Requires Python 3.9+.
setup:
	python -m pip install --upgrade pip
	python -m pip install -e '.[dev,tokens]'
	python -m playwright install chromium

test:
	python -m pytest -q

# Convenience targets that write canonical datasets into the tracked data/ dir.
scrape-support:
	docusign-scraper crawl "https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=dpj1702944516878.html&_LANG=enus" --max-pages 300 --out data/agreement-manager-support

scrape-api:
	docusign-scraper crawl "https://developers.docusign.com/docs/agreement-manager-api/" --max-pages 100 --out data/agreement-manager-api
