__author__ = 'raz0r'
__version__ = '1.1'

import click

from .tasks import default_tasks
from .types import URL

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--proxy','proxy',type=URL(),help='HTTP Proxy to send scan traffic through')
@click.argument('url', type=URL())
@click.version_option()
def main(url, proxy):
    """\b
           ______ __  __  _____
     /\   |  ____|  \/  |/ ____|
    /  \  | |__  | \  / | (___   ___ __ _ _ __
   / /\ \ |  __| | |\/| |\___ \ / __/ _` | '_ \\
  / ____ \| |____| |  | |____) | (_| (_| | | | |
 /_/    \_\______|_|  |_|_____/ \___\__,_|_| |_|


aemscan - Adobe Experience Manager Vulnerability Scanner"""

    click.echo(main.__doc__)
    click.echo("version: {}\n".format(__version__))

    if proxy:
      proxy_input_from_user = proxy
      proxy = {'http': proxy, 'https': proxy}
    else:
      proxy_input_from_user = "None"
      proxy = {}     

    click.echo(click.style("Proxy: " + proxy_input_from_user, fg='yellow'))
    click.echo(click.style("URL: " + url, fg='yellow'))    
    
    for task in default_tasks:
        task.run(url, proxy)

if __name__ == '__main__':
    main()