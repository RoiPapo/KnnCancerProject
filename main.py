import sys
from Data import Data
from agglomerative_clustering import AgglomerativeClustering
from link import SingleLink, CompleteLink


def main(argv):
    path = argv[1]
    genes_data = Data(path)
    sample_list = genes_data.create_samples()
    single_agro_clustering = AgglomerativeClustering(SingleLink, sample_list)
    complete_agro_clustering = AgglomerativeClustering(CompleteLink, sample_list)
    single_final_clusters = single_agro_clustering.run(int(argv[3]))
    Complete_final_clusters = complete_agro_clustering.run(int(argv[3]))
    missions_to_print = argv[2].split(", ")
    general_printer(missions_to_print, single_final_clusters, Complete_final_clusters)


def general_printer(missions_to_print, single_final_clusters, Complete_final_clusters):
    """
    /just prints
    :param missions_to_print: single complete or both
    """
    if "Single_Link" in missions_to_print:
        print("Single Link:")
        for cluster in single_final_clusters:
            print(cluster)
        print("\n")
    if "Complete_Link" in missions_to_print:
        print("Complete Link:")
        for cluster in Complete_final_clusters:
            print(cluster)


if __name__ == '__main__':
    main(sys.argv)