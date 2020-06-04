import math


class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id  # number of sample (ex. sample_5 id == 5)
        self.genes = genes  # list of genes values
        self.label = label  # string

    def compute_euclidean_distance(self, other):
        """
        :param other: an object from class Sample
        :return: the euclidean distance between s_id and other
        """
        # Euclidean distance: dist(x, y) = ||x-y|| = sqrt(sum(_(i=1)^n (xi-yi)^2)) (x and y are SAMPLES)
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self.genes, other.genes)]))
        # distance = 0
        # for i in range(len(self.genes)):
        #     distance += math.pow((self.genes[i] - other.genes[i]), 2)
        #
        # distance = math.pow(distance, 0.5)
        return distance
