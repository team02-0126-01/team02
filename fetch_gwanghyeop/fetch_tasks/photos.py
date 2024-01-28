class Photos:
    def __init__(self, id: int, userid: int, name: str, url: str, thumbnail_url: str):
        self.id = id
        self.userid = userid
        self.name = name
        self.url = url
        self.thumbnail_url = thumbnail_url