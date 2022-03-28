# 10 28.03.2022

class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        if title == '':
            title = 'Unknown'
        if author == '':
            author = 'Unknown'
        print(f"\n\nNew song made:\nTitle: {title} \nAuthor: {author}")

    def sing(self, lines_present=-1):
        x = '_' * (len(self.author + self.title) + 3)
        print(x, '\nSinging:')
        self._print_lines(self.lyrics, lines_present)
        return self

    def yell(self, lines_present=-1):
        x = '_' * (len(self.author + self.title) + 3)
        lines_upper = [line.upper() for line in self.lyrics]
        print(x, '\nYELLING:')
        self._print_lines(lines_upper, lines_present)
        return self

    @staticmethod
    def _print_lines(lyrics, line_count=-1):
        all_lines_count = len(lyrics)
        if line_count == -1:
            line_count = len(lyrics)
        elif line_count <= 0:
            print("no lines to print")
        elif all_lines_count < line_count:
            print(f"only {all_lines_count} lines can be printed:\n")
        for i in lyrics[:line_count]:
            print(i)


class Rap(Song):
    def break_it(self, lines_present=-1, drop="yeah"):
        x = '_' * (len(self.author + self.title) + 3)
        lyrics = [line.replace(' ', f' {drop.upper()} ') + ' ' + drop.upper() for line in self.lyrics]
        print(x, '\nRapping:')
        self._print_lines(lyrics, lines_present)
        return self


ziemelmeita = Song('Ziemeļmeita', 'Jumprava', ['Gāju meklēt ziemeļmeitu', 'Garu, tālu ceļu veicu'])

ziemelmeita.sing(1).yell(10).sing().sing(-3)


zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])

zrap.break_it(1, "yah")