import json

json_file_path = "./chunks_output.json"

def separate_content_types(chunk):
    content_data = {
        "text" : chunk["text"],
        "tables" : [],
        "images" : [],
        "types" : ["text"]  
    }

    if "metadata" in chunk and "orig_elements" in chunk["metadata"]:
        for element in chunk["metadata"]["orig_elements"]:
            element_type = element.category

            if element_type == "Table":
                print('x')


def summarize_chunks(chunks):
    for chunk in chunks:
        separate_content_types(chunk)


# Summarize chunks
with open(json_file_path, "r", encoding="utf-8") as file:
    chunks = json.load(file)
    
summarize_chunks(chunks[:1])

