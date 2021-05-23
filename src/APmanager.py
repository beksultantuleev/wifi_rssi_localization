
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

    def add_anchor_ap(self, attenuation, x, y, distance, signal, name, mac):
        ap = {
            'signalAttenuation': attenuation,
            'location': {
                'y': y,
                'x': x
            },
            'reference': {
                'distance': distance,
                'signal': signal
            },
            'name': name,
            "mac" : mac
        }
        self.list_of_aps.append(ap)
        # if len(self.list_of_aps) > 1:
        self.sorted_list_of_aps = sorted(
            self.list_of_aps, key=self.sortkeypicker(["mac"]))

    # def add_ap_to_list(self, ap):
    #     self.list_of_aps.append(ap)

    def get_ap_list(self):
        return self.list_of_aps

    def get_sorted_ap_list(self):
        return self.sorted_list_of_aps

if __name__ == "__main__":
    test = APmanager()
    test.add_anchor_ap(3, 0, 1, 5, -54, "V", "this is mac")
    test.add_anchor_ap(4, 1, 2, 5, -65, "C", "no this is mac")
    print("not sorted")
    print(test.get_ap_list())
    print("sorted")
    print(test.get_sorted_ap_list())
