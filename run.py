#!/usr/bin/env python

from instance import Instance


num_test_instances = 50

train_intances = []
test_intances = []
k = 5

f = open("data/train.csv",'r')
is_first_row = True
i = 0

print "parsing.."

temp_instances = []
for line in f:
    if(is_first_row):
        is_first_row = False;
        continue
    elements = line.split(',')
    inst = Instance(int(elements[0]))
    features = []
    for element in (elements[1:]):
        value = int(element)
        features.append(value)
    inst.set_features(features)
    temp_instances.append(inst)
    i = i + 1

train_intances = temp_instances[:2000]
test_intances = temp_instances[-num_test_instances:]

print "done."


print len(test_intances)
print len(train_intances)


num_correct = 0
total = 0
for i in range(0, len(test_intances)):
    print i
    test_element = test_intances[i]
    closest = []
    for intance in train_intances:
        distance = test_element.angle_distance(intance)
        closest.append((distance, intance));
        closest = sorted(closest, key = lambda x: x[0])
        closest = closest[:k]

    votes = [0] * 10
    for j in range(0, len(votes)):
        votes[j] = 0
    for instance in closest:
        votes[instance[1].classification] += 1
    topVote = 0
    for j in range(0, len(votes)):
        if(votes[j] > votes[topVote]):
            topVote = j

    total += 1
    if(topVote == test_element.classification):
        num_correct += 1
    else:
        test_element.out("incorrect%d.png" % (i))
    print str(topVote) + " -> " + str(test_element.classification)

print "accuracy: %f" % (float(num_correct) / float(total))
