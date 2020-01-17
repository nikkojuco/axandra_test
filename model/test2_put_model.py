from flask_restplus.reqparse import RequestParser


class Test2PutModel:

    def __init__(self):
        self._request_parser = RequestParser(bundle_errors=True)
        self._request_parser.add_argument('website', type=str, help='Website', required=True)
        self._request_parser.add_argument('is_malicious', type=str, help='Malicious Status', required=True)

    def get_req_parser(self):
        req_parser = self._request_parser.parse_args()
        return req_parser
