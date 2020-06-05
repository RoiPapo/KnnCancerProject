from cluster import Cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link  # {Single Link, Complete Link}
        self.samples = samples  # a List of objects of class Sample
        self.distance_map = [[0 for x in range(300)] for y in range(299)]

    def fill_distance_mat(self):
        for i in range(len(self.samples) - 1):
            for j in range(i + 1, len(self.samples)):
                self.distance_map[self.samples[i].s_id][self.samples[j].s_id] = self.samples[
                    i].compute_euclidean_distance(
                    self.samples[j])

    def make_initial_clusters(self):
        cluster_list = []
        for sample in self.samples:
            cluster_list.append(Cluster(sample.s_id, sample))
        return cluster_list

    def run(self, max_clusters):
        """
        :param max_clusters: INTEGER indicating the maximum number of clusters
        :return: runs the cluster algorithm such that the for [max_clusters] clusters
        """
        cluster_list = self.make_initial_clusters()
        self.fill_distance_mat()
        while len(cluster_list) > max_clusters:
            min_distances = float('inf')
            for i in range(len(cluster_list) - 1):
                for j in range(i + 1, len(cluster_list)):
                    current_distance = self.link.compute(None, cluster_list[i], cluster_list[j],
                                                          self.distance_map)
                    if current_distance < min_distances:
                        min_distances = current_distance
                        index_of_best_distance = (i, j)
            index1, index2 = index_of_best_distance
            item_to_delete = cluster_list[index1].merge(cluster_list[index2])
            cluster_list = list(filter(lambda c: c.c_id is not item_to_delete, cluster_list))
        return cluster_list
