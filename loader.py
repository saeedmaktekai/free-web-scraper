from langchain_community.document_loaders import WebBaseLoader
# Load the website content
loader = WebBaseLoader("https://maktek.ai/")
docs = loader.load()
filename = "data.txt"
with open(filename, "w") as file:
   for doc in docs:
      file.write(doc.page_content)
      file.write("\n\n")  
print(f"Data has been saved to {filename}")




