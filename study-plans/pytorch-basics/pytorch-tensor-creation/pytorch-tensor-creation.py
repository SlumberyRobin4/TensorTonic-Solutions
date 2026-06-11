import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == 'full':
        return torch.full(shape, value).tolist()
    elif method == 'zeros':
        return torch.zeros(shape).tolist()
    else:
        return torch.ones(shape).tolist()