
class APmanager():
    def __init__(self):
        self.list_of_aps = []
        self.sorted_list_of_aps = []

    def sortkeypicker(self, keynames):
        negate = set()
        for i, k in enumerate(keynames):
            if k[:1] == '-':
                keynames[i] = k[1:]
                negate.add(k[1:])

        def getit(adict):
            composite = [adict[k] for k in keynames]
            for i, (k, v) in enumerate(zip(keynames, composite)):
                if k in negate:
                    composite[i] = -v
            return composite
        return getit

    def add_ap(self, atten, x, y, dist, signal, name):
        ap = {
            'signalAttenuation': atten,
            'location': {
                'y': y,
                'x': x
            },
            'reference': {
                'distance': dist,
                'signal': signal
            },
            'name': name
        }
        self.list_of_aps.append(ap)
        # if len(self.list_of_aps) > 1:
        self.sorted_list_of_aps = sorted(
            self.list_of_aps, key=self.sortkeypicker(["name"]))

    # def add_ap_to_list(self, ap):
    #     self.list_of_aps.append(ap)

    def get_ap_list(self):
        return self.list_of_aps

    def get_sorted_ap_list(self):
        return self.sorted_list_of_aps

if __name__ == "__main__":
    test = APmanager()
    test.add_ap(3, 0, 1, 5, -54, "V")
    test.add_ap(4, 1, 2, 5, -65, "C")
    print("not sorted")
    print(test.get_ap_list())
    print("sorted")
    print(test.get_sorted_ap_list())
