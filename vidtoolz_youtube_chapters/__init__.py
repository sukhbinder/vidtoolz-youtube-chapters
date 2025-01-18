import vidtoolz
from vidtoolz_youtube_chapters.youtubechapters import (
    read_timeline_from_file,
    format_timeline,
)
import sys


def create_parser(subparser):
    parser = subparser.add_parser(
        "chapters", description="Write formated youtube chapters with text inputs"
    )
    # Add subprser arguments here.
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file_path", type=str, help="Path to the input file.", default=None
    )
    group.add_argument(
        "-t",
        "--text",
        nargs="*",
        help="Supply text or if '-' Read from standard input instead of file.",
    )

    return parser


class ViztoolzPlugin:
    """ Write formated youtube chapters with text inputs """

    __name__ = "chapters"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.hello)

    def hello(self, args):
        # this routine will be called when "vidtoolz "chapters is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")

    def run(self, args):
        if args.file_path:
            print(read_timeline_from_file(args.file_path))
        elif args.text:
            text = " ".join(args.text)
            if text == "-":
                try:
                    text = str(sys.stdin.buffer.readline())
                    print(format_timeline(text))
                except ValueError:
                    pass
            else:
                print(format_timeline(text))
        else:
            self.parser.print_help()


chapters_plugin = ViztoolzPlugin()
