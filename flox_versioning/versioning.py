import click

from flox_versioning.utils import unified_version


@click.group()
@click.pass_obj
def version(flox):
    """Project versioning"""


@version.command(name="list")
@click.pass_obj
def list_versions(flox):
    versions = flox.container.issue_tracker.versions.list()
    print(versions)


@version.command()
@click.pass_obj
@click.argument('name')
def create(flox, name):

    version = flox.container.issue_tracker.versions.create(name)
    print(version)


@version.command()
@click.pass_obj
@click.option('--version', default='rc')
@click.argument('issue')
def assign(flox, version, issue):
    tracker = flox.container.issue_tracker
    version_name = unified_version(flox, version)

    tracker_version = tracker.versions.find(version_name)
    if not tracker_version:
        tracker_version = tracker.versions.create(version_name)

    tracker_issue = tracker.issues.get(issue)
    tracker_issue.assign_version(tracker_version)
