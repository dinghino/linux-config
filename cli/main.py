import click
from app import AppManager, launch_test_script

pass_conf = click.make_pass_decorator(AppManager, ensure=True)


def echo_header(text):
    """ Echo a stylish header. """
    hborder = click.style('===', fg='green')
    text = click.style(' {} '.format(text), bold=True)
    click.echo('{}{}{}'.format(hborder, text, hborder))


@pass_conf
def setup(config):
    """
    App setup entry point from cli. allows interactive configuration of
    basic informations such as usernames and passwords that will be used or
    stored when needed.
    """
    click.clear()
    echo_header('Basic configuration')
    click.echo('Some configuration so I can work better!')
    if not config.sudo:
        sudo = click.prompt(
            'Enter your sudo password, so I won\'t ask again',
            type=str, hide_input=True, confirmation_prompt=True)

        config.sudo = sudo
    if click.confirm('Have github?', default='yes'):
        get_gh_login()

    config.update_option('setup', value='Done')


@pass_conf
def get_gh_login(config):
    config.has_gh = True
    gh_user = click.prompt('Username', type=str)
    gh_pass = click.prompt('Password', hide_input=True,
                           confirmation_prompt=True)
    config.gh_user = gh_user
    config.gh_pass = gh_pass


@pass_conf
def menu(config):
    validate_prompt = click.IntRange(1, len(config.options))

    def echo_menu_row(i, text, installed=None, *args, **kwargs):
        ins = installed
        """ print a row of the main menu with status. """
        idx = click.style('{:^3}'.format(i + 1), bold=True)
        idx = click.style('{}'.format(idx))
        # txt color and date_ string are defined by the presence of installed
        # argument, allowing a visual feedback on what's done already.
        txt = '{:<35}'.format(click.style(text, fg='green' if ins else ''))
        date_ = '({})'.format(click.style(ins, dim=True)) if ins else ''
        # Print out the created row
        click.echo('{i} {t}{d}'.format(i=idx, t=txt, d=date_))

    click.clear()
    echo_header('One bootstrap to rule them all')

    # Generate the menu
    for i, opt in enumerate(config.options):
        echo_menu_row(i, **opt)

    # Get the user choice
    choice = click.prompt('What to do next',
                          type=validate_prompt,
                          prompt_suffix='? ')
    # Get the correct option from the app options list
    chosen = config.options[choice - 1]

    # Ask for confirmation.
    confirm_str = '  {}'.format(
        click.style(chosen['text'], bold=True, fg='yellow'))
    if click.confirm(confirm_str, default='yes', show_default=True):
        chosen['callback']()
        click.pause()

    menu()


@click.group()
@click.option('-v', '--verbose', count=True, default=0)
@pass_conf
def cli(config, verbose):
    """
    Bootstrap application for linux system.
    Allows management of basic dependecies and application for developing in
    Python 3.6, node.js etc.

    It also manages some system configuration and basic application such as
    terminal emulators (tilix), vim (with optionak configuration), visual studio
    code...
    """
    # Update configuration values
    config.verbose = verbose
    # Add cli specific functionalities to the options from the app
    config.add_option('Setup', setup, 0)
    config.add_option(click.style('Quit', fg='yellow'), lambda: exit(0))
    config.add_option(click.style('Test', fg='red'), launch_test_script)


@cli.command()
@pass_conf
def start(config):
    """ Interactive mode with menu and stuff. """

    # if not config.setup_done:
    #     setup()
    menu()


if __name__ == '__main__':
    cli()
