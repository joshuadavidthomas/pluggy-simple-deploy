import pluggy

hookspec = pluggy.HookspecMarker("simple_deploy")


@hookspec
def simple_deploy_confirm_platform_preliminary():
    """Confirm the platform and perform any preliminary setup."""
    ...


@hookspec
def simple_deploy_prep_automate_all():
    """Perform any preparation needed before automating the entire deployment."""
    ...


@hookspec
def simple_deploy_deploy():
    """Deploy the project."""
    ...