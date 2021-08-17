import logging
import sys
import argparse
import lusid as lu

from lusid.utilities import ApiClientFactory


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    logging_formatter = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
    stdout_handler.setFormatter(logging_formatter)
    root_logger.addHandler(stdout_handler)


def main(argv):
    setup_logging()

    ap = argparse.ArgumentParser()

    ap.add_argument("-k", "--key", action="store", help="API key")
    ap.add_argument("-u", "--url", action="store", help="LUSID API url")
    ap.add_argument("-c", "--cred", action="store", help="credentials file")

    args = ap.parse_args()

    # initialise an ApiFactory using either a Personal Access Token or API credentials
    api_factory = ApiClientFactory(token=args.key, api_url=args.url) if args.key else ApiClientFactory(api_secrets_filename=args.cred)

    done = False
    next_page = None
    instruments = []

    instruments_api = api_factory.build(lu.InstrumentsApi)

    while not done:

        # set a filter to determine which instruments to return,
        # see https://support.lusid.com/knowledgebase/article/KA-01914/en-us for more details
        instrument_filter = "state eq 'Active'"

        kwargs = {
            "filter": instrument_filter,
            "limit": 500
        }

        if next_page is not None:
            kwargs["page"] = next_page

        response = instruments_api.list_instruments(**kwargs)
        instruments.extend(response.values)

        next_page = response.next_page
        done = response.next_page is None

    # filter instruments that have a full instrument definition
    instruments_defn = list(filter(lambda i: i.instrument_definition is not None, instruments))

    logging.info(f"loaded {len(instruments)} instruments in total")
    logging.info(f"loaed {len(instruments_defn)} instruments with definitions")


if __name__ == "__main__":
    main(sys.argv)
