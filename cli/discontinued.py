"""
This module contains discontinued and test functions and cli views that just
mess the code, BUT that i want to keep for reference or future reimplementation
"""


@pass_app
def setup(app):
    """
    App setup entry point from cli. allows interactive configuration of
    basic informations such as usernames and passwords that will be used or
    stored when needed.
    """
    click.clear()
    echo_header('Basic configuration')
    click.echo('Some configuration so I can work better!')
    if not app.sudo:
        sudo = click.prompt(
            'Enter your sudo password, so I won\'t ask again',
            type=str, hide_input=True, confirmation_prompt=True)

        app.sudo = sudo
    if click.confirm('Have github?', default='yes'):
        get_gh_login()

    app.update_option('setup')


@pass_app
def get_gh_login(app):
    app.has_gh = True
    gh_user = click.prompt('Username', type=str)
    gh_pass = click.prompt('Password', hide_input=True,
                           confirmation_prompt=True)
    app.gh_user = gh_user
    app.gh_pass = gh_pass


def _setup_app_context(app):
    """Add testing functionalities that will be removed later on."""
    def launch_test_script(opt_idx):
        # TODO: Remove once done testing stuff. Function callback for
        # 'Test script call' option
        def cb():
            click.secho('Launching test script...', bold=True, bg='red')
            result = app.execute(
                app.get_script_path('apt.exists.sh python3.6'),
                cb=app.update_option, idx=opt_idx
            )
            click.secho(result, fg='cyan', bold=True)
        return cb

    # Add cli specific functionalities to the options from the app
    app.add_option('Setup', setup, 0)

    idx = len(app.options)
    app.add_option(click.style('Test script call', bold=True),
                   launch_test_script(idx))


@cli.command('install')
@click.argument('script')
@pass_app
def install_directly(app, script):
    """Run an install script."""
    click.echo('Installing: {}'.format(script))
    click.secho('Fake for now...', fg='yellow')
