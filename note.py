# python -m pip install ddgs

from ddgs import DDGS

query = input(r"C:\pythoncore-3.14-64\python.exe: can't open file 'C:\\Users\\HP\\OneDrive\\Documents\\notee.py': [Errno 2] No such file or directory ").strip()

try:
    results = DDGS().text(query, max_results=5)

    for i, result in enumerate(results, start=1):
        print(f"\n{i}. {result['title']}")
        print(result["href"])
        print(result["body"])

except Exception as e:
    print("Search error:", e)


