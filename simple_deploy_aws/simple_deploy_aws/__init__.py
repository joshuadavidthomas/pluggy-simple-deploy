import simple_deploy


@simple_deploy.hookimpl
def simple_deploy_confirm_platform_preliminary():
    print("Targeting AWS")
    print("Performing preliminary AWS setup")


@simple_deploy.hookimpl
def simple_deploy_prep_automate_all():
    print("Preparing to completely automate the AWS deployment")


@simple_deploy.hookimpl
def simple_deploy_deploy():
    print("Deploying to AWS")
