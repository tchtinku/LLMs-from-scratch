import pytest
from gpt_train import main
import http.client
from urllib.parse import urlparse


@pytest.fixture
def gpt_config():
    return {
        "vocab_size": 50257,
        "context_length": 12, # small for testing efficiency
        "emb_dim": 32,    # small for testing efficiency
        "n_heads": 4,     # small for testing efficiency
        "n_layers": 2,     # small for testing efficiency
        "drop_rate": 0.1,
        "qkv_bias": False
    }
    
@pytest.fixture
def other_settings():
    return {
        "learning_rate": 5e-4,
        "num_epochs": 1,    # small for testing efficiency
        "batch_size": 2,
        "weight_decay": 0.1
    }
    
def test_main(gpt_config,)