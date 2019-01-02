from click.testing import CliRunner

from weather.scripts import cli


def test_stations():
    runner = CliRunner()
    result = runner.invoke(cli, ['get-stations'])
    assert result.exit_code == 0
    assert 'Fetching data...' in result.output
    assert 'Time taken for API call: ' in result.output
    assert 'Total no. of registered stations: ' in result.output
