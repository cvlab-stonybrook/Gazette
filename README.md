# Gazette
Official repository for **Gaze**-**t**o-**te**xt generative decoding model aka **Gazette** proposed in "Gaze-to-text Generation: Beyond Categorical Decoding of Human Attention" by Sounak Mondal, Dimitris Samaras, Gregory Zelinsky, Minh Hoai.

🎉 Our paper has been accepted to [**European Conference on Computer Vision (ECCV) 2026**](https://eccv.ecva.net/Conferences/2026)!

📨 Contact **Sounak Mondal** at ```somondal@cs.stonybrook.edu``` for any queries. **Please do not open issues in this repository for questions or inquiries, as we do not actively monitor it. Instead, please contact Sounak directly via email.**

🧠 We introduce a novel learning problem: decoding gaze into natural language descriptions of human goals across diverse visual tasks. Unlike prior work, which frames gaze decoding as a discriminative task over predefined categories, we formulate it as a generative learning problem: training a model to produce free-form descriptions that capture the rich nuances and open-ended nature of human intentions beyond fixed labels. To this end, we introduce Gazette, the first gaze-to-text decoding framework. Based on multimodal large language models (MLLMs), Gazette learns to decode gaze scanpaths into natural language for goals that may extend beyond categorical labels and require articulation in natural language. To help Gazette filter out individual differences in gaze behavior and learn the goal-specific spatiotemporal dynamics crucial for generating accurate natural language goal descriptions, we propose a novel strategy that leverages the encyclopedic knowledge and reasoning abilities of a large language model to synthesize natural language explanations of goal-directed attentional behavior called think-aloud transcripts. Instruction tuning on these synthetic narratives allows Gazette to achieve state-of-the-art performance in gaze decoding across multiple tasks, demonstrating its generalizability and versatility, thereby enabling gaze to serve as a powerful, non-intrusive cue for inferring human goals and intentions in diverse scenarios.

🧑‍💻 Code coming soon, stay tuned!

📜 Preprint coming soon, stay tuned!
