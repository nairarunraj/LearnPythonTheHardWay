# Ex40 Classes

class Song:
    ## Constructor
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So, I'll stop"])

bulls_on_a_parade = Song(["They rally around the family",
                            "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_a_parade.sing_me_a_song()

lyrics = ["Twinkle twinkle little star",
            "How I wonder what you are"]

twinkle = Song(lyrics)
twinkle.sing_me_a_song()
