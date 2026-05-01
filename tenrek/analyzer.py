from tenrek.metrics import cyclomatic
from tenrek.metrics import cognitive_complexity
from tenrek.metrics import nesting
from tenrek.metrics import loc
from tenrek.metrics import nloc
from tenrek.metrics.for_classes import god_class
from tenrek.metrics import longest_string
from tenrek.metrics import average_string_lenght
from tenrek.metrics import maintainability_index
from tenrek.metrics.halstead import halstead_uniq_elements
from tenrek.metrics.halstead import halstead_all_elements
from tenrek.metrics.halstead import halstead_volume
from tenrek.metrics.halstead import halstead_difficulty
from tenrek.metrics.halstead import halstead_effort
from tenrek.metrics.halstead import halstead_time

class ComplexityAnalyzer:
    def __init__(self, parser, standard: str = "cpp17"):
        self.parser = parser
        self.standard = standard

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



    


