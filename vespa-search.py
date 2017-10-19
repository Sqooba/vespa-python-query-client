#!/usr/bin/env python3

import requests
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
    'Complete YQL Query. May or may not be terminated with \';\''
)

flags.DEFINE_string(
    'query',
    None,
    'Simple Vespa query. Mutually exclusive with --yql'
)

flags.mark_flags_as_mutual_exclusive(('yql', 'query'), required=True)

flags.DEFINE_boolean(
    'ssl',
    False,
    'Should the query be issued over https.'
)

flags.DEFINE_list(
    'param',
    [],
    'Parameters to be added to the request. Comma separated list.'
    'E.g. hitcountestimate=True,tracelevel=2'
)


def parse_args(argv):
    if len(argv) == 1:
        print('Options:\n%s' % FLAGS)
        exit(1)
    flags.FLAGS(argv)


def check_yql_semicolon(yql):
    ret = yql.strip()
    if not ret.endswith(';'):
        return ret + ';'
    return ret


def add_query(payload):
    if FLAGS.yql is not None:
        payload['yql'] = check_yql_semicolon(FLAGS.yql)
    else:
        payload['query'] = FLAGS.query.strip()


def prefix(ssl_flag):
    if ssl_flag:
        return 'https'
    return 'http'


def main(argv):
    """
    Issue search requests to a Vespa http(s) search end-point.
    """
    parse_args(argv)

    payload = dict([tuple(p.split('=')) for p in FLAGS.param])
    print('Additional parameters:\n%s' % payload)

    add_query(payload)

    req_string = '%s://%s:%d/search/' \
                 % (prefix(FLAGS.ssl), FLAGS.host, FLAGS.port)

    r = requests.get(req_string, params=payload)
    print("Issuing call to:\n", r.url, "\n")
    print("Response:\n")
    print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    main(sys.argv)
