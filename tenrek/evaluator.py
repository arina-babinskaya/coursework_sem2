from enum import Enum
from dataclasses import dataclass
from math import isnan, isinf
from typing import Any


class Verdict(str, Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Threshold:
    green_max: float
    yellow_max: float


class MetricEvaluator:
    """
    Оценивает метрики сложности C++ кода.

    Правило:
    - для большинства метрик меньше = лучше;
    - для maintainability_index больше = лучше;
    - unknown используется для служебных полей, None, NaN и неподдержанных метрик.

    Пороги подобраны как практические warning/action границы, а не как абсолютная истина.
    """

    LOWER_IS_BETTER = {
        "cyclomatic": Threshold(10, 20),
        "cognitive_complexity": Threshold(25, 40),
        "nesting": Threshold(3, 5),
        "loc": Threshold(40, 80),
        "nloc": Threshold(30, 60),
        "args_count": Threshold(4, 7),
        "longest_string": Threshold(100, 140),
        "average_string_length": Threshold(80, 100),
        "fan_in": Threshold(10, 30),
        "fan_out": Threshold(7, 14),
        "god_class": Threshold(20, 40),
        "lcom1": Threshold(10, 25),
        "lcom4": Threshold(1, 3),
        "halstead_uniq_elements": Threshold(40, 80),
        "halstead_all_elements": Threshold(150, 400),
        "halstead_volume": Threshold(1000, 4000),
        "halstead_difficulty": Threshold(20, 50),
        "halstead_effort": Threshold(20000, 100000),
        "halstead_time": Threshold(1100, 5500),
    }

    SKIP_FIELDS = {
        "name",
        "type",
        "start_line",
        "end_line",
        "bases",
    }

    def evaluate(self, metric_name: str, value: Any) -> str:
        if not self._is_number(value):
            return Verdict.UNKNOWN.value

        value = float(value)

        if metric_name == "maintainability_index":
            return self._evaluate_maintainability(value)

        rule = self.LOWER_IS_BETTER.get(metric_name)
        if rule is None:
            return Verdict.UNKNOWN.value

        if value <= rule.green_max:
            return Verdict.GREEN.value
        if value <= rule.yellow_max:
            return Verdict.YELLOW.value
        return Verdict.RED.value

    def _evaluate_maintainability(self, value: float) -> str:
        """
        Visual Studio scale:
        20–100 green, 10–19 yellow, 0–9 red.
        """
        if value >= 20:
            return Verdict.GREEN.value
        if value >= 10:
            return Verdict.YELLOW.value
        return Verdict.RED.value

    def evaluate_result(self, result: dict) -> dict:
        output = result.copy()

        for key, value in result.items():
            if key in self.SKIP_FIELDS:
                continue

            output[f"{key}_verdict"] = self.evaluate(key, value)

        return output

    @staticmethod
    def _is_number(value: Any) -> bool:
        if isinstance(value, bool):
            return False
        if not isinstance(value, (int, float)):
            return False
        return not isnan(float(value)) and not isinf(float(value))