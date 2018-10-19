# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Models.TrainTestBinaryEvaluator
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def models_traintestbinaryevaluator(
        training_data,
        testing_data,
        nodes,
        inputs_subgraph=0,
        outputs_subgraph=0,
        predictor_model=None,
        warnings=None,
        overall_metrics=None,
        per_instance_metrics=None,
        confusion_matrix=None,
        **params):
    """
    **Description**
        Train test for binary classification

    :param training_data: The data to be used for training (inputs).
    :param testing_data: The data to be used for testing (inputs).
    :param nodes: The training subgraph (inputs).
    :param inputs_subgraph: The training subgraph inputs (inputs).
    :param outputs_subgraph: The training subgraph outputs (inputs).
    :param predictor_model: The trained model (outputs).
    :param warnings: Warning dataset (outputs).
    :param overall_metrics: Overall metrics dataset (outputs).
    :param per_instance_metrics: Per instance metrics dataset
        (outputs).
    :param confusion_matrix: Confusion matrix dataset (outputs).
    """

    entrypoint_name = 'Models.TrainTestBinaryEvaluator'
    inputs = {}
    outputs = {}

    if training_data is not None:
        inputs['TrainingData'] = try_set(
            obj=training_data,
            none_acceptable=False,
            is_of_type=str)
    if testing_data is not None:
        inputs['TestingData'] = try_set(
            obj=testing_data,
            none_acceptable=False,
            is_of_type=str)
    if nodes is not None:
        inputs['Nodes'] = try_set(
            obj=nodes,
            none_acceptable=False,
            is_of_type=list)
    if inputs_subgraph is not None:
        inputs['Inputs'] = try_set(
            obj=inputs_subgraph,
            none_acceptable=False,
            is_of_type=dict,
            field_names=['Data'])
    if outputs_subgraph is not None:
        inputs['Outputs'] = try_set(
            obj=outputs_subgraph,
            none_acceptable=False,
            is_of_type=dict,
            field_names=['Model'])
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)
    if warnings is not None:
        outputs['Warnings'] = try_set(
            obj=warnings, none_acceptable=False, is_of_type=str)
    if overall_metrics is not None:
        outputs['OverallMetrics'] = try_set(
            obj=overall_metrics, none_acceptable=False, is_of_type=str)
    if per_instance_metrics is not None:
        outputs['PerInstanceMetrics'] = try_set(
            obj=per_instance_metrics, none_acceptable=False, is_of_type=str)
    if confusion_matrix is not None:
        outputs['ConfusionMatrix'] = try_set(
            obj=confusion_matrix, none_acceptable=False, is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint