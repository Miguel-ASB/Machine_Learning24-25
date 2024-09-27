import torch

my_tensor = torch.tensor([[4.0,1.0],[5.0,3.0],[6.0,2.0]])

print(my_tensor[:])
print(my_tensor[1:])
print(my_tensor[1:,:]) #recomendable
print(my_tensor[0,:])
print(my_tensor[-1,0])

