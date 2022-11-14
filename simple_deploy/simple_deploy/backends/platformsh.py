import simple_deploy


@simple_deploy.hookimpl
def simple_deploy_confirm_platform_preliminary():
    print("Targeting Platform.sh")
    print("Performing preliminary Platform.sh setup")


@simple_deploy.hookimpl
def simple_deploy_prep_automate_all():
    print("Preparing to completely automate the Platform.sh deployment")


@simple_deploy.hookimpl
def simple_deploy_deploy():
    print("Deploying to Platform.sh")
