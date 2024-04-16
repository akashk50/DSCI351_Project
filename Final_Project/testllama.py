import torch
from llama.model import Transformer, ModelArgs

import torch.distributed as dist
import os

api_key = "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"

def setup(rank, world_size):
    """
    Initialize the distributed environment.
    """
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12345'
    # Initialize the process group
    dist.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    """
    Clean up the distributed environment.
    """
    dist.destroy_process_group()


from llama.model import Transformer, ModelArgs

def main():
    # Assuming a single-process setup for simplicity
    rank = 0
    world_size = 1
    setup(rank, world_size)
    
    try:
        params = ModelArgs(
            dim=4096,
            n_layers=32,
            n_heads=32,
            vocab_size=50257,
            max_seq_len=2048
        )
        transformer_model = Transformer(params)
        print("Model initialized successfully.")
    except Exception as e:
        print(f"Error initializing the model: {e}")
    finally:
        cleanup()

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
