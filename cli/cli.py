# -*- coding: utf-8 -*-
"""
CLI for the rule them all program
"""

import arrow
import click
from app import AppManager

pass_app = click.make_pass_decorator(AppManager, ensure=True)
# Map some cli-specific shortcuts to the keyboard
CLI_ACTIONS = {
    'q': lambda: exit(0)
}


def echo_header(text):
    """ Echo a stylish header, 79 characters long. """
    txtlen = len(text)
    border_len = (80 - txtlen - 2) // 2
    hborder = click.style('=' * border_len, fg='green')
    text = click.style(' {} '.format(text), bold=True)
    click.echo('{}{}{}'.format(hborder, text, hborder))


@pass_app
def menu(app):
    # Choices available for the user are numbers within the range of 1 and the
    # number of options, PLUS the keys of the CLI specific actions
    prompt_choices = range(1, len(app.options))
    prompt_choices = list(map(lambda x: str(x), prompt_choices))
    prompt_choices.extend(CLI_ACTIONS.keys())
    validate_prompt = click.Choice(prompt_choices)

    def echo_menu_row(i, text, installed=None, show_status=True,
                      *args, **kwargs):
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
        # humanize datetime
        try:
            inst = arrow.Arrow.utcfromtimestamp(inst).humanize()
        except Exception as e:
            # installed is not a parsable string. maybe is missing?
            # don't care.
            pass
        date_ = '({})'.format(click.style(inst, dim=True)) if dispclr else ''

        # Print out the created row
        click.echo('{i}{s}{t}{d}'.format(i=idx, t=txt, d=date_, s=status))

    def handle_chose_option(choice):
        click.echo()
        # Ask for confirmation.
        confirm_str = click.style(choice['text'], bold=True, fg='yellow')
        descr = choice.get('description')
        if descr:
            click.echo(descr)
        click.echo()
        if click.confirm(confirm_str, default='yes', show_default=True):
            execute_choice(choice)

    def execute_choice(choice):
        output, error = None, None
        try:
            output, error = choice['callback']()
        except TypeError as e:
            # FIXME: This pass is due to the missing callback function
            # normalization, meaning that we have to be sure the the callback
            # returns a tuple (likely with function output and errors), or else
            # it will fail while unpacking the return value. This except clause
            # allows to bypass it
            error = 'Callback for `{}` has issues.\n{}'.format(
                choice['text'], e)
        except Exception as e:
            click.echo(e)
            msg = 'Error while trying to run option `{}` function!\n'\
                  '>>> {}\n'.format(choice['text'], e, choice)
            click.secho(msg, fg='red', bold=True)

        if output:
            click.secho(output, fg='green')
        elif error:
            click.secho(error, fg='red')
    # Execution time!

    click.clear()
    echo_header('One bootstrap to rule them all')
    click.echo()

    # Generate the menu
    for i, opt in enumerate(app.options):
        echo_menu_row(i, **opt)
    click.echo()

    choice = click.prompt(
        'What to do next', type=validate_prompt, prompt_suffix='? ')

    try:
        choice = app.options[int(choice) - 1]
        handle_chose_option(choice)
    except ValueError:
        # `choice` can't be converted to integer, so it's not a menu valid
        # app option. try with cli specific command that, if created right
        # should not raise anything.
        try:
            CLI_ACTIONS[choice.lower()]()
        except TypeError as e:
            # choice doesn't map to a callable
            click.secho(str(e), fg='yellow')
        except Exception as e:
            # Everything else that could be specific to the callback func.
            # We don't want the program to crash, so catch everything, log and
            # go ahead
            click.secho(str(e), fg='red')

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
    app.verbosity = verbose

    # If no command is passed execute the start automatically
    if ctx.invoked_subcommand is None:
        ctx.invoke(start)


@cli.command(short_help='Interactive mode')
@pass_app
def start(app):
    """
    Entry point for the cli application. takes care of setting up things
    locally and launching the main menu for the first time.
    """

    menu()


if __name__ == '__main__':
    cli()
