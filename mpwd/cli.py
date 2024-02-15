""" mpwd CLI """
import code

import typer
from IPython import start_ipython

main = typer.Typer(name="mpwd CLI")


@main.command()
def shell():
    """Opens interactive shell"""

    typer.echo("Opening interactive shell")
    try:
        start_ipython()
    except ImportError:
        code.interact()
