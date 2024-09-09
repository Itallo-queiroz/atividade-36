import random

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self, outra_pessoa):
        return f"\033[93mTudo bem, {outra_pessoa.nome}? Sou {self.nome} e tenho {self.idade} anos. Você lembra de mim? \033[0m"

    def conversar(self, outra_pessoa):
        saudacao = self.cumprimentar(outra_pessoa)
        resposta = outra_pessoa.responder(self)
        assunto = self.escolher_assunto()
        retorno_assunto = outra_pessoa.falar_sobre(assunto)
        return (f"{saudacao}\n"
                f"{resposta}\n"
                f"{self.nome}: {assunto}\n"
                f"{outra_pessoa.nome}: {retorno_assunto}")

    def responder(self, outra_pessoa):
        respostas = [
            f"\033[92mOlá, {outra_pessoa.nome}! Lembro sim. Como você está hoje?\033[0m",
            f"\033[92mOi {outra_pessoa.nome}! Claro que lembro. Como vai você?\033[0m",
            f"\033[92mOi {outra_pessoa.nome}! Que bom te ver. Como você tem passado?\033[0m"
        ]
        return random.choice(respostas)

    def escolher_assunto(self):
        assuntos = [
            "\033[93mVocê tem algum plano para o fim de semana? \033[0m",
            "\033[93mQual foi a última série ou livro que você leu? \033[0m",
            "\033[93mVocê já pensou em fazer uma viagem para algum lugar novo? \033[0m",
            "\033[93mComo está seu trabalho/estudos? Alguma novidade? \033[0m",
            "\033[93mQual é o seu hobby favorito? \033[0m"
        ]
        return random.choice(assuntos)

    def falar_sobre(self, assunto):
        if "fim de semana" in assunto:
            respostas = [
                "\033[92mEstou planejando relaxar e talvez fazer uma caminhada no parque. E você?\033[0m",
                "\033[92mVou aproveitar para assistir a alguns filmes que estou adiando há um tempo. Você tem alguma recomendação?\033[0m"
            ]
            return random.choice(respostas)
        elif "série" in assunto or "livro" in assunto:
            respostas = [
                "\033[92mAcabei de ler um livro incrível sobre desenvolvimento pessoal. Você tem alguma sugestão de leitura?\033[0m",
                "\033[92mRecentemente terminei uma série de suspense que eu realmente gostei. E você, está assistindo algo interessante?\033[0m"
            ]
            return random.choice(respostas)
        elif "viagem" in assunto:
            respostas = [
                "\033[92mEstou pensando em visitar algum lugar histórico, como Roma ou Atenas. Você já foi a algum lugar interessante?\033[0m",
                "\033[92mQuero conhecer uma cidade litorânea. Alguma sugestão de destino?\033[0m"
            ]
            return random.choice(respostas)
        elif "trabalho" in assunto or "estudos" in assunto:
            respostas = [
                "\033[92mMeu trabalho está bem, estou envolvido em um projeto novo. E o seu, como está indo?\033[0m",
                "\033[92mEstou focado em meus estudos e me preparando para alguns exames importantes. E você, está ocupado com o que?\033[0m"
            ]
            return random.choice(respostas)
        elif "hobby" in assunto:
            respostas = [
                "\033[92mEstou realmente gostando de tocar violão no meu tempo livre. E você, tem algum hobby que ama?\033[0m",
                "\033[92mMeu hobby favorito é cozinhar. Estou sempre tentando novas receitas. E o seu?\033[0m"
            ]
            return random.choice(respostas)
        else:
            return "\033[92mNão tenho muito o que dizer sobre isso, mas estou sempre disposto a ouvir.\033[0m"


# Criando dois objetos da classe Pessoa
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Carlos", 30)

# Mostrando a conversa amigável e interessante entre os dois objetos
conversa = pessoa1.conversar(pessoa2)
print(conversa)
