"""systems_model = engine.SystemsModel(aviation.transforms).

required_global_fleet = systems_model.evaluate (inputs, output)
"""

import collections.abc
import typing

from aviation._model import Transform


class SystemsModel:
    def __init__(
        self, transforms: collections.abc.Sequence[Transform[typing.Any, ...]]
    ) -> None:  # sequences are homogeneous - all items in a sequnece need to be of the same type
        self.transforms = set(
            transforms
        )  # systems_model.transforms <-- now has this attribute, cast as a set

    def evaluate(self, inputs: dict[str, typing.Any], output: str) -> typing.Any:  # noqa: ANN401
        # if the requested `output` has already been supplied as an input then this can just be returned directy without any need for computation
        if output in inputs:
            return inputs[output]
        # the requested output isn't in inputs so it muist be the name of a tranform in `self.transforms``. If it's not found in `self.tranforms` then there muist be an error
        for transform in self.transforms:
            if transform.name == output:
                break
        else:
            # if we cannot find a tranform matching the output , raise an error
            message = f"No transform with name `{output}`."
            raise ValueError(message)

        # to evaluate the `transform`,
        for parameter in transform.parameters:
            if parameter not in inputs:
                inputs[parameter] = self.evaluate(inputs, parameter)

        # evaluate and return the `transform` associated with the passed output
        arguments = {parameter: inputs[parameter] for parameter in transform.parameters}
        return transform(**arguments)
