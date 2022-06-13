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
        list_qte_item = []
        for x in texto:
            qte_item = len(x)
            list_qte_item.append(qte_item)
            qte_total_letras += qte_item
        texto_palavras = len(texto)
        return qte_total_letras, texto_palavras, list_qte_item
    
    def frequencia(self, texto):
        frequencia_por_palavra = [texto.count(p) for p in texto]
        return dict(zip(texto, frequencia_por_palavra))

    def popularidade(self, texto, palavras):
        dFrequencia = self.frequencia(texto)
        return dict((k, dFrequencia[k]) for k in palavras if k in dFrequencia)


    def grafico(self, texto):
        itens = self.set_legther(texto)[2]
        titulo = self.get_name(texto)
        fig, ax = plt.subplots()
        ax.set_title("quantidade de letras conforme as palavras ax")
        ax.bar(titulo, itens)
        return fig
###############################################################################
#"""o que ficaria em
if __name__ == '__main__':
    extrator = Extrator()
    extrator.grafico('João silva salron')
    # pyscript.write('grafico', extrator.grafico(nome))
    
# fica no py-script dentro do html
# """