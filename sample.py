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
        return distance
