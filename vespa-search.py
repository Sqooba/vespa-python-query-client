#!/usr/bin/env python3

import requests
import urllib
import json
import sys

from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'host',
    'localhost',
    'Vespa http search front-end to connect to.'
)

flags.DEFINE_integer('port', 8080, 'Port of the search front-end.')

flags.DEFINE_string(
    'yql',
    None,
    'Complete YQL Query. Will be URL encoded, nothing else.'
)

flags.mark_flag_as_required('yql')


def main(argv):
    flags.FLAGS(argv)

    r = requests.get(
        'http://%s:%d/search/?yql=%s' % (
            FLAGS.host, FLAGS.port, urllib.parse.quote_plus(FLAGS.yql))
    )

    print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    main(sys.argv)
