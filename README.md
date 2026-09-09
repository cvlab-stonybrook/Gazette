# Gazette
Official repository for **Gaze**-**t**o-**te**xt generative decoding model aka **Gazette** proposed in "Gaze-to-text Generation: Beyond Categorical Decoding of Human Attention" by Sounak Mondal, Dimitris Samaras, Gregory Zelinsky, Minh Hoai.

🎉 Our paper has been accepted to [**European Conference on Computer Vision (ECCV) 2026**](https://eccv.ecva.net/Conferences/2026)!

📜 Find the preprint on [arXiv](https://arxiv.org/pdf/2607.23917v1)!

📨 Contact **Sounak Mondal** at ```somondal@cs.stonybrook.edu``` for any queries. **Please do not open issues in this repository for questions or inquiries, as we do not actively monitor it. Instead, please contact Sounak directly via email.**

🧠 We introduce a novel learning problem: decoding gaze into natural language descriptions of human goals across diverse visual tasks. Unlike prior work, which frames gaze decoding as a discriminative task over predefined categories, we formulate it as a generative learning problem: training a model to produce free-form descriptions that capture the rich nuances and open-ended nature of human intentions beyond fixed labels. To this end, we introduce Gazette, the first gaze-to-text decoding framework. Based on multimodal large language models (MLLMs), Gazette learns to decode gaze scanpaths into natural language for goals that may extend beyond categorical labels and require articulation in natural language. To help Gazette filter out individual differences in gaze behavior and learn the goal-specific spatiotemporal dynamics crucial for generating accurate natural language goal descriptions, we propose a novel strategy that leverages the encyclopedic knowledge and reasoning abilities of a large language model to synthesize natural language explanations of goal-directed attentional behavior called think-aloud transcripts. Instruction tuning on these synthetic narratives allows Gazette to achieve state-of-the-art performance in gaze decoding across multiple tasks, demonstrating its generalizability and versatility, thereby enabling gaze to serve as a powerful, non-intrusive cue for inferring human goals and intentions in diverse scenarios.

# Installation

```bash
conda env create -n gazette --file gazette_env_export.yml
conda activate gazette
```

# Steps to follow before running the code

1. Download COCO-Search18, RefCOCO-Gaze, and AiR-D image stimuli.
2. Download [this folder](https://drive.google.com/drive/folders/1KW-p8P13qD9GX3_WCAua3q84p-igzDvI?usp=drive_link) titled ```training``` and place in ```data```.
3. Update the image paths

All `image` fields in the training file (`Gazette_finetune_thinkaloud.json`) and the
evaluation files (`gazette_finetune_test_questions_{tp,ta,vqa}.jsonl`) use a
`/path/to/` placeholder prefix. Replace it with the location of the image stimuli
on your system:

| Path pattern | Stimuli source |
| --- | --- |
| `/path/to/coco-search18/TP/images/<category>/…` | [COCO-Search18](https://sites.google.com/view/cocosearch/) — target-present |
| `/path/to/coco-search18/TA/images/<category>/…` | [COCO-Search18](https://sites.google.com/view/cocosearch/) — target-absent |
| `/path/to/refgaze/data/images_512X320/…` | [RefCOCO-Gaze](https://github.com/cvlab-stonybrook/refcoco-gaze/) |
| `/path/to/AiR/stimuli/…` | [AiR-D](https://github.com/szzexpoi/AiR) |

# Scripts

To train the model, run: 

```bash gazette_finetuning.sh```

To evaluate the model, run: 

```python3 llava/eval/model_vqa.py --question_file=./data/validation/questions/gazette_finetune_test_questions_tp.jsonl --model_path=/path/to/your/checkpoint/```

Optionally run: ```python visual_search_postprocess.py``` to convert the MLLM predictions for COCO-Search18 to the canonical category names. 

# Citation

Please cite our work as follows:

```
@InProceedings{mondal2026gazette,
author = {Mondal, Sounak and Samaras, Dimitris and Zelinsky, Gregory and Hoai, Minh},
title = {Gaze-to-text Generation: Beyond Categorical Decoding of Human Attention},
booktitle = {European Conference on Computer Vision (ECCV)},
year = {2026}
}
```
