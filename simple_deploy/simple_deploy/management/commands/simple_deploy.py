import importlib

from django.core.management.base import BaseCommand

from simple_deploy.plugins import pm


class Command(BaseCommand):
    """Perform the initial deployment of a simple project.
    Configure as much as possible automatically.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--platform",
            type=str,
            help="Which platform do you want to deploy to?",
            default="",
        )

    def handle(self, *args, **options):
        """Parse options, and dispatch to platform-specific helpers."""
        self.stdout.write("Configuring project for deployment...")

        # Load the platform-specific plugin.
        # Surely there's a better way to do this? But for a proof of concept,
        # this is fine.
        try:
            module = importlib.import_module(
                f"simple_deploy.backends.{options['platform']}"
            )
        except ModuleNotFoundError:
            try:
                plugin_module = f"simple_deploy_{options['platform']}"
                module = importlib.import_module(plugin_module)
            except ModuleNotFoundError:
                self.stdout.write(f"Unknown platform: {options['platform']}")
                return
        
        pm.register(module, options["platform"])

        # Call the platform-specific hooks.
        pm.hook.simple_deploy_confirm_platform_preliminary()
        pm.hook.simple_deploy_prep_automate_all()
        pm.hook.simple_deploy_deploy()
