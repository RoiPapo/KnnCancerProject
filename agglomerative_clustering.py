from cluster import Cluster
from link import SingleLink


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link  # {Single Link, Complete Link}
        self.samples = samples  # a List of objects of class Sample
        self.distance_map = [[0 for x in range(50)] for y in range(49)]

    def fill_distance_mat(self):
        # for isample in self.samples:
        #     for jsample in self.samples:
        #         if self.samples.index(jsample) > self.samples.index(isample):
        #             self.distance_map[isample.s_id][jsample.s_id] = isample.compute_euclidean_distance(jsample)
        for i in range(len(self.samples) - 1):
            for j in range(i + 1, len(self.samples)):
                self.distance_map[self.samples[i].s_id][self.samples[j].s_id] = self.samples[
                    i].compute_euclidean_distance(
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
            # for icluster in cluster_list:
            #    for jcluster in cluster_list:
            #        if cluster_list.index(jcluster) > cluster_list.index(icluster):
            #            current_distance = SingleLink.compute(None, icluster, jcluster, self.distance_map)
            #            if current_distance < min_distances:
            #                min_distances = current_distance
            #                index_of_best_distance = (cluster_list.index(icluster), cluster_list.index(jcluster))
            for i in range(len(cluster_list) - 1):
                for j in range(i + 1, len(cluster_list)):
                    current_distance = SingleLink.compute(None, cluster_list[i], cluster_list[j],
                                                          self.distance_map)
                    if current_distance < min_distances:
                        min_distances = current_distance
                        index_of_best_distance = (i, j)
            index1, index2 = index_of_best_distance
            item_to_delete = cluster_list[index1].merge(cluster_list[index2])
            # item_to_delete = cluster_list[min(index_of_best_distance)].merge(cluster_list[max(index_of_best_distance)])
            cluster_list = list(filter(lambda c: c.c_id is not item_to_delete, cluster_list))
            # if cluster_list[max(index_of_best_distance)].c_id == item_to_delete:
            #     cluster_list.remove(cluster_list[max(index_of_best_distance)])
            # elif cluster_list[min(index_of_best_distance)].c_id == item_to_delete:
            #     cluster_list.remove(cluster_list[min(index_of_best_distance)])
            min_distances = float('inf')
        return cluster_list
