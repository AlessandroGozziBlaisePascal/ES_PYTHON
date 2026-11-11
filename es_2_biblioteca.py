class Biblioteca:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.libri = []

    def aggiungi_libro(self, libro: Libro) -> None:
        self.libri.append(libro)

    def cerca_per_titolo(self, testo: str) -> List[Libro]:
        testo = testo.lower()
        return [libro for libro in self.libri if testo in libro.titolo.lower()]

    def cerca_per_autore(self, autore: str) -> List[Libro]:
        autore = autore.lower()
        return [libro for libro in self.libri if autore in libro.autore.lower()]

    def conta_libri(self) -> int:
        return len(self.libri)

    def __len__(self) -> int:
        return self.conta_libri()