import sys

from amr_utils.amr_readers import AMR_Reader

from display import Display
from evaluate.utils import evaluate
from models.subgraph_model import Subgraph_Model
from nlp_data import add_nlp_data


def coverage(amrs, alignments):
    coverage_count = 0
    total = 0
    for amr in amrs:
        for n in amr.nodes:
            align = amr.get_alignment(alignments, node_id=n)
            if align:
                coverage_count+=1
            total+=1
    return f'{100*coverage_count/total:.2f}%'

def main():
    train_align_file = sys.argv[1]
    train_amr_file = sys.argv[2]
    eval_amr_file = sys.argv[3]

    reader = AMR_Reader()
    train_amrs = reader.load(train_amr_file, remove_wiki=True)
    add_nlp_data(train_amrs, train_amr_file)

    eval_amrs = reader.load(eval_amr_file, remove_wiki=True)
    add_nlp_data(eval_amrs, eval_amr_file)
    gold_dev_alignments = reader.load_alignments_from_json(sys.argv[4], eval_amrs)

    train_alignments = reader.load_alignments_from_json(train_align_file, train_amrs)

    align_model = Subgraph_Model(train_amrs, align_duplicates=True)
    align_model.update_parameters(train_amrs, train_alignments)

    eval_alignments = align_model.align_all(eval_amrs)
    print('align subgraphs', coverage(eval_amrs, eval_alignments))

    evaluate(eval_amrs, eval_alignments, gold_dev_alignments)
    print()

    # write output
    align_file = eval_amr_file.replace('.txt', '') + f'.subgraph_alignments.json'
    print(f'Writing subgraph alignments to: {align_file}')
    reader.save_alignments_to_json(align_file, eval_alignments)
    for amr in eval_amrs:
        amr.alignments = eval_alignments[amr.id]
    Display.style(eval_amrs, eval_amr_file.replace('.txt', '') + f'.subgraphs.html')


if __name__=='__main__':
    main()