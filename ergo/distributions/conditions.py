from abc import ABC, abstractmethod
from dataclasses import dataclass


class Condition(ABC):
    @abstractmethod
    def loss(self, dist):
        ...


@dataclass
class PercentileCondition(Condition):
    percentile: float
    value: float

    def __init__(self, percentile, value):
        if not 0 <= percentile <= 1:
            raise ValueError(f"Percentile should be in 0..1, got {percentile}")
        self.percentile = percentile
        self.value = value

    def loss(self, dist):
        actual_percentile = dist.cdf(self.value)
        return (actual_percentile - self.percentile) ** 2

    def __str__(self):
        return f"There is a {round(self.percentile * 100)}% chance that the value is <{self.value}"