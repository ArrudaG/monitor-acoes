from src.services.acao_service import AcaoService
from src.services.notificacao_service import NotificacaoService

def test_retorno_ticker():
    resultado = NotificacaoService.obter_tickers()
    assert resultado is not None
    assert isinstance(resultado, list)

def test_buscar_diario():
    ticker = NotificacaoService.obter_tickers()
    resultado = AcaoService.buscar_diario(ticker)
    assert resultado is not None