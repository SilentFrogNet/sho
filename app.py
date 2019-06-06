import os
import click

from colorama import init as colorama_init
from termcolor import colored
from click_shell import shell, add_shell_only_command
# from configobj import ConfigObj

from sho.core.sho import ShO
from sho.utils import Banners
from sho.utils.logger import Logger, LogTypes

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


# DEFAULT_DELAY = 30.0
# DEFAULT_URL_TIMEOUT = 15
# DEFAULT_SEARCH_MAX = 100
# DEFAULT_DOWNLOAD_FILE_LIMIT = 100
# DEFAULT_NUM_OF_THREADS = 8
#
# ALLOWED_CONFIG_SET_COMMANDS = ['working_dir', 'verbose', 'stealth', 'file_types', 'number_threads', 'domain']
#
# project_configs = ConfigObj('configs.ini')

class ShoConfig:

    def __init__(self):
        self.set_default_configs()
        self.sho = None
        # self.configs = project_configs

    def set_default_configs(self):
        self.logger = None

        self.working_dir = os.getcwd()
        # self.verbose = False
        # self.stealth = False
        # self.file_types = []
        # self.number_threads = DEFAULT_NUM_OF_THREADS
        # self.domain = None
        #
        # self.search_max = DEFAULT_SEARCH_MAX
        # self.download_limit = DEFAULT_DOWNLOAD_FILE_LIMIT
        # self.delay = DEFAULT_DELAY
        # self.url_timeout = DEFAULT_URL_TIMEOUT


with_context = click.make_pass_decorator(ShoConfig, ensure=True)

mypackage_root_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
    cli_version = version_file.read().strip()

colorama_init()


def echo_info(text, file=None):
    click.secho("[*] Info: ", fg='cyan', bold=True, nl="", file=file)
    click.echo(text, file=file)


def echo_warning(text, file=None):
    click.secho("[!] Warning: ", fg='yellow', bold=True, nl="", file=file)
    click.secho(text, fg='yellow', file=file)


def echo_error(text, file=None):
    click.secho("[-] Error: ", fg='red', bold=True, nl="", file=file)
    click.secho(text, fg='red', file=file)


def modify_usage_error():
    '''
        a method to append the help menu to an usage error

    :return: None
    '''

    from click._compat import get_text_stderr
    from click.utils import echo

    def show(self, file=None):
        import sys
        if file is None:
            file = get_text_stderr()
        if self.ctx is not None:
            color = self.ctx.color
            echo(self.ctx.get_usage() + '\n', file=file, color=color)
        echo_error(self.format_message(), file=file)
        sys.argv = [sys.argv[0]]

    click.exceptions.UsageError.show = show


modify_usage_error()


# def csv_list(ctx, param, value):
#     if value is None:
#         return []
#     types = value.split(',')
#
#     out_types = []
#     for t in types:
#         if t in FileTypes.special_groups():
#             out_types.extend(FileTypes.SPECIAL_GROUPS.get(t, []))
#         else:
#             if t in FileTypes.ALL:
#                 out_types.append(t)
#             else:
#                 echo_warning(f"The file type \"{t}\" is unknown. Ignored.")
#
#     return list(set(out_types))
#
#
# def parse_ctx_config_set(ctx, param, value):
#     if not value:
#         return None
#
#     vals = value.split("=")
#     if len(vals) != 2:
#         return None
#
#     cmd = vals[0].strip()
#     val = vals[1].strip()
#
#     if cmd in ALLOWED_CONFIG_SET_COMMANDS:
#         return {
#             'option': cmd,
#             'value': val
#         }
#
#     return None


def get_shell_prompt():
    return f"{colored('ShO', 'red', attrs=['bold'])}> "


def get_shell_intro():
    return "Loading ShO..."


def get_history_file():
    # return project_configs.get('DEFAULT', {}).get('support_directory', '~/.click-history')
    return '~/.click-history'


@shell(prompt=get_shell_prompt(), intro=get_shell_intro(), hist_file=get_history_file(), context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', '-v', is_flag=True,
              help="Enables verbose mode.")
@click.version_option(version=cli_version)
@click.pass_context
def cli(ctx, verbose):
    """
    ShO is a command line tool to safely store shells configurations.
    """

    ctx.obj = ShoConfig()
    ctx.obj.sho = ShO(verbose=verbose)

    ctx.obj.logger = Logger(LogTypes.TO_COLORED_SCREEN)


@cli.command()
@with_context
def list(ctx_conf):
    """
    Lists all the shells that has already been saved.
    """

    shells = ctx_conf.sho.list()
    if shells:
        for s in shells:
            echo_info(s)
    else:
        echo_info("No configured shells. Please use the 'add' command to add them.")


@cli.command()
def banner():
    """
    Prints a random banner of the application
    """
    banner_str = "ShO - Copyright (C) 2019 Ilario Dal Grande @ SilentFrog\n"
    banner_str += Banners.get_random_banner(version=cli_version)
    print("\n" + banner_str)

#
# @click.command('config')
# @click.option('--view/--set', '-v/-s', is_flag=True, default=True,
#               help='Define if is in view or in set mode.')
# @click.option('--reset', is_flag=True, default=False,
#               help='If set will purge all, removing also all recovered metadata.')
# @click.argument('settings', callback=parse_ctx_config_set, expose_value=True, is_eager=True, required=False)
# @with_context
# def config_cmd(ctx_conf, view, reset, settings):
#     """
#     Set the common ctx_configurations.
#     """
#
#     '''
#     You can set:
#         working_dir PATH    Changes the working directory folder location.
#         verbose             Enables verbose mode.
#         stealth             Enables stealth mode. I'll just display found files, no downloads or analysis will be performed.
#         file_types  TYPES   A comma-separated list of file types to search/analyze. Allowed values are [pdf, doc, xls, ppt, docx, xlsx, pptx, odt, ods, odp, jpg, jpeg, tiff].
#                             Also the following special values are allowed: [ALL, OFFICE, XOFFICE, OPEN_OFFICE, IMAGES]
#         number_threads      Number of search threads. (DEFAULT: 8)
#         domain  DOMAIN      The domain to search into. It'll be used also for metadata extraction.
#     '''
#
#     if reset:
#         ctx_conf.set_default_configs()
#     else:
#         if view:
#             for attr in ALLOWED_CONFIG_SET_COMMANDS:
#                 val = getattr(ctx_conf, attr, None)
#                 if val is not None:
#                     print(f"  {attr} = {val}")
#         else:
#             if settings:
#                 val = settings['value']
#                 if settings['option'] == 'file_types':
#                     val = csv_list(ctx_conf, None, val)
#                 if settings['option'] == 'working_dir':
#                     val = os.path.abspath(val)
#                 elif settings['option'] == 'number_threads':
#                     val = to_int(val)
#                 setattr(ctx_conf, settings['option'], val)
#
#                 if ctx_conf.number_threads <= 0:
#                     echo_warning(f"Number of threads (-r) must be greater than 0. Set to default: {DEFAULT_NUM_OF_THREADS}")
#                     ctx_conf.number_threads = DEFAULT_NUM_OF_THREADS
#             else:
#                 raise click.BadParameter("Missing setting to configure")
#
#
# @click.command('purge')
# @with_context
# def purge_cmd(ctx_conf):
#     """
#     Will reset all the configurations to default.
#     """
#     ctx_conf.mercurius = None
#
#
# add_shell_only_command(cli, config_cmd, 'config')
# add_shell_only_command(cli, purge_cmd, 'purge')

# FOR DEBUG PURPOSE ONLY
import sys

if __name__ == '__main__':
    cli(sys.argv[1:])
# FOR DEBUG PURPOSE ONLY
