# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
RegressionStacking
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def regression_stacking(
        validation_dataset_proportion=0.3,
        **params):
    """
    **Description**
        None

    :param validation_dataset_proportion: The proportion of instances
        to be selected to test the individual base learner. If it is
        0, it uses training set (settings).
    """

    entrypoint_name = 'RegressionStacking'
    settings = {}

    if validation_dataset_proportion is not None:
        settings['ValidationDatasetProportion'] = try_set(
            obj=validation_dataset_proportion,
            none_acceptable=True,
            is_of_type=numbers.Real)

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleRegressionOutputCombiner')
    return component