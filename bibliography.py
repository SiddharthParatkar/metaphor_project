from metaphor_python import Metaphor
import requests
from bs4 import BeautifulSoup

apa_or_mla = ""

def process_text_file(file_path: str, metaphor: callable):
    global apa_or_mla
    results = set()  # Initialize an empty hashset to store unique results

    # Open the text file and read line by line
    with open(file_path, 'r') as file:
        # for first line, check if APA or MLA without case
        apa_or_mla = file.readline().strip().upper()
        for line in file:
            line = line.strip()  # Remove leading and trailing whitespace
            if line:  # Skip empty lines
                result_url = metaphor(line)  # Run the 'metaphor' function on the line
                results.add(generate_citation(result_url))  # Add the result to the hashset

    # Print the unique results
    for result in results:
        print(result)

# Example usage
def metaphor(line: str) -> str:
    metaphor = Metaphor("METAPHOR_API_KEY")

    response = metaphor.search(
        line,
        exclude_domains=["https://www.twitter.com", "https://www.x.com", "https://www.reddit.com", "https://www.facebook.com", "https://www.youtube.com"],
        num_results=1,
    ).get_contents()
    return response.contents[0].url

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

def generate_citation(url):
    soup = fetch_and_parse(url)
    if soup:
        title = soup.title.string if soup.title else "No Title"
        author_meta = soup.find('meta', {'name': 'author'})
        author = author_meta['content'] if author_meta else "No Author"
        # publication_date_meta = soup.find('meta', {'name': 'date'})
        # publication_date = publication_date_meta['content'] if publication_date_meta else "No Date"
        publication_date = "No Date"
        for tag in soup.find_all(['time', 'span', 'div', 'p']):
            if tag.has_attr('datetime'):
                publication_date = tag['datetime']
                break
            elif tag.string and '20' in tag.string:  # Crude check for years
                publication_date = tag.string
                break
        
        # APA Style
        if apa_or_mla == "APA":
            apa_citation = f"{author} ({publication_date}). {title}. Retrieved from {url}"
            return apa_citation
        else:
            # MLA Style
            mla_citation = f'"{title}." {author}, {publication_date}. Web. {url}.'
            
            # return mla_citation
            return mla_citation
    else:
        return None, None
    
if __name__ == '__main__':
    file_path = 'test.txt'  # Replace with the path to your text file
    process_text_file(file_path, metaphor=metaphor)