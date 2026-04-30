from parser import CppParser
from analyzer import ComplexityAnalyzer
import json


def main(file_name):
    parser = CppParser(file_name)
    parser.parse()

    analyzer = ComplexityAnalyzer(parser)
    results = analyzer.analyze()

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()