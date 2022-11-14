import simple_deploy


@simple_deploy.hookimpl
def simple_deploy_confirm_platform_preliminary():
    print("Targeting Fly.io")
    print("Performing preliminary Fly.io setup")


@simple_deploy.hookimpl
def simple_deploy_prep_automate_all():
    print("Preparing to completely automate the Fly.io deployment")


@simple_deploy.hookimpl
def simple_deploy_deploy():
    print("Deploying to Fly.io")