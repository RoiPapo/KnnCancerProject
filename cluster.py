class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id  # number of the cluster
        self.cluster_samples = []  # list of samples
        self.cluster_samples.append(samples)  # string
        self.print_sample_array = []

    def merge(self, other):
        """
        :param other: a cluster
        :return: merged clusters by the minimal number of the two clusters
        """
        if self.c_id < other.c_id:
            # self.cluster_samples = list(set(self.cluster_samples) | set(other.cluster_samples))
            self.cluster_samples.extend(other.cluster_samples)
            return other.c_id
        else:
            # other.cluster_samples = list(set(self.cluster_samples) | set(other.cluster_samples))
            other.cluster_samples.extend(self.cluster_samples)
            return self.c_id

    def compute_purity(self):
        """

        :return: the purity measurement
        """
        tag_occurrences_data = {'BRCA': 0, 'KIRC': 0, 'COAD': 0, 'LUAD': 0, 'PRAD': 0}
        for sample in self.cluster_samples:
            tag_occurrences_data[sample.label] += 1

        # Purity = (the dominant label)/(cluster size)
        self.dominant_label = max(tag_occurrences_data, key=tag_occurrences_data.get)
        return (tag_occurrences_data[self.dominant_label]) / (len(self.cluster_samples))

    def __str__(self):
        """
        :return: print the cluster data (sample, dominant label, purity)
        """
        self.purity = self.compute_purity()
        for sample in self.cluster_samples:
            self.print_sample_array.append(sample.s_id)
        self.print_sample_array.sort()
        return 'Cluster {self.c_id}: {self.print_sample_array}, dominant label: {self.dominant_label}, purity: {self.purity}'.format(
            self=self)
        # print("Cluster " + self.c_id, end=' ')
        # print(self.samples, end='')
        # print(", dominant label: " + self.dominant_label, end=' ')
        # print(", purity:", end=' ')
        # print(self.compute_purity())
