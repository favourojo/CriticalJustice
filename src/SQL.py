
import chart_studio.plotly as py
from plotly.graph_objs import *
trace1 = {
  "uid": "e59e0e", 
  "name": "Building/Use", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 11842, None, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace2 = {
  "uid": "b46848", 
  "name": "Noise", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 6630, 4328, 2771, 2788, 2665, 4755, 7716, None, None, None, None, None, None, None, None, None, None, None, None, 8724, 10291, 12345, 11874, None]
}
trace3 = {
  "uid": "67c879", 
  "name": "Dirty Conditions", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, None, None, None, None, None, 24481, None, None, None, None, 12348, 10532, None, None, None, None, None], 
  "visible": True
}
trace4 = {
  "uid": "da3ac3", 
  "name": "Sewer", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, 5948, None, None, None, 6576, None, None, 15232, 16196, 16178, 14256, 13486, 13213, 12761, 11141, None, None, 10061, None, None, None, None, None], 
  "visible": True
}
trace5 = {
  "uid": "0f18f1", 
  "name": "Taxi Complaint", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, 1490, 1676, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace6 = {
  "uid": "c695f5", 
  "name": "General Construction/Plumbing", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, None, None, 14899, 15691, 14542, None, 12927, 13667, 11387, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace7 = {
  "uid": "9fa287", 
  "name": "Street Light Condition", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, 12845, 44009, 76667, 82382, 21828, 52730, 51453, 40379, 24158, 9904, 9186, 9380, 10945, 12526, 9097, None, None], 
  "visible": True
}
trace8 = {
  "uid": "603090", 
  "name": "Missed Collection (All Materials)", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, 17009, 13963, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace9 = {
  "uid": "8c5771", 
  "name": "Water System", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, 4035, None, None, 1945, 5427, 9257, 14605, 18638, 19246, 19358, 19221, 18068, 19030, 20480, 21078, 20400, 17487, 15718, 13349, 11109, 8615, None, None], 
  "visible": True
}
trace10 = {
  "uid": "ddf793", 
  "name": "Illegal Parking", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, 1802, 3517, 7463, 11370, None, None, None, None, None, None, None, None, 8769, None, 8703, 9188, 10986, 8838, 7195, None], 
  "visible": True
}
trace11 = {
  "uid": "628823", 
  "name": "Street Condition", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 2736, None, None, None, 2346, 6899, 35215, 29454, 34193, 34529, 29504, 25923, 39173, 52609, 37891, 24564, 17117, 26067, 29566, 9260, 8062, None, 6596, None], 
  "visible": True
}
trace12 = {
  "uid": "99c04f", 
  "name": "Other", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 24963, 20001, 12133, 11277, 15430, 30329, 60150, 143260, 222263, 242672, 244957, 225790, 227665, 218406, 216547, 194797, 151869, 133464, 104735, 94243, 83764, 74412, 57444, None], 
  "visible": True
}
trace13 = {
  "uid": "10597d", 
  "name": "Noise - Vehicle", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 3749, None, 2010, 2284, 1705, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace14 = {
  "uid": "fd2e1a", 
  "name": "Blocked Driveway", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 5471, 3416, 2816, 2875, 4095, 7652, 13432, 17141, 17593, 15573, 14515, 13872, None, 11899, None, 12145, 13125, 14664, 15488, 16770, 17193, 15296, 11664, None], 
  "visible": True
}
trace15 = {
  "uid": "c2a24f", 
  "name": "Noise - Street/Sidewalk", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 8485, 5796, 3797, 3289, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6897, 8956, 12070, 13982, None], 
  "visible": True
}
trace16 = {
  "uid": "fded78", 
  "name": "Sanitation Condition", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, 6707, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace17 = {
  "uid": "395ea3", 
  "name": "Noise - Commercial", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 14817, 9553, 5097, 2458, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 13290, 18779, None], 
  "visible": True
}
trace18 = {
  "uid": "7c28f0", 
  "name": "Damaged Tree", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, None, None, 14250, 13382, 12287, None, None, None, None, None, None, None, None, None, None, None, None], 
  "visible": True
}
trace19 = {
  "uid": "703c33", 
  "name": "Broken Muni Meter", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9712, 9076, None, None, None, None, None, None], 
  "visible": True
}
trace20 = {
  "uid": "a29d51", 
  "name": "Traffic Signal Condition", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, 5142, 3285, 3282, 3787, 3234, 4863, 8932, 14104, 13382, None, None, None, 14962, 33431, 17646, 12326, 10232, None, None, None, None, None, 6165, None], 
  "visible": True
}
trace21 = {
  "uid": "1f5a32", 
  "name": "Graffiti", 
  "type": "bar", 
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
  "y": [None, None, None, None, None, None, None, None, None, None, None, None, None, 15577, None, None, None, None, 11916, None, None, None, None, None, None], 
  "visible": True
}
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20, trace21])
layout = {
  "title": "The 6 Most Common 311 Complaints", 
  "width": 1152, 
  "xaxis": {
    "type": "linear", 
    "range": [0.5, 23.5], 
    "title": "Hour in Day", 
    "autorange": True
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [0, 458912.63157894736], 
    "title": "Number of Complaints", 
    "autorange": True, 
    "showexponent": "last", 
    "exponentformat": "SI"
  }, 
  "height": 472, 
  "legend": {
    "x": 1.0204520990312163, 
    "y": 0.009685230024213076
  }, 
  "barmode": "stack", 
  "autosize": True, 
  "showlegend": True
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)