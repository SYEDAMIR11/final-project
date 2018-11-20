import fresh_tomatoes
import media
import webbrowser
nadeem_sarwar = media.Nohay("Nadeem Sarwar"," A best Noha reciter","https://i.ytimg.com/vi/6tyKj2ZeAsc/maxresdefault.jpg","https://www.youtube.com/watch?v=-yZgdwUfrfU")

#print (nadeem_sarwar.storyline)
mir_hasan_mir = media.Nohay("Mir Hasan Mir", "A natural Noha recitermairne on an alien planet","https://yaimam.com/wp-content/uploads/2017/08/Mir-Hasan-Mir-YAIMAM-logo-min.jpg","https://www.youtube.com/watch?v=JUMxGpHSSXk&t=40s")
#print (mir_hasan_mir.storyline)
#mir_hasan_mir.show_trailer()

ali_safdar = media.Nohay("Ali Safdar", "Inqalbi Noha reciter","https://4.bp.blogspot.com/-3rvZ_N5fbLs/V9z-Bz1WHFI/AAAAAAAAAJk/GC6e31tlNvMMzLQXmMx5gLtf_JDxSt4QQCPcB/s320/ali-safdar-nohay.jpg","https://www.youtube.com/watch?v=ajJ4pBXBxVQ")


nohays = [nadeem_sarwar, mir_hasan_mir, ali_safdar]
fresh_tomatoes.open_nohays_page(nohays)
#print (media.Nohay.VALID_RATINGS)
#print (media.Nohay.__module__)
#print (media.Nohay.__name__)
#print (media.Nohay.__doc__)
