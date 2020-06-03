from cluster import Cluster
from link import SingleLink


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link  # {Single Link, Complete Link}
        self.samples = samples  # a List of objects of class Sample
        self.distance_map = [[0 for x in range(50)] for y in range(49)]

    def fill_distance_mat(self):
        for i in range(len(self.samples)-1):
            for j in range(i + 1, len(self.samples)):
                self.distance_map[self.samples[i].s_id][self.samples[j].s_id] = self.samples[i].compute_euclidean_distance(
                    self.samples[j])

    def run(self, max_clusters):
        """
        :param max_clusters: INTEGER indicating the maximum number of clusters
        :return: run the algorithm such that the maximum number of clusters is not bigger than max_clusters
        """

        cluster_list = []
        for sample in self.samples:
            cluster_list.append(Cluster(sample.s_id, sample))

        self.fill_distance_mat()

        min_distances = float('inf')
        while len(cluster_list) > max_clusters:
            for i in range(len(cluster_list) - 1):
                for j in range(i + 1, len(cluster_list)):
                    current_distance = SingleLink.compute(None, cluster_list[i], cluster_list[j],
                                                          self.distance_map)
                    if current_distance < min_distances:
                        min_distances = current_distance
                        index_of_best_distance = {i, j}

            item_to_delete = cluster_list[min(index_of_best_distance)].merge(cluster_list[max(index_of_best_distance)])
            if cluster_list[max(index_of_best_distance)].c_id == item_to_delete:
                cluster_list.remove(cluster_list[max(index_of_best_distance)])
            elif cluster_list[min(index_of_best_distance)].c_id == item_to_delete:
                cluster_list.remove(cluster_list[min(index_of_best_distance)])
            min_distances = float('inf')
        return cluster_list
