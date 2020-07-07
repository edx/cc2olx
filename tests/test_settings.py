from pathlib import Path

from cc2olx.cli import parse_args
from cc2olx.settings import collect_settings


def test_collect_settings(imscc_file):
    parsed_args = parse_args([
        "-i",
        str(imscc_file)
    ])

    settings = collect_settings(parsed_args)

    assert settings == {
        "input_files":  {imscc_file},
        "output_format": parsed_args.result,
        "workspace": Path.cwd() / "tmp",
        "logging_config": {
            "level": parsed_args.loglevel,
            "format": "{%(filename)s:%(lineno)d} - %(message)s",
        }
    }
