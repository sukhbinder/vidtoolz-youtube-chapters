import pytest
import vidtoolz_youtube_chapters as w
from vidtoolz_youtube_chapters.youtubechapters import format_timeline

from argparse import ArgumentParser


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(["-t", "hello"])
    assert result.text == ["hello"]


def test_plugin(capsys):
    w.chapters_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (
            "0 intro, 40s parking, 1m20s Fundera park, 10m Outro",
            "00:00 Intro\n00:40 Parking\n01:20 Fundera Park\n10:00 Outro",
        ),
        (
            "0s, introduction, 40s, journey starts 1m10s, parking space 2m, fundera park, 10m30, outro",
            "00:00 Introduction\n00:40 Journey Starts\n01:10 Parking Space\n02:00 Fundera Park\n10:30 Outro",
        ),
        ("1m5s start, 2m finish", "01:05 Start\n02:00 Finish"),
        ("0 intro", "00:00 Intro"),
        ("3m", "03:00 Untitled Event"),  # Missing event
        ("invalid text", ""),
    ],
)
def test_format_timeline(input_text, expected_output):
    assert format_timeline(input_text) == expected_output


def test_empty_input():
    assert format_timeline("") == ""


# def test_malformed_time():
#     malformed_input = "1.5m event, 90sec run"
#     expected_output = "01:30 Event\n01:30 Run"
#     assert format_timeline(malformed_input) == expected_output
