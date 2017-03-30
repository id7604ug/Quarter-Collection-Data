# Quarters #

Larry, Momo, Anthony

## PDF scraping ##

Downloaded PDFs are in raw_pdf

<strike>Parse text with PyPDF2,</strike> Copy and paste text from PDF, then scrape text for initial data

Output as Django fixture

## Image scraping ##

Parse 80x80 GIFs from US Mint. Filenames are well-formatted.

Better image files exist, but are not uniformly named.

Manually processed image files are in raw_img

## Django interface ##

On first run, import fixtures from scraper

Model: State abbreviation as primary key, State name, Year issued, description
