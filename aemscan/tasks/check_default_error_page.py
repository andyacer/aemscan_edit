__author__ = 'raz0r'

import re
import click
import requests

requests.packages.urllib3.disable_warnings()

def run(url, proxy):
    response = requests.get(url + '/non_existing', proxies=proxy, verify=False, timeout=20)
    banner = parse_response(response.content)
    if banner:
        click.echo(click.style('Custom error pages are not enabled, service banner: {}'.format(banner), fg='green'))
    else:
        click.echo(click.style('Custom error pages are enabled', fg='red'))


def parse_response(response):
    match = re.search("<address>(.+?)</address>", response)
    if match:
        return match.group(1)
    return False