import webbrowser
import fresh_tomatoes

"""
It is import fresh_tmatoes program
"""
import media
"""
It is use to import media module
"""

nadeem_sarwar = media.Nohay("Nadeem Sarwar", "A best Noha reciter",
                            "https://www.newsone.tv/wp-content/uploads/2017/12/Nadeem-sarwar.jpg",
                            "https://www.youtube.com/watch?v=-yZgdwUfrfU")


mir_hasan_mir = media.Nohay("Mir Hasan Mir",
                            "A natural Noha recitermairne on an alien planet",
                            "https://yaimam.com/wp-content/uploads/2017/08/Mir-Hasan-Mir-YAIMAM-logo-min.jpg",
                            "https://www.youtube.com/watch?v=JUMxGpHSSXk&t=40s")

ali_safdar = media.Nohay("Ali Safdar", "Inqalbi Noha reciter",
                         "http://i.ytimg.com/vi/dCv49nQ8v0k/hqdefault.jpg",
                         "https://www.youtube.com/watch?v=ajJ4pBXBxVQ")

nohays = [nadeem_sarwar, mir_hasan_mir, ali_safdar]
fresh_tomatoes.open_nohays_page(nohays)

"""
Calling function and also using nohay array, taking input from files entertainment and meida files and produce HTML
file name of fresh_tomatoes
"""
