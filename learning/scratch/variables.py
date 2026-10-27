bus= "3b"
device = "00"
function_pcie= "1"
pcie_bus = bus + ":"+device + "."+function_pcie
print(pcie_bus)
print(len(pcie_bus))