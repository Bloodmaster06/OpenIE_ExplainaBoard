import argparse
import os
import sys
# sys.path.append('../')

import torch.nn as nn
import logging
import torch
from eval.oie_eval.oie_readers.goldReader import GoldReader
from eval.oie_eval.carb import Benchmark
from eval.oie_eval.matcher import Matcher
def eval(gold_output, model_output, result, error_log):
    """
        Args:
            gold_output(str): the path of gold(true) predication.
            model_output(str): the path of the result predicated by model.
            result(str): the path of the evaluation result.
            error_log(str): the path of the error log.
        """
    benchmark = Benchmark(gold_file)
    predicted = GoldReader()
    predicted.read(model_output)
    matching_func = Matcher.binary_linient_tuple_match
    logging.info("Writing PR curve of {} to {}".format(predicted.name, result))
    auc, optimal_f1_point= benchmark.compare(  predicted = predicted.oie,
                                        matchingFunc = matching_func,
                                        output_fn = result,
                                        error_file = error_log)
    precision, recall, f_1 = optimal_f1_point[0], optimal_f1_point[1], optimal_f1_point[2]
    with open(result, "a") as fw:
        fw.write("precision: {:.5f}, recall: {:.5f}, f_1: {:.5f}".format(precision, recall, f_1))

    print("AUC:{:.5f}, P:{:.5f}, R:{:.5f}, F1:{:.5f}".format(auc,precision, recall, f_1))
    return auc, precision, recall, f_1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Usage for OPENIE evaluation.")
    args, extra_args = parser.parse_known_args()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    args = parser.parse_args()
    data_dir = './data/openie4/'
    gold_output = data_dir + 'test.gold'
    model_output = data_dir + 'test_output'
    result = data_dir + 'result'
    error_log = data_dir + 'error_log'
    auc, precision, recall, f1 = eval(
        gold_output, 
        model_output, 
        result,
        error_log)