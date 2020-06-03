from Data import Data
from agglomerative_clustering import AgglomerativeClustering


def main():
    path = "hw3_sample_input.csv"
    genes_data = Data(path)
    sample_list = genes_data.create_samples()
    single_agro_clustering = AgglomerativeClustering("single", sample_list)
    final_clusters = single_agro_clustering.run(5)
    for cluster in final_clusters:
        print(cluster)


if __name__ == "__main__":
    main()
