import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    numparr = np.array(list).reshape(3, 3)

    #calculating the values
    mean = [numparr.mean(axis=0).tolist(), numparr.mean(axis=1).tolist(), numparr.mean()]
    variance = [numparr.var(axis=0).tolist(), numparr.var(axis=1).tolist(), numparr.var()]
    std = [numparr.std(axis=0).tolist(), numparr.std(axis=1).tolist(), numparr.std()]
    maxim = [numparr.max(axis=0).tolist(), numparr.max(axis=1).tolist(), numparr.max()]
    minim = [numparr.min(axis=0).tolist(), numparr.min(axis=1).tolist(), numparr.min()]
    total = [numparr.sum(axis=0).tolist(), numparr.sum(axis=1).tolist(), numparr.sum()]

    #creating the dictionary
    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": std,
        "max": maxim,
        "min": minim,
        "sum": total
    }
    
    return calculations