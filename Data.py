import pandas as pd
from sample import Sample


class Data:
    def __init__(self, path):
        df = pd.read_csv(path).T
        # df = pd.read_csv(path)
        self.data = df.to_dict(orient="list")


    def create_samples(self):
        """
        :return: a List of objects form class Sample. Contains all samples that appear under 'sample' column the dataset
        """
        sample_list = list()
        for key, value in self.data.items():
            value.pop(0)
            label = value.pop()
            sample_list.append(Sample(key, value, label))

        return sample_list

