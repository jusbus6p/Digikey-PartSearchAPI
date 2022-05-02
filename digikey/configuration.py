import pprint
from typing import Union

import requests
import json
import time
import os


class Configuration(object):
    def __init__(self):
        # Default Base url
        self.host = "https://api.digikey.com/Search/v3"
        # Folder for downloading files
        self.resource_folder_path = None

        # Authentication Settings
        self.client_id = ""
        self.client_secret = ""
        self.client_callback_url = ""

        self.oauth_file = "dk_oauth.json"

        self.refresh_oath_host = "https://api.digikey.com/v1/oauth2/token"
        # access token for OAuth
        self.access_token = ""
        self.access_token_lifetime = 1799
        self.access_token_expire_time = 0

        self.refresh_token = ""
        self.refresh_token_lifetime = 7775999
        self.refresh_token_expire_time = 0

        self.access_token_prefix = "Bearer"

        self.locale_site = "US"
        self.locale_language = "en"
        self.locale_currency = "USD"

        self.accept = "application/json"
        self.content_type = "application/json"

    def create_header(self) -> dict:
        header = {
            "accept": self.accept,
            "Content-type": self.content_type,
            "X-DIGIKEY-Client-Id": self.client_id,
            "Authorization": self.access_token_prefix + " " + self.access_token,
            "X-DIGIKEY-Locale-Site": self.locale_site,
            "X-DIGIKEY-Locale-Language": self.locale_language,
            "X-DIGIKEY-Locale-Currency": self.locale_currency
        }
        return header

    def get_tokens_from_file(self):
        try:
            with open(self.resource_folder_path + os.path.sep + self.oauth_file) as auth:
                auth_file = json.load(auth)
        except Union[FileNotFoundError, IOError]:
            self.refresh_tokens()
            return

        self.access_token = auth_file["access_token"]
        self.refresh_token = auth_file["refresh_token"]
        self.access_token_expire_time = auth_file["access_token_expire"]
        self.refresh_token_expire_time = auth_file["refresh_token_expire"]
        if int(self.access_token_expire_time) < int(time.time()):
            self.refresh_tokens()
        if int(self.refresh_token_expire_time) < int(time.time()):
            self.refresh_tokens()

    def refresh_tokens(self, refresh_token=""):
        if refresh_token == "":
            refresh_token = self.refresh_token
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }
        header = {"Content-type": "application/x-www-form-urlencoded"}

        response = requests.post(self.refresh_oath_host, data=data, headers=header)
        created_time = int(time.time())
        expire_time_auth_token = created_time + self.access_token_lifetime
        self.access_token_expire_time = expire_time_auth_token
        expire_time_refresh_token = created_time + self.refresh_token_lifetime
        self.refresh_token_expire_time = expire_time_refresh_token
        data = response.json()
        if response.status_code == 200:
            response.close()

            to_file = {"access_token": data["access_token"], "refresh_token": data["refresh_token"],
                       "access_token_expire": self.access_token_expire_time,
                       "refresh_token_expire": self.refresh_token_expire_time, "last_modified": created_time}

            self.access_token = data["access_token"]

            self.refresh_token = data["refresh_token"]

            with open(self.resource_folder_path + os.path.sep + self.oauth_file, 'w') as auth:
                json.dump(to_file, auth)

