import math
import png

def dot(array1, array2):
    sum = 0
    for idx, val in enumerate(array1):
        sum = sum + (array1[idx] * array2[idx])
    return sum

def length(array):
    sum = 0
    for val in array:
        sum = sum + (val * val)
    return math.sqrt(sum)

class Instance:
    def __init__(self, classification):
        self.classification = classification
    def set_features(self, features):
        self.features = features
    def euclidean_distnace(self, instance):
        sum = 0
        for idx, val in enumerate(instance.features):
            sum = sum + (instance.features[idx] * self.features[idx])
        return math.sqrt(sum)
    def angle_distance(self, instance):
        dotprod = dot(self.features, instance.features)
        a = length(self.features)
        b = length(instance.features)
        angle = math.acos(dotprod/(a * b))
        return angle

    def out(self, filename):
        size = int(math.sqrt(len(self.features)))
        print size
        rows = []
        for i in range(0, size):
            rows.append(self.features[size*i:size*(i+1)])
        print self.features
        f = open("output/" + filename, 'wb')
        w = png.Writer(width=28, height=28, greyscale=True, bitdepth=8)
        w.write(f, rows)
        f.close()