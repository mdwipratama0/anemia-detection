import tensorflow as tf
import tensorflow_transform as tft

CATEGORICAL_FEATURES = {
    "Gender": 2
}

NUMERICAL_FEATURES = [
    "Hemoglobin",
    "MCH",
    "MCHC",
    "MCV"
]

LABEL_KEY = "Result"


def convert_num_to_one_hot(label_tensor, num_labels=2):
    one_hot_tensor = tf.one_hot(label_tensor, num_labels)
    return tf.reshape(one_hot_tensor, [-1, num_labels])
    
def transformed_name(key):
    return key + '_xf'


def preprocessing_fn(inputs):
    outputs = {}

    for key in CATEGORICAL_FEATURES:
        dim = CATEGORICAL_FEATURES[key]
        int_value = tft.compute_and_apply_vocabulary(
            inputs[key], top_k=dim + 1
        )
        outputs[transformed_name(key)] = convert_num_to_one_hot(
            int_value, num_labels=dim + 1
        )

    for feature in NUMERICAL_FEATURES:
        outputs[transformed_name(feature)] = tft.scale_to_0_1(inputs[feature])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs