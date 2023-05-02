import numpy as np

__version__ = "1.0"


def prediction_strength(train_labels, test_labels):
    """Computes the prediction strength of a clustering.

    Args:
        train_labels: A list of test labels predicted on training clusters.
        test_labels: A list of test labels predicted on test clusters.

    Returns:
        A float representing the prediction strength of the clustering.
    """

    number_of_clusters = np.unique(train_labels).size
    size = train_labels.size

    train_labels = train_labels.reshape(-1, 1)
    train_similarity_matrix = np.tile(train_labels, size) == train_labels.T
    np.fill_diagonal(train_similarity_matrix, False)

    test_labels = test_labels.reshape(-1, 1)
    test_similarity_matrix = np.tile(test_labels, size) == test_labels.T

    D_matrix = train_similarity_matrix == test_similarity_matrix

    prediction_strength = []
    for i in range(number_of_clusters):
        mask = (test_labels == i).reshape(-1, 1)
        n = np.sum(mask)
        if n == 1:
            return 0
        prediction_sum = np.sum(D_matrix[mask, :][:, mask])
        prediction_strength.append(prediction_sum / (n * (n - 1)))

    return np.min(prediction_strength)
