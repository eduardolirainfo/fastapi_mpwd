import typer

main = typer.Typer(name="mpwd CLI")


@main.command()
def shell():
    """Opens interactive shell"""

    typer.echo("Opening interactive shell")
    try:
        from IPython import start_ipython

        start_ipython()
    except ImportError:
        import code

        code.interact()
