# -*- coding: utf-8 -*-
"""
CLI for the rule them all program
"""
import click
from app import AppManager

pass_app = click.make_pass_decorator(AppManager, ensure=True)


def _setup_app_context(app):
    """
    Add testing functionalities and other stuff that will be removed later on
    """
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
    # TODO: pass a callback view to allow the user to type a command that the
    # app will .execute(), allowing using commands directly from the app.
    app.add_option(
        click.style('Execute command', fg='blue'),
        None, show_status=False)


def echo_header(text):
    """ Echo a stylish header, 79 characters long. """
    txtlen = len(text)
    border_len = (80 - txtlen - 2) // 2
    hborder = click.style('=' * border_len, fg='green')
    text = click.style(' {} '.format(text), bold=True)
    click.echo('{}{}{}'.format(hborder, text, hborder))


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


@pass_app
def menu(app):
    validate_prompt = click.IntRange(1, len(app.options))

    def echo_menu_row(i, text, installed=None, show_status=True, *args, **kwargs):
        """ print a row of the main menu with status. """
        inst = installed  # shortcut

        # Status icon
        done = click.style('{:^3}'.format(' ✓ '), fg='green')
        todo = click.style('{:^3}'.format(' ✘ '), fg='red')
        nostatus = '{:^3}'.format('')
        status = nostatus if not show_status else done if inst else todo

        # User friendly option index number
        idx = click.style('{:^3}'.format(i + 1), bold=True)
        idx = '[{}]'.format(idx)

        # txt color and date_ string are defined by the presence of installed
        # argument, allowing a visual feedback on what's done already.
        dispclr = inst and show_status
        txt = '{:<35}'.format(click.style(text, fg='green' if dispclr else ''))
        date_ = '({})'.format(click.style(inst, dim=True)) if dispclr else ''

        # Print out the created row
        click.echo('{i}{s}{t}{d}'.format(
            i=idx, t=txt, d=date_, s=status))

    click.clear()
    echo_header('One bootstrap to rule them all')
    click.echo()
    # Generate the menu
    for i, opt in enumerate(app.options):
        echo_menu_row(i, **opt)
    click.echo()

    # Get the user choice
    choice = click.prompt('What to do next',
                          type=validate_prompt,
                          prompt_suffix='? ')
    # Get the correct option from the app options list
    chosen = app.options[choice - 1]
    click.echo()
    # Ask for confirmation.
    confirm_str = '  {}'.format(
        click.style(chosen['text'], bold=True, fg='yellow'))
    if click.confirm(confirm_str, default='yes', show_default=True):
        try:
            chosen['callback']()
        except TypeError as e:
            msg = 'Error while trying to run option {} function!\n'\
                  '>>> {}'.format(choice, e)
            click.secho(msg, fg='red', bold=True)
        click.pause()

    menu()


@click.group(invoke_without_command=True)
@click.option('-v', '--verbose', count=True, default=0)
@pass_app
@click.pass_context
def cli(ctx, app, verbose):
    """
    Bootstrap application for linux system.
    Allows management of basic dependecies and application for developing in
    Python 3.6, node.js etc.

    It also manages some system configuration and basic application such as
    terminal emulators (tilix), vim (with optionak configuration), visual studio
    code...
    """
    # Update configuration values
    app.verbose = verbose

    # add some configuration for testing and stuff to the app context
    _setup_app_context(app)

    # Quit option should be last
    app.add_option(
        click.style('Quit', fg='yellow'),
        lambda: exit(0),
        show_status=False)

    # If no command is passed execute the start automatically
    if ctx.invoked_subcommand is None:
        ctx.invoke(start)


@cli.command()
@pass_app
def start(app):
    """ Interactive mode with menu and stuff. """
    # if not app.setup_done:
    #     setup()
    menu()


@cli.command('install')
@click.argument('script')
@pass_app
def install_directly(app, script):
    """Run an install script."""
    click.echo('Installing: {}'.format(script))
    click.echo('Fake for now...')


if __name__ == '__main__':
    cli()
