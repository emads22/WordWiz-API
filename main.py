import justpy as jp
from wordwiz_api import WordWizAPI


# Register the API route with JustPy
jp.Route(WordWizAPI.path, WordWizAPI.serve)

if __name__ == "__main__":
    jp.justpy(port=8080)
