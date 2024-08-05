import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup

# mute tensorflow complaints
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def extract_from_url(url):
    text = ""
    reg = urllib.request.Request(
        url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        )
    html = urllib.request.urlopen(reg)
    parser = BeautifulSoup(html, 'html.parser')
    for paragraph in parser.find_all('p'):
        print(paragraph.text)
        text += paragraph.text
    return text


def process(text):
    summarizer = pipeline('summarization', model='t5-small')
    result = summarizer(text, max_length=180)
    click.echo("Summarization process complete!")
    click.echo("=" * 80)
    return result[0]['summary_text']


@click.command()
@click.option('--url', help='URL to extract text from')
@click.option('--file', help='Text to summarize')
def main(url, file):
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file, 'r') as _f:
            text = _f.read()
    click.echo("Please provide a URL or a file to summarize")
    click.echo(f"Summarizing text from: -> {url or file}")
    click.echo(process(text))
