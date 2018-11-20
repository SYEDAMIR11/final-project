import webbrowser
class Nohay():
    """This class provides a way to store nohay related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, nohay_title, nohay_storyline, poster_image,
                trailer_youtube) :
        self.title = nohay_title
        self.storyline = nohay_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)