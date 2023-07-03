# How To Use

This repo allows you to do two things: 

1. scrape Open Music Theory to store page titles, links to assignments, and download PDFs of assignments
2. create a workbook by combine the separate PDFs into one PDF

## Installation

This project requires Python 3.9 or newer, and uses [Poetry](https://python-poetry.org/) for dependency management. If you haven't already done so, install Poetry according to the [installation instructions](https://python-poetry.org/docs/#installation).

Once Poetry is installed, run the command `poetry install` in the directory containing the `pyproject.toml` file.


## Scrape OMT

The Python library [Scrapy](https://scrapy.org/) does the actual scraping. The spider loads the URL specified in `omt/omt/spiders/omt_spider.py` (which is https://viva.pressbooks.pub/openmusictheory/part/fundamentals/) and performs the following actions:

- stores the page title, assignments section, and downloads all PDF files linked to in the assignments section
- finds the link to the next page, and performs the step above on the next page if it exists

To start scraping:

1. make sure any PDFs in the `omt/assignment_pdfs/assignment_pdfs` directory are moved or deleted
2. navigate to the `omt` directory with the terminal command `cd omt`
3. run the command `scrapy runspider omt/spiders/omt_spider.py`

The actual scraping takes a while, as there are delays between page loads and file downloads built in to the spider to avoid harming the server.

The scraping process creates a CSV file with all page data called `assignments_{datetime}.csv` and stores all downloaded PDFs in the `omt/assignment_pdfs/assignment_pdfs` directory.

## Create a workbook

While still in the `omt` directory, run the command `python combine_pdfs.py`. This will create a PDF file titled `omt_workbook.pdf` in the `omt/assignment_pdfs/joined` directory.