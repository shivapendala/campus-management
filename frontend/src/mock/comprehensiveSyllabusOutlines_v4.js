/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 4
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v4 = {
  CSE: {
    semesters: [
      {
        semester: 6,
        courses: [
          {
            code: "CS601",
            title: "Software Engineering",
            units: [
              {
                unit: 1,
                title: "Software Process Models",
                topics: [
                  "Software engineering definition, software development life cycle (SDLC) phases.",
                  "Process models: Waterfall model, incremental process models, evolutionary process models (Prototyping, Spiral).",
                  "Unified Process (UP), Agile software development paradigms, Scrum framework, Extreme Programming (XP).",
                  "Software engineering ethics, professional practices, statutory software quality standards."
                ],
                learning_objectives: "Compare SDLC process models and apply agile scrum practices to development cycles."
              },
              {
                unit: 2,
                title: "Requirements Engineering & Analysis",
                topics: [
                  "Requirements engineering tasks: Inception, elicitation, elaboration, negotiation, specification, validation, management.",
                  "Software Requirements Specification (SRS) document structure, IEEE 830 standard.",
                  "Requirements modeling: Scenario-based modeling (use cases, activity diagrams), data modeling (class diagrams).",
                  "Behavioral modeling: State machine diagrams, sequence diagrams, collaboration diagrams."
                ],
                learning_objectives: "Elicit system requirements and write standard IEEE 830 compliant SRS specifications."
              },
              {
                unit: 3,
                title: "Software Design Concepts",
                topics: [
                  "Design process and design quality guidelines, abstraction, refinement, modularity, information hiding.",
                  "Functional independence: Cohesion types, coupling types, design trade-offs.",
                  "Software architecture designs: Data-centered, data-flow, call and return, layered architectures.",
                  "User Interface (UI) design guidelines, golden rules of interface design, user analysis and task modeling."
                ],
                learning_objectives: "Apply modularity rules and evaluate cohesion/coupling margins in software designs."
              },
              {
                unit: 4,
                title: "Software Testing Strategies",
                topics: [
                  "Strategic approach to software testing: Unit testing, integration testing (top-down, bottom-up, regression).",
                  "Validation testing, system testing: Recovery, security, stress, and performance testing.",
                  "Black-box testing techniques: Equivalence partitioning, boundary value analysis, decision table testing.",
                  "White-box testing techniques: Basis path testing, cyclomatic complexity calculation, control structure testing."
                ],
                learning_objectives: "Formulate testing matrices and compute cyclomatic complexity paths for coverage."
              },
              {
                unit: 5,
                title: "Software Project Management & Quality",
                topics: [
                  "Project metrics: Size-oriented metrics (LOC), function-oriented metrics (FP), empirical estimation models (COCOMO).",
                  "Software quality assurance (SQA): Software quality factors (McCall's factors), ISO 9000, CMMI levels.",
                  "Risk management: Risk identification, projection, mitigation, monitoring, and management (RMMM) plan.",
                  "Software configuration management (SCM): Version control (Git), change control process, build automation."
                ],
                learning_objectives: "Estimate software sizes using COCOMO models and construct risk mitigation maps."
              }
            ],
            textbooks: [
              "Roger S. Pressman and Bruce Maxim, 'Software Engineering: A Practitioner's Approach'.",
              "Ian Sommerville, 'Software Engineering', Pearson."
            ]
          }
        ]
      }
    ]
  },
  AIML: {
    semesters: [
      {
        semester: 5,
        courses: [
          {
            code: "AI502",
            title: "Natural Language Processing",
            units: [
              {
                unit: 1,
                title: "Text Processing and Language Modeling",
                topics: [
                  "Introduction to NLP, tokenization, stemming, lemmatization, stop words removal.",
                  "Regular expressions for pattern matching, sentence segmentation.",
                  "N-gram language models, perplexity evaluation, smoothing techniques (Laplace, Good-Turing, Kneser-Ney).",
                  "Part-of-Speech (POS) tagging: Hidden Markov Models (HMM), Viterbi tagging algorithm."
                ],
                learning_objectives: "Preprocess raw text corpora and build statistical language models."
              },
              {
                unit: 2,
                title: "Vector Semantics and Word Embeddings",
                topics: [
                  "Lexical semantics, WordNet, homonymy, polysemy, synonymy.",
                  "Vector space models, Term Frequency-Inverse Document Frequency (TF-IDF).",
                  "Word2Vec: Continuous Bag of Words (CBOW) and Skip-gram architectures, negative sampling.",
                  "Global Vectors for Word Representation (GloVe), FastText character-level embeddings."
                ],
                learning_objectives: "Implement static word vector representations and evaluate semantic spaces."
              },
              {
                unit: 3,
                title: "Sequence Labeling & Parsing",
                topics: [
                  "Named Entity Recognition (NER): Feature-based CRFs, BiLSTM-CRF architectures.",
                  "Constituency parsing: Context-Free Grammars, Cocke-Younger-Kasami (CYK) algorithm.",
                  "Dependency parsing: Transition-based and graph-based dependency parsing models.",
                  "Semantic Role Labeling (SRL), dependency tree representations."
                ],
                learning_objectives: "Construct syntactic dependency trees and identify sequence entities."
              },
              {
                unit: 4,
                title: "Seq2Seq Models & Attention",
                topics: [
                  "Machine translation: Statistical vs Neural Machine Translation (NMT).",
                  "Sequence-to-Sequence (Seq2Seq) framework, Encoder-Decoder architectures.",
                  "Information bottleneck in Seq2Seq, Bahdanau additive attention, Luong multiplicative attention.",
                  "Beam search decoding, evaluation metrics: BLEU, ROUGE, METEOR."
                ],
                learning_objectives: "Design encoder-decoder models and apply attention weighting maps."
              },
              {
                unit: 5,
                title: "Pre-trained Language Models",
                topics: [
                  "Transformer architecture review: Self-attention, multi-head attention, feed-forward layers.",
                  "Bidirectional Encoder Representations from Transformers (BERT): Pre-training tasks (MLM, NSP), fine-tuning.",
                  "Generative Pre-trained Transformer (GPT) series: Autoregressive training, zero-shot and few-shot learning.",
                  "Instruction tuning, Reinforcement Learning from Human Feedback (RLHF), LLM safety and alignment."
                ],
                learning_objectives: "Fine-tune BERT classifiers and prompt autodecoder LLMs."
              }
            ],
            textbooks: [
              "Daniel Jurafsky and James H. Martin, 'Speech and Language Processing'.",
              "Christopher D. Manning and Hinrich Schütze, 'Foundations of Statistical Natural Language Processing'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v4;
