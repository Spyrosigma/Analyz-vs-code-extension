# Analyz - Visual Studio Code Extension

Analyz a Code Buddy is a powerful Visual Studio Code extension designed to assist developers during coding sessions, providing real-time code analysis and helpful suggestions for better understanding and efficient coding. Leveraging the Mistral Instruct model fine-tuned on a dataset of over 200 rows, this extension offers comprehensive support for various programming languages and scenarios. With seamless integration into Visual Studio Code, it delivers a user-friendly experience, allowing developers to optimize their code structure and enhance overall coding efficiency. 

# Functionality

### Chatbot

Analyz is a chatbot created to assist users and make coding simpler, readily available right within the vscode. The chatbot is designed to understand what you're asking, generate helpful code snippets, and provide useful information. It uses the Mistral 7b finetuned model, ensuring it generate responses that suit your specific needs.

https://github.com/srujan-landeri/Analyz-vs-code-extension/assets/66351075/24ceb275-b772-4217-b679-a3d5f1038b13

### Algorithm Complexity Analysis

Algorithm Analysis is one such metric every programmer uses to know how well the function is. Analyz makes this easy, by providing insights on every function by providing the time and space complexity along with suggestions on how can the function be improved further with just a single click.

https://github.com/srujan-landeri/Analyz-vs-code-extension/assets/66351075/b8fab4e8-5809-489b-8cea-fe1501922c7b

### Code Converter

Analyz simplifies the code conversion by allowing users to modify their code directly from within the editor. This user-friendly feature supports programming languages, compatible with more than 70 languages. For increased accuracy and versatility, Analyz leverages the power of OpenAI, ensuring that your code changes are accurate. 

https://github.com/srujan-landeri/Analyz-vs-code-extension/assets/66351075/8d10a129-428d-47b7-9b30-936f47e32dd5

### Flowcharts

The flowchart functionality in Analyz is unique and distinctive. Unlike GPT, Analyz can create flowcharts, offering unique capabilities by using OpenAI. Analyz can effectively create flowcharts to help users understand concepts easily.

https://github.com/srujan-landeri/Analyz-vs-code-extension/assets/66351075/fd9133f2-b501-4ade-b323-7487fda5d684

# Fine-tuned model

🔗https://huggingface.co/RachitD15673/mistral-finetuned-7B-instruct-manual

**Fine-Tuned Mistral 7B Model**

In this repository, we detail the process through which the Mistral 7B language model was fine-tuned using a specialized dataset sourced from the Algorithms repository on GitHub.

**Fine-Tuning Process Overview**

The fine-tuning was accomplished by employing the QLoRA (Query-specific LORA) technique, a method that efficiently adapts large language models to new tasks with minimal parameter updates.

**Steps of Fine-Tuning with QLoRA:**

1. *Dataset Acquisition*:
   - We procured a custom dataset of algorithmic content from TheAlgoritms GitHub repository, which provided diverse coding problems and their algorithmic solutions.

2. *Preprocessing*:
   - The dataset underwent preprocessing to structure it appropriately for the model, involving tokenization and formatting suitable for the Mistral 7B's input requirements.

3. *QLoRA Configuration*:
   - We configured QLoRA by specifying the additional parameters to be introduced to the model’s attention mechanism, specifically targeting the query matrices.

4. *Model Initialization*:
   - The pre-trained Mistral 7B model was loaded, and QLoRA was integrated, allowing for efficient fine-tuning without extensive retraining of the original model parameters.

5. *Training*:
   - The training loop, tailored for the QLoRA-augmented model, optimized the newly introduced parameters using the prepared dataset, focusing the model's learning on algorithmic patterns and intricacies.

6. *Validation*:
   - Post-training, the model was evaluated against a set of algorithmic problems it had not seen before to ensure it had effectively learned from the fine-tuning process.

7. *Model Saving*:
   - With fine-tuning complete and the model achieving a high level of performance on algorithmic content, we saved the enhanced model, encapsulating the QLoRA adjustments.

The fine-tuning process allowed us to maintain the breadth of knowledge inherent to Mistral 7B while refining its expertise to understand and generate algorithmic code effectively.
