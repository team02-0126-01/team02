class Posts:
    def __init__(self, id:int, title:str, body:str,*comment:list):
        self.id = id
        self.title = title
        self.body = body
        self.comment = comment