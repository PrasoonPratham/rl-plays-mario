import torch

# check if GPU is available
if torch.cuda.is_available():
    print("GPU is available")
else:
    print("GPU is not available")

# move a tensor to GPU
x = torch.tensor([1, 2, 3], dtype=torch.float32)
x = x.cuda()

# print the device of the tensor
print(x.device)
