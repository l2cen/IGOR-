import unittest
from Jogador import Jogador
from Embarcacao import Embarcacao
from PosicionarFrota import posicao_valida, posicionar_embarcacao
from Partida import realizar_jogada

class TestBatalhaNaval(unittest.TestCase):
    def setUp(self):
        self.jogador = Jogador("Jogador1", "humano")
        self.embarcacao = Embarcacao("Porta-Aviões", 5)

    def test_criar_embarcacao(self):
        self.assertEqual(self.embarcacao.tipo, "Porta-Aviões")
        self.assertEqual(self.embarcacao.max_ataques, 5)
        self.assertEqual(self.embarcacao.ataques_recebidos, 0)

    def test_posicionar_embarcacao_valida(self):
        valido = posicao_valida(self.jogador.tabuleiro, (0, 0), 'horizontal', self.embarcacao.tamanho)
        self.assertTrue(valido)
        sucesso = posicionar_embarcacao(self.jogador, self.embarcacao, (0, 0), 'horizontal')
        self.assertTrue(sucesso)
        self.assertIn((0,0), self.embarcacao.posicoes)

    def test_ataque_e_status_embarcacao(self):
        posicionar_embarcacao(self.jogador, self.embarcacao, (0, 0), 'horizontal')
        resultado = realizar_jogada(self.jogador, (0, 0))
        self.assertIn(resultado, ['acertou', 'afundou'])
        self.assertGreaterEqual(self.embarcacao.ataques_recebidos, 1)

if __name__ == "__main__":
    unittest.main()
