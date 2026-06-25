import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    #turn values into a tensor with requires_grad = True so the graph is recorded
    x = torch.tensor(values, dtype = torch.float32, requires_grad = True)

    #define y vector
    y_vector = (x**3) + (2*x)
    
    #compute y as a scalar
    y = y_vector.sum()

    #backpropagate
    y.backward()

    #return list of x gradient
    return x.grad.tolist()