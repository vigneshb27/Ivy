import wikipedia

def search(query):
    try:
        results = wikipedia.summary(query , sentences = 2)
    except:
        return "Sorry some sort of error"
    return results

