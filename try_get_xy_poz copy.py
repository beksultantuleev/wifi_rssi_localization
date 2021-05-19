from rssi_module.rssi import RSSI_Localizer, RSSI_Scan
from rssi_module import rssi
import numpy as np


interface = 'wlo1'  # wlo1
rssi_scanner = rssi.RSSI_Scan(interface)
# ssids = ['unitn-x']
ssids = ['VIVO HOTSPOT', "Xperia mini", "Xperia xzp"]

# all ap info
ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

# print(f"all APS>>> {ap_info}")

"Localizer"

accessPoint = {
    'signalAttenuation': 3,
    'location': {
        'y': 0,
        'x': 0
    },
    'reference': {
        'distance': 3,
        'signal': -44
    },
    'name': 'xzp'
}

# accessPoints = [{
#     'signalAttenuation': 3,
#     'location': {
#         'y': 0,
#         'x': 0
#     },
#     'reference': {
#         'distance': 1,
#         'signal': -34
#     },
#     'name': 'VIVO HOTSPOT'
# },
#     {
#         'signalAttenuation': 4,
#         'location': {
#             'y': 0,
#             'x': 2
#         },
#         'reference': {
#             'distance': 1,
#             'signal': -32
#         },
#         'name': 'Xperia mini'
# }]


# accessPoints = [{
#     'signalAttenuation': 3,
#     'location': {
#         'y': 0,
#         'x': 1
#     },
#     'reference': {
#         'distance': 4,
#         'signal': -50
#     },
#     'name': 'dd-wrt'
# },
#     {
#         'signalAttenuation': 4,
#         'location': {
#             'y': 1,
#             'x': 7
#         },
#         'reference': {
#             'distance': 3,
#             'signal': -41
#         },
#         'name': 'ucrwpa'
# }]

# accessPoints = [{
#     'signalAttenuation': 3,
#     'location': {
#         'y': 2,
#         'x': 2
#     },
#     'reference': {
#         'distance': 1,
#         'signal': -41
#     },
#     'name': 'Xzp'
# },
#     {
#         'signalAttenuation': 4,
#         'location': {
#             'y': 2,
#             'x': 0
#         },
#         'reference': {
#             'distance': 1,
#             'signal': -43
#         },
#         'name': 'mini'
# }, {
#         'signalAttenuation': 4,
#         'location': {
#             'y': 0,
#             'x': 2
#         },
#         'reference': {
#             'distance': 1,
#             'signal': -40
#         },
#         'name': 'vivo'
# }]

# change according to needs (1 or several aps)
# rssi_localizer_instance = RSSI_Localizer(accessPoints=accessPoints)

# apNodes = RSSI_Localizer.getDistancesForAllAPs(
#     rssi_localizer_instance, [-44, -32, -63])  # for mult aps
distance = RSSI_Localizer.getDistanceFromAP(accessPoint, -48)  # for single ap
print(f"\n this is distance of apNODE >>>{distance}")
print(ap_info)
# my fix here


def createMatrices(accessPoints):
    count = len(accessPoints)
    # Sets up that te matrics only go as far as 'n-1' rows,
    # with 'n being the # of access points being used.
    n_count = count-1
    # initialize 'A' matrix with 'n-1' ranodm rows.
    a = np.empty((n_count, 2))
    # print(f"this is a {a}")
    # initialize 'B' matrix with 'n-1' ranodm rows.
    b = np.empty((n_count, 1))
    # print(f"this is b {a}")
    # Define 'x(n)' (x of last accesspoint)
    x_n = accessPoints[n_count]['x']
    print(f"this is xn >>{x_n}")
    # Define 'y(n)' (y of last accesspoint)
    y_n = accessPoints[n_count]['y']
    # Define 'd(n)' (distance from of last accesspoint)
    d_n = accessPoints[n_count]['distance']
    # Iteration through accesspoints is done upto 'n-1' only
    for i in range(n_count):
        ap = accessPoints[i]
        x, y, d = ap['x'], ap['y'], ap['distance']
        a[i] = [2*(x-x_n), 2*(y-y_n)]
        b[i] = [(x**2)+(y**2)-(x_n**2)-(y_n**2)-(d**2)+(d_n**2)]
    return a, b


# print(createMatrices(apNodes))
# a, b = createMatrices(apNodes)


def computePosition(a, b):
    # Get 'A_transposed' matrix
    at = np.transpose(a)
    # Get 'A_transposed*A' matrix
    at_a = np.matmul(at,a) #before
    # a_at = np.matmul(a, at)  # after
    # Get '[(A_transposed*A)^-1]' matrix
    inv_at_a = np.linalg.inv(at_a) #before
    # inv_a_at = np.linalg.inv(a_at)  # after
    # Get '[A_transposed*B]'
    at_b = np.matmul(at, b) #before
    # at_b = np.matmul(at, b)  # after
    # Get '[(A_transposed*A)^-1]*[A_transposed*B]'
    # This holds our position (xn,yn)
    x = np.matmul(inv_at_a, at_b) #before
    # x = np.matmul(inv_a_at, at_b)  # after
    return x


# print(computePosition(a, b))
# end of fixing

# print(np.linalg.inv([[4,0], [1,2]]))

"self localization"
# rssi_values = [ap['signal'] for ap in ap_info]
# # print(rssi_values)
# distance = RSSI_Localizer.getDistancesForAllAPs(rssi_localizer_instance, rssi_values) #for mult aps
# print(f"\n this is distance >>>{distance}")
# position = rssi_localizer_instance.getNodePosition(rssi_values)
# print(position)
