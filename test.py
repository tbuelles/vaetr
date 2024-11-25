import torch

device = torch.device("cpu")
if torch.backends.mps.is_available():
    device = torch.device("mps")
print(f"Device: {device}")
