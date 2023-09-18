class IP:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return ".".join((str(self.a), str(self.b), str(self.c), str(self.d)))

    def __and__(self, other):
        return IP(self.a & other.a, self.b & other.b, self.c & other.c, self.d & other.d)

    def __or__(self, other):
        return IP(self.a | other.a, self.b | other.b, self.c | other.c, self.d | other.d)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def to_bin(self):
        return ".".join(
            (bin(self.a)[2:].zfill(8), bin(self.b)[2:].zfill(8), bin(self.c)[2:].zfill(8), bin(self.d)[2:].zfill(8)))


class Network:
    def __init__(self, ip: IP, n: int):
        self.network_ip = ip

        mask_ip_int = int((n * "1").ljust(32, "0"), 2)
        lst = []
        for i in range(4):
            lst.insert(0, mask_ip_int % 256)
            mask_ip_int //= 256
        self.mask_ip = IP(*lst)
        self.network_ip &= self.mask_ip

        lst = [255 - x for x in lst]
        self.broadcast_ip = self.network_ip | IP(*lst)

    def __contains__(self, item: IP):
        return item & self.mask_ip == self.network_ip


ip1 = IP(192, 168, 186, 227)      # IP d'une machine sur un réseau
print(ip1.to_bin())             # affiche l'IP en binaire

n = Network(ip1, 29)            # réseau avec la machine, 20 bits fixe

print(n.mask_ip.to_bin())       # affiche le masque en binaire
print(n.mask_ip)                # puis en décimal
print(n.network_ip.to_bin())    # IP du réseau en binaire
print(n.network_ip)             # puis en décimal
print(n.broadcast_ip.to_bin())  # IP de broadcast en binaire
print(n.broadcast_ip)           # puis en décimal
ip2 = IP(192, 168, 186, 240)
print(ip2 in n)
              # ip3 est-elle sur le réseau ?

