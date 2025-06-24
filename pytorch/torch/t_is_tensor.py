import torch

t = torch.tensor([1, 2, 3])  # This will create a tensor from the list [1, 2, 3]
# The function to check if an object is a tensor
print(torch.is_tensor(t))
typ= t.storage()
print(type(typ))  # This will print the type of t, which should be <class 'torch.Tensor'>
print(torch.is_storage(t.storage()))  # This will check if t is a storage object
print(torch.is_complex(t))
print(torch.is_conj(t))  # This checks if the storage of t is conjugate