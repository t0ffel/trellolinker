#!/usr/bin/env python3

from app.collector import TrelloCollector
from app.CFtoBoard import CFtoBoard

import logging
import os
import yaml
import argparse


def main():
    logging_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=logging_format,
                        level=logging.INFO)

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='report config',
                        default="config/cfsync.yml")
    parser.add_argument('--parent', help='parent card')
    parser.add_argument('action', nargs='?',
                        help='list to list custom fields,'
                        'sync_cf to sync downstream',
                        default="sync_cf")
    args = parser.parse_args()

    if os.path.isfile(args.config):
        with open(args.config, 'r') as stream:
            report_config = yaml.load(stream)
    else:
        logger.error('Invalid configuration file!')
        return

    with open("secrets/trello_secret.yml", 'r') as stream:
        trello_secret_config = yaml.load(stream)

    collector = TrelloCollector(report_config, trello_secret_config)
    logger.info('Started querying of Trello {}'.format(collector))

    if args.action == 'list':
        collector.list_boards()  # output list of Trello boards and lists
        return
    elif args.action == 'list_parents':
        collector.print_cards(collector.parent_cards_generator(), "Parent")
#         for card in collector.parent_cards_generator():
#             logger.info("Parent card: {}".format(card))
    elif args.action == 'list_all_children':
        collector.print_cards(collector.all_children_card_generator(), "Child")
    elif args.action == 'sync_cf':
        cf_list = collector.list_cf()
        for cf_val in cf_list:
            logger.info("Custom field name: {}".format(cf_val['name']))
            for board in collector.target_board_generator():
                cf_to_board = CFtoBoard(cf_val['name'], cf_val['values'],
                                        board)
                cf_to_board.check_and_add_board_cf()
        return
    else:
        logger.error('Unrecognized actions %s' % (args.action))
        return


if __name__ == '__main__':

    main()
