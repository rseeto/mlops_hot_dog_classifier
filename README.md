# MLOps/Hot Dog Classifier
## Project Organization Summary
    ├── README.md
    ├── requirements.txt
    ├── LICENSE.txt    
    ├── data
    │   ├── intermediary
    │   │   ├── food
    │   │   ├── hard taco
    │   │   ├── hot dog
    │   │   ├── open face sandwich
    │   │   └── taco
    │   ├── processed
    │   │   ├── baseline.tfrecord
    │   │   └── taco_bias.tfrecord
    │   └── raw
    │       ├── food
    │       ├── hard taco
    │       ├── hot dog
    │       ├── open face sandwich
    │       └── taco
    ├── mlops_hot_dog_classifier
    │   ├── data
    │   │   └── download_images.py
    │   └── __init__.py
    ├── models
    │   ├── baseline_model
    │   │   ├── assets
    │   │   ├── variables
    │   │   ├── keras_metadata.pb
    │   │   └── saved_model.pb
    │   └── taco_bias
    │       ├── assets
    │       ├── variables
    │       ├── keras_metadata.pb
    │       └── saved_model.pb
    └── notebooks
        ├── 1.0-data-prep.ipynb
        ├── 2.0-pipeline-interactive.ipynb
        ├── 2.1-pipeline-airflow.ipynb
        └── 3.0-results.ipynb
* File structure is truncated for brevity

## Description
This project was meant to answer the question 'Is a hot dog a taco or a sandwich?' while incorporating deep learning TensorFlow Extended production pipeline techniques. The goal of this project was to train a model to classify tacos, sandwiches, and miscellaneous food. From a Bayesian perspective, the trained model could then be used to predict if an image of a hot dog was most like a taco or sandwich based on the magnitude of the prediction. The Keras model was a relatively simplistic image classification model incorporating transfer learning; however, the emphasis was on learning to develop production level TensorFlow Extended pipelines and not necessarily on the model itself.

The notebook [1.0-data-prep.ipynb](notebooks/1.0-data-prep.ipynb) details the data preparation process. In short, three hundred images of tacos, sandwiches, and miscellaneous food were manually reviewed, interleaved, and processed into a baseline data set. Another data set containing open face sandwich, hard tacos and miscellaneous food was created. This data set was referred to as a taco bias data set as it was believed that the curvature of the hard tacos mimicked the curvature of a hot dog bun and the resulting model would predict that hot dogs were more similar to tacos.

The notebook [2.0-pipeline-interactive.ipynb](notebooks/2.0-pipeline-interactive.ipynb) outlines the creation of an interactive TensorFlow Extended pipeline to train an image classification pipeline. The pipeline contained the `ExampleGen`, `StatisticsGen`, `SchemaGen`, `ExampleValidator`, `Transform`, `Trainer`, `Evaluator`, and `Pusher` components. Transfer learning was used with `EfficientNetB0` as the base model. The `Transform` component resized the image to 224 by 224. The `Trainer` component used transfer learning with `EfficientNetB0` as the base model. The model was trained on the baseline data set.

The notebook [2.1-pipeline-airflow.ipynb](notebooks/2.1-pipeline-airflow.ipynb) outlines the a similar pipeline to the interactive pipeline but using Airflow as an orchestrator. The model was initially trained on the baseline data set. This model also integrated Airflow's scheduling capabilities by incorporating the taco bias data set to simulate a pipeline with continuous training.

The interactive pipeline produced a model trained just with the baseline data while the Airflow pipeline produced a model trained with the taco bias data set. The notebook [3.0-results.ipynb](notebooks/3.0-results.ipynb) used each model to predict whether an image of a hot dog was classified as a taco, sandwich, or miscellaneous food. On a set of 400 hot dogs, the baseline model predicts the average hot dog is 23.8% food, 41.7% sandwich, and 34.5% taco while the taco bias model predicts the average hot dog is 17.9% food, 76.0% sandwich, and 6.1% taco. The results would indicate that a hot dog is a sandwich according to our deep learning models.

## Technologies
Project is created with:
* Python version: 3.9.0
    * Tensorflow/Keras (TFRecord), TensorFlow Extended
* Airflow

## License
[MIT](LICENSE.txt)

## References
* [TFX Keras Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components_keras)
* [TFX Airflow Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop)
* [Building Machine Learning Pipelines](https://www.amazon.com/Building-Machine-Learning-Pipelines-Automating/dp/1492053198/ref=sr_1_1?crid=2BHDWBBKHI7FH&keywords=tfx+pipeline&qid=1661279339&rnid=2941120011&s=books&sprefix=tfx+pipeline%2Caps%2C105&sr=1-1)
