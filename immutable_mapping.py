from types import MappingProxyType
d = {1:'A'}
m = MappingProxyType(d)
m[1]=23
print(m[1])