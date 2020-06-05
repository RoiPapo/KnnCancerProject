class Link:
    def compute(self, cluster, other, distance_table):
        # Abstract method, SingleLink & CompleteLink need to implement this!
        raise NotImplementedError("SingleLink & CompleteLink need to implement the compute() method!")


class SingleLink(Link):
    def compute(self, cluster, other, distance_table):
        """
        :param cluster: object of Cluster type
        :param other: object of Cluster type
        :param distance_table: contains all the distances
        :return: the shortest distance between 2 points from different cluster
        """
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


class CompleteLink(Link):
    def compute(self, cluster, other, distance_table):
        """
         :param cluster: object of Cluster type
         :param other: object of Cluster type
         :param distance_table: contains all the distances
         :return: the max distance between 2 points from different cluster
         """
        max_distance = 0
        for i in range(len(cluster.cluster_samples)):
            for j in range(len(other.cluster_samples)):
                if cluster.cluster_samples[i].s_id < other.cluster_samples[j].s_id:
                    computation = distance_table[cluster.cluster_samples[i].s_id][other.cluster_samples[j].s_id]
                else:
                    computation = distance_table[other.cluster_samples[j].s_id][cluster.cluster_samples[i].s_id]
                if computation > max_distance:
                    max_distance = computation
        return max_distance
