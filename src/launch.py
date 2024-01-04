from services.argument_parser import init_argparser
from util.import_phrases import import_phrases
from util import db_initializer


from board import Board


def main():
    arg_parser = init_argparser()

    if arg_parser.import_phrases:
        print("Importing phrases from file: " + arg_parser.import_phrases)
        import_phrases(arg_parser.import_phrases)

    if arg_parser.launch:
        print("Launching the game (somewhere in the future)")

    if arg_parser.initialize:
        print("Initializing the database.")
        db_initializer.initialize_database()


if __name__ == "__main__":

    main()
