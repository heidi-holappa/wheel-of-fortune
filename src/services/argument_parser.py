import os

import argparse


def init_argparser():

    parser = argparse.ArgumentParser(
        prog='Wheel of Fortune',
        description='A game of Wheel of Fortune',
        epilog='Have fun playing!'
    )

    parser.add_argument(
        '-p',
        '--import_phrases',
        required=False,
        help='Import a list of phrases from a file. The file must be a .txt file with one phrase, author and category per line separated with a semicolon'
    )

    parser.add_argument(
        '-l',
        '--launch',
        required=False,
        help='Launch the game'
    )

    parser.add_argument(
        '-i',
        '--initialize',
        required=False,
        help='Initialize the database',
        action='store_true'
    )

    parser_args = parser.parse_args()

    return parser_args
