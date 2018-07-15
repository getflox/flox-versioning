import click


@click.group()
@click.pass_obj
def versioning(flox):
    """Project versioning"""
