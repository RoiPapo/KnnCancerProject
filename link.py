class Link:
    def compute(self, cluster, other, distance_table, distance=None):
        # Abstract method, SingleLink & CompleteLink need to implement this!
        raise NotImplementedError("SingleLink & CompleteLink need to implement the compute() method!")


class SingleLink(Link):
    def compute(self, cluster, other, distance_table, distance=None):
        """

        :param distance_table: table of distances
        :param cluster: object of Cluster type
        :param other: object of Cluster type
        :param distance_table: contains all the distances
        :param distance:
        :return:
        """
        # if distance is None:
        #    distance = float('inf')
        min_distance = float('inf')
        for i in range(len(cluster.cluster_samples)):
            for j in range(len(other.cluster_samples)):
                if cluster.cluster_samples[i].s_id < other.cluster_samples[j].s_id:
                    computation = distance_table[cluster.cluster_samples[i].s_id][other.cluster_samples[j].s_id]
                else:
                    computation = distance_table[other.cluster_samples[j].s_id][cluster.cluster_samples[i].s_id]
            if computation < min_distance:
                min_distance = computation
        return min_distance

        # for sample in cluster.sample_list:
        #     for other_sample in other.sample_list:


class CompleteLink(Link):
    def compute(self, cluster, other, distance=None):
        """
        :param cluster: object of Cluster type
        :param other: object of Cluster type
        :param distance:
        :return:
        """
        distance = 0
        #    for i in range(len(cluster.samples)):
        #        for j in range(len(other.samples)):
        #            computation = cluster.samples[i].compute_euclidean_distance(self, other.samples[j])
        #            if computation > distance:
        #                distance = computation
        return distance
