from collections import namedtuple

"""we are basically phrasing the requirement for configuration"""

DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

""" 1. Download Url
    2. download folder (compressed file)
    3. extract folder (extracted file)
    4. train dataset folder
    5. test dataset folder
"""

DataValidationConfig = namedtuple("DataValidationConfig",
["schema_file_path"])

"""schema_file_path = here we will define the number of columns, names of columns, no. of rows etc"""

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                    "transformed_train_dir",
                                                                    "transformed_test_dir",
                                                                    "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path", "base_accuracy"])

""" 1. trained_model_file_path = this is the location of pickle file which we create after model training
    2. Base_accuracy = we will specify some accuracy here. if the new model provides better accuracy than the base 
                        accuracy, then the new model is selected.
"""
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path", "time_stamp"])

""" 1. model_evaluation_file_path = we will keep information of all the models available in the production
    2. time_stamp = here timestamp is nothing but the time when we are doing the comparison with the base model """

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])

"""export_dir_path = where we will push the model in production"""