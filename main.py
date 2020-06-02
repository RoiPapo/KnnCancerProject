from sample import Sample
from cluster import Cluster
from Data import Data
from agglomerative_clustering import AgglomerativeClustering


def main():
    # path = argv[1]
    # features = argv[2]
    path = "hw3_sample_input.csv"
    sample1 = Sample(3, [12, 2, 3], "hi")
    genes_data = Data(path)
    sample_list = genes_data.create_samples()
    single_agro_clustering= AgglomerativeClustering("single",sample_list)
    final_clusters= single_agro_clustering.run(5)
    for cluster in final_clusters:
        print(cluster)
    cluster1 = Cluster(3, sample1)



if __name__ == "__main__":
    main()
