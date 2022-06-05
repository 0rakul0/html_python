import matplotlib.pyplot as plt

class Extrator():

    def get_name(self, texto: str):
        texto = texto.split(' ')
        return texto

    def get_email(self, texto: str):
        return texto
    
    def get_phone(self, texto: str):
        return texto

    def set_legther(self, texto: str):
        qte_total_letras = 0
        texto = texto.split(' ')
        for x in texto:
            qte_item = len(x)
            qte_total_letras += qte_item
        texto_palavras = len(texto)
        return qte_total_letras, texto_palavras

    def grafico(self, texto):
        itens = self.set_legther(texto)
        titulo = self.get_name(texto)[0]
        fig, ax = plt.subplots()
        ax.set_title("quantidade de letras conforme as palavras ax")
        ax.bar(titulo, itens)
        return fig
###############################################################################
"""o que ficaria em 
if __name__ == '__main__':
    extrator = Extrator()
    extrator.grafico('João silva salron')
    pyscript.write('grafico', extrator.grafico(nome))
    
fica no py-script dentro do html
"""