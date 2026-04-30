from metrics import cyclomatic
from metrics import cognitive_complexity
from metrics import nesting
from metrics import loc
from metrics import nloc
from metrics.for_classes import god_class
from metrics import longest_string
from metrics import average_string_lenght
from metrics import maintainability_index
from metrics.halstead import halstead_uniq_elements
from metrics.halstead import halstead_all_elements
from metrics.halstead import halstead_volume
from metrics.halstead import halstead_difficulty
from metrics.halstead import halstead_effort
from metrics.halstead import halstead_time

class ComplexityAnalyzer:
    def __init__(self, parser):
        self.parser = parser

    def analyze(self):
        results = []
        function_metrics = [
            cyclomatic,
            cognitive_complexity,
            nesting,
            loc,
            nloc,
            longest_string,
            average_string_lenght,
            maintainability_index,
            halstead_uniq_elements,
            halstead_all_elements,
            halstead_volume,
            halstead_difficulty,
            halstead_effort,
            halstead_time
        ]

        class_metrics = [
            loc,
            nloc,
            nesting,
            god_class,
            longest_string,
            average_string_lenght
        ]

        functions = self.parser.get_functions()

        for func in functions:
            info = self.parser.get_function_info(func)
            result = {**info, "type": "function"}

            for metric in function_metrics:
                name = metric.__name__.split('.')[-1]
                result[name] = metric.calculate(func)

            results.append(result)


        methods = self.parser.get_methods()

        for method in methods:
            info = self.parser.get_function_info(method)
            result = {**info, "type": "method"}

            for metric in function_metrics:
                name = metric.__name__.split('.')[-1]
                result[name] = metric.calculate(method)

            results.append(result)


        classes = self.parser.get_classes()

        for clas in classes:
            info = self.parser.get_class_info(clas)
            result = {**info, "type": "class"}

            for metric in class_metrics:
                name = metric.__name__.split('.')[-1]
                result[name] = metric.calculate(clas)

            results.append(result)

        return results



    


