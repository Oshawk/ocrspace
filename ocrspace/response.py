class Response:
    def __init__(self, json):
        self.text = json["ParsedResults"][0]["ParsedText"]
        self.raw = json

    def __str__(self):
        return self.text