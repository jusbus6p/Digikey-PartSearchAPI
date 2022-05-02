from __future__ import annotations

import pprint

from digikey.api_client import ApiClient
from digikey.models import KeywordSearchRequest
from digikey.models import KeywordSearchResponse
from digikey.api_exception import ApiException


class PartSearchAPI(object):
    def __init__(self, api_client: ApiClient = None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def keyword_search(self, keyword_search_request: KeywordSearchRequest) -> KeywordSearchResponse | None:

        response_data, response_code = self.api_client.call_api("/Products/Keyword",
                                                                "POST",
                                                                keyword_search_request.to_dict(api_friendly=True),
                                                                KeywordSearchResponse)

        if not 200 <= response_code <= 299:
            return None

        return response_data

