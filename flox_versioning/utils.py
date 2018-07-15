def unified_version(flox, name):
    return f'{flox.name}-{name}' if flox.container.issue_tracker.multiproject else name
