import webbrowser
"""
webbrowser module imported, it is used for display web based documents
"""


class Nohay():
    """This class provides a way to store nohay related information"""
    def __init__(self, nohay_title, nohay_storyline, poster_image,
                 trailer_youtube):

        """
        initialize the movie instance
        Argumens:
        nohay title
        poster detail
        and youtube link
        """
        self.title = nohay_title
        self.storyline = nohay_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        this function is use show trailer
        """
        webbrowser.open(self.trailer_youtube_url)