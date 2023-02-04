# from hate.pipeline.train_pipeline import TrainPipeline

# if __name__ == "__main__":
#     TrainPipeline().run_pipeline()

from hate.pipeline.prediction_pipeline import PredictionPipeline

if __name__ == "__main__":
    PredictionPipeline().run_pipeline(text="you are good")

# import pandas as pd

# data = pd.read_csv("artifacts/12_06_2022_11_55_37/DataTransformationArtifacts/final.csv")
# print(data)

