# TRANSCODER
## Main idea
1. get the language we actually want to convert 
2. select a folder, a file or multiple files in order to gain the knwoledge about what is the starting language (if multiple files then select the most predominant one, can also become a classification problem since we can have similar frameworks such as react and angular and we should discern the language based on specific files we can map the correlation between files and also the code structure to derive the specific language used)
3. use codellama to derive a first (modifiable) 

## Problems
1. How do we chunk the documents that are passed to build eventually a RAG pipeline
2. What embeddings should we use
3. What vector store should we use?
4. Is streamlit a good framework to use or is it better to code this directly in angular? and create a backend with fastapi?
5. Should we use langchain with langserve to ease our work?
6. How to store documents? Is mongodb a good approach?

## Security problems
1. If some malicious code is built inside the folders that are passed how can we be sure? What are the checks that we want to perform?

## Virtual env
With conda
```
conda create -n transcoder
```
Fresh start
```
pip freeze > req.txt & pip uninstall -r req.txt & rm req.txt
```
Python version = 3.12.4

## Model used 
codellama:13b
INFOS
| **Model**              |                                  |
|------------------------|----------------------------------|
| **Architecture**       | llama                            |
| **Parameters**         | 13.0B                            |
| **Context Length**     | 16384                            |
| **Embedding Length**   | 5120                             |
| **Quantization**       | Q4_0                             |

| **Parameters**            |                                  |
|---------------------------|----------------------------------|
| **rope_frequency_base**   | 1e+06                            |
| **stop**                  | "[INST]"                         |
| **stop**                  | "[/INST]"                        |
| **stop**                  | "<<SYS>>"                        |
| **stop**                  | "<</SYS>>"                       |

| **License**               |                                  |
|---------------------------|----------------------------------|
| **Name**                  | LLAMA 2 COMMUNITY LICENSE AGREEMENT|
| **Version Release Date**  | July 18, 2023                     |

## MVP
Create a frontend page that takes in a single file.
Evaluate based on the file what is the actual language used.
Have a combobox where the user select the output language.
Perform the translation.
It should contain also the instruction in how to run the program if it needs some particular configurations.
The final result doesnt need to be modifiable.

## Run streamlit
I had a problem running streamlit so I needed to use this command instead of only streamlit
```
python -m streamlit run main.py
```
