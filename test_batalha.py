import unittest
from Jogador import Jogador
from Embarcacao import Embarcacao
from PosicionarFrota import posicao_valida, posicionar_embarcacao
from Partida import realizar_jogada

class TesteBatalhaNaval(unittest.TestCase):
    def setUp(self):
        # Criação de jogador e embarcação para os testes
        self.jogador = Jogador("Jogador1", "humano")
        self.embarcacao = Embarcacao("Porta-Aviões", 5)

    def test_criar_embarcacao(self):
        # Verifica se a embarcação foi criada corretamente
        self.assertEqual(self.embarcacao.tipo, "Porta-Aviões")
        self.assertEqual(self.embarcacao.max_ataques, 5)
        self.assertEqual(self.embarcacao.ataques_recebidos, 0)

    def test_posicionar_embarcacao_valida(self):
        # Testa posicionamento válido da embarcação no tabuleiro
        valido = posicao_valida(self.jogador.tabuleiro, (0, 0), 'horizontal', self.embarcacao.tamanho)
        self.assertTrue(valido)
        sucesso = posicionar_embarcacao(self.jogador, self.embarcacao, (0, 0), 'horizontal')
        self.assertTrue(sucesso)
        self.assertIn((0, 0), self.embarcacao.posicoes)

    def test_ataque_e_status_embarcacao(self):
        # Posiciona a embarcação e simula um ataque
        posicionar_embarcacao(self.jogador, self.embarcacao, (0, 0), 'horizontal')
        resultado = realizar_jogada(self.jogador, (0, 0))
        self.assertIn(resultado, ['acertou', 'afundou'])
        self.assertGreaterEqual(self.embarcacao.ataques_recebidos, 1)

# ---------------------------------------------
# COMO RODAR OS TESTES:
#
# No terminal, vá até a pasta do projeto e execute:
# python test_batalha.py
# ou
# python -m unittest test_batalha.py
#
# Os testes irão rodar automaticamente e mostrar o resultado
# ---------------------------------------------

if __name__ == "__main__":
    unittest.main()
