import tabula 
import pandas as pd
import torch                     # for all things PyTorch
import torch.nn as nn            # for torch.nn.Module, the parent object for PyTorch models
import torch.nn.functional as F  # for the activation function

def get_data(file):
    # Read PDF into a list of DataFrames
    dfs = tabula.read_pdf(file, pages="all") 

    # Access the first DataFrame (if there's only one table)
    data = pd.concat(dfs,ignore_index=True)

    return data

def to_tensor(dataframe):
    return torch.from_numpy(dataframe.values[:,1:-1].astype(float))

if __name__ == "__main__":
    data = get_data("D:/Gas/si.pdf")
    print(data)
    torch_data = to_tensor(data)
    print(torch_data)

