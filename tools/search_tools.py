import json
import os

import requests
from langchain.tools import tool


class SearchTools():
    @tool("Search the internet")
    def search_internet(query):
        """
        Usefull to search the internet about a given topic
        :return: relevant results
        """
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "No results found"
        results = response.json()['organic']
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append(''.join([f"Title: {result['title']}\n", f"Link: {result['url']}",
                    f"Snippet: {result['snippet']}", "\n----------------"]))
            except KeyError:
                next
        return '\n'.join(string)


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    print("Search the internet about Python programming")
    print(SearchTools.search_internet('Python programming'))
