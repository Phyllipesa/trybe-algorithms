import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(3, 'b')
    assert encrypt_message('camada', 3) == 'mac_ada'
    assert encrypt_message('camada', 4) == 'ad_amac'
    assert encrypt_message('camada', 9) == 'adamac'
    assert encrypt_message('camada', -1) == 'adamac'
    assert encrypt_message('camada', 5) == 'damac_a'
