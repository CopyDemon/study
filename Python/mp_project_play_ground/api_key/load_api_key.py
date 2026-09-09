"""
This module is used to load the api key from the system env vars
"""
import os

class Load_API_Key:
    def __init__(self,which_key:str):
        self.which_key = which_key
        self.api_key = self._get_api_key()

    def _get_api_key(self):
        """private method to get the api key, assigned to self.api_key
        later will use getter to return to caller
        Returns:
            string: the api key
        """
        try:
            if not self.which_key:
                # required arg check
                raise ValueError("arg which_key is not set, its required")
            
            api_key = os.getenv(self.which_key)
            if not api_key:
                # api key existing check
                raise ValueError(f"API key {self.which_key} is not set in system env vars")
            return api_key
        except ValueError as e:
            raise ValueError(f"Failed to load API key {self.which_key}: {e}") from e
    
    def get_key(self):
        """callable getter method to get the api key

        Returns:
            string: the api key
        """
        try:
            if not self.api_key:
                # api key existing check
                raise ValueError("api key is not set, please check system env vars")
            return self.api_key
        except ValueError as e:
            raise ValueError(f"Failed to get API key {self.which_key}: {e}") from e
        


