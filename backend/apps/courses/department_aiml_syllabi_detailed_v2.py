"""
EduCore Framework - Department of Artificial Intelligence & Machine Learning (AIML) Detailed Course Syllabi v2

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced AIML courses:
- AI502: Natural Language Processing (NLP)
- AI601: Computer Vision & Generative AI (CV)
"""

from typing import Dict, Any

AIML_DETAILED_COURSES_CATALOG_V2: Dict[str, Dict[str, Any]] = {
    "AI502": {
        "code": "AI502",
        "title": "Natural Language Processing",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Text Processing and Language Modeling",
                "topics": [
                    "Introduction to NLP, tokenization, stemming, lemmatization, stop words removal",
                    "Regular expressions for pattern matching, sentence segmentation",
                    "N-gram language models, perplexity evaluation, smoothing techniques (Laplace, Good-Turing, Kneser-Ney)",
                    "Part-of-Speech (POS) tagging: Hidden Markov Models (HMM), Viterbi algorithm for decoding"
                ]
            },
            {
                "unit": 2,
                "title": "Vector Semantics and Word Embeddings",
                "topics": [
                    "Lexical semantics, WordNet, homonymy, polysemy, synonymy",
                    "Vector space models, Term Frequency-Inverse Document Frequency (TF-IDF)",
                    "Word2Vec: Continuous Bag of Words (CBOW) and Skip-gram architectures, negative sampling",
                    "Global Vectors for Word Representation (GloVe), FastText character-level embeddings",
                    "Evaluating embeddings: Intrinsic and extrinsic evaluation metrics"
                ]
            },
            {
                "unit": 3,
                "title": "Sequence Labeling & Parsing",
                "topics": [
                    "Named Entity Recognition (NER): Feature-based CRFs, BiLSTM-CRF architectures",
                    "Constituency parsing: Context-Free Grammars, Cocke-Younger-Kasami (CYK) algorithm",
                    "Dependency parsing: Transition-based and graph-based dependency parsing models",
                    "Semantic Role Labeling (SRL), dependency tree representations"
                ]
            },
            {
                "unit": 4,
                "title": "Seq2Seq Models & Attention Mechanism",
                "topics": [
                    "Machine translation: Statistical vs Neural Machine Translation (NMT)",
                    "Sequence-to-Sequence (Seq2Seq) framework, Encoder-Decoder architectures",
                    "Information bottleneck in Seq2Seq, Bahdanau additive attention, Luong multiplicative attention",
                    "Beam search decoding, evaluation metrics: BLEU, ROUGE, METEOR"
                ]
            },
            {
                "unit": 5,
                "title": "Pre-trained Language Models",
                "topics": [
                    "Transformer architecture review: Self-attention, multi-head attention, feed-forward layers",
                    "Bidirectional Encoder Representations from Transformers (BERT): Pre-training tasks (MLM, NSP), fine-tuning",
                    "Generative Pre-trained Transformer (GPT) series: Autoregressive training, zero-shot and few-shot learning",
                    "Instruction tuning, Reinforcement Learning from Human Feedback (RLHF), LLM safety and alignment"
                ]
            }
        ],
        "textbooks": [
            "Daniel Jurafsky and James H. Martin, 'Speech and Language Processing', Pearson, 3rd Edition Draft.",
            "Christopher D. Manning and Hinrich Schütze, 'Foundations of Statistical Natural Language Processing', MIT Press."
        ]
    },
    "AI601": {
        "code": "AI601",
        "title": "Computer Vision",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Image Formation & Processing",
                "topics": [
                    "Pinhole camera model, camera calibration, intrinsic and extrinsic parameters",
                    "Image filtering: Gaussian blur, median filter, bilateral filter",
                    "Edge detection: Sobel, Laplacian of Gaussian, Canny edge detector",
                    "Scale-Invariant Feature Transform (SIFT), Speeded-Up Robust Features (SURF), Harris corner detector"
                ]
            },
            {
                "unit": 2,
                "title": "Image Classification & CNNs",
                "topics": [
                    "Image classification pipeline, linear classifiers, loss functions: Multiclass SVM, Softmax",
                    "Convolutional Neural Networks (CNNs) for vision, architectural evolution: VGG, ResNet, EfficientNet",
                    "Data augmentation techniques, transfer learning, fine-tuning strategies"
                ]
            },
            {
                "unit": 3,
                "title": "Object Detection & Segmentation",
                "topics": [
                    "Object detection concepts, bounding box regression, Intersection over Union (IoU), non-maximum suppression",
                    "Two-stage detectors: R-CNN, Fast R-CNN, Faster R-CNN (Region Proposal Networks)",
                    "One-stage detectors: YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector)",
                    "Semantic segmentation: Fully Convolutional Networks (FCN), U-Net, DeepLab",
                    "Instance segmentation: Mask R-CNN architecture"
                ]
            },
            {
                "unit": 4,
                "title": "Object Tracking & Video Analysis",
                "topics": [
                    "Optical flow: Lucas-Kanade and Horn-Schunck algorithms",
                    "Object tracking paradigms: Kalman filtering, Mean-Shift, DeepSORT tracker",
                    "Action recognition in video: 3D CNNs, Two-stream networks, LSTM-based models"
                ]
            },
            {
                "unit": 5,
                "title": "Generative Models in Vision",
                "topics": [
                    "Variational Autoencoders (VAEs): Mathematical formulation, reparameterization trick",
                    "Generative Adversarial Networks (GANs): Minimax game, DCGAN, CycleGAN, StyleGAN",
                    "Diffusion models: Denoising Diffusion Probabilistic Models (DDPM), Stable Diffusion architecture",
                    "Evaluation of generative models: Inception Score (IS), Frechet Inception Distance (FID)"
                ]
            }
        ],
        "textbooks": [
            "Richard Szeliski, 'Computer Vision: Algorithms and Applications', Springer, 2nd Edition.",
            "David A. Forsyth and Jean Ponce, 'Computer Vision: A Modern Approach', Pearson, 2nd Edition."
        ]
    }
}
