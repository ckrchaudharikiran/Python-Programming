# Base class
class Network:
    def connectivity(self):
        return "Network connects"

# Derived class
class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

# Sub-derived class
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"    

# Creating an instance of Network_5G_Airtel
network_object = Network_5G_Airtel()
print(network_object.connectivity())        # Inherited from Network class
print(network_object.fast_connectivity())   # Inherited from Network_5G class
print(network_object.fast_and_stable_connectivity())   # Inherited from Network_5G_Airtel class



# MRO for Multilevel Inheritance in Python
# Let's consider a scenario from the above example in which the Network_5G class also have a method named connectivity(). Now, What will happen if we call the connectivity() method from the instance of the Network_5G_Airtel class?. This is where the Method Resolution Order (MRO) comes into play.

# Let's modify the previous example to include a connectivity() method in the Network_5G class −
# Base class
# class Network:
#     def connectivity(self):
#         return "Network connects"

# # Derived class
# class Network_5G(Network):
#     def fast_connectivity(self):
#         return "5G Network provides superfast connectivity"

#     def connectivity(self):
#         return "5G Network connects faster"

# # Sub-derived class
# class Network_5G_Airtel(Network_5G):
#     def fast_and_stable_connectivity(self):
#         return "Airtel 5G network is fast and remains stable"

# # Creating an instance of Network_5G_Airtel
# obj1 = Network_5G_Airtel()
# print(obj1.connectivity())  # Inherited from Network class
