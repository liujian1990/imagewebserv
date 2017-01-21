class VideoCtrl:
    def __init__(self):
        self.opened = True
    def close(self):
        self.opened = False
    def get_status(self):
        return self.opened