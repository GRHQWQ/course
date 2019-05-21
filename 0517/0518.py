import numpy as np 
np_data = np.arange(6).reshape((2,3))
print(np_data)


import torch 
torch_data = torch.from_numpy(np_data)
# torch_data = torch.Tensor(np_data)
print(torch_data)

torch_data = torch_data.numpy()
print(torch_data)
