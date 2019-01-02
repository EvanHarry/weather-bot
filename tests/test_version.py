from click.testing import CliRunner

from weather import __version__
from weather.scripts import cli


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['version'])
    assert result.exit_code == 0
    assert result.output == 'weather-bot version-%s\n' % __version__
