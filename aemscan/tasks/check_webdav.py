__author__ = 'raz0r'

import click
import requests

requests.packages.urllib3.disable_warnings()

def run(url, proxy):
    response = requests.options(url + '/', proxies=proxy, verify=False, timeout=20)
    if 'propfind' in response.headers.get('allow', '').lower() or response.status_code == 401:
        click.echo(click.style('WebDAV is enabled', fg='green'))
    else:
        click.echo(click.style('WebDAV is disabled', fg='red'))