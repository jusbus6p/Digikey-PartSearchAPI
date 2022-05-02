from digikey.api.part_search_api import PartSearchAPI
from digikey.models.keyword_search_request import KeywordSearchRequest
from digikey.api_client import ApiClient
from digikey.configuration import Configuration

config = Configuration()

config.client_id = "EXAMPLE"
config.client_secret = "EXAMPLE"
config.client_callback_url = "EXAMPLE"

config.resource_folder_path = "EXAMPLE"


config.get_tokens_from_file()

client = ApiClient(config)

api = PartSearchAPI(client)
start = 0
while True:
    kwsr = KeywordSearchRequest(keywords="-", record_count=50, record_start_position=start)

    data = api.keyword_search(kwsr)
    stop = data.products_count
    if start >= stop:
        break
    if data is not None:
        for product in data.products:
            print(product.manufacturer_part_number)

    start += 50

