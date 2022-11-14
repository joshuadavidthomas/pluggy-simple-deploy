import simple_deploy


@simple_deploy.hookimpl
def simple_deploy_confirm_platform_preliminary():
    print("Targeting Heroku")
    print("Performing preliminary Heroku setup")


@simple_deploy.hookimpl
def simple_deploy_prep_automate_all():
    print("Preparing to completely automate the Heroku deployment")


@simple_deploy.hookimpl
def simple_deploy_deploy():
    print("Deploying to Heroku")