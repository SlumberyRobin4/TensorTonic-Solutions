import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    #convert input (x) to float tensors
    x = torch.tensor(x, dtype = torch.float32)
    
    if op == 'flatten':
        return torch.flatten(x).tolist()
    elif op == 'squeeze':
        return x.squeeze().tolist()
    else:
        return torch.transpose(x, 0, 1).tolist()
