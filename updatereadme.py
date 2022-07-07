import json

read_me_base = open('READMEBase.md')

snippet_text = open('snippets.json')
snippets = json.load(snippet_text)

read_me_new = read_me_base.read().splitlines()
for snippet in snippets.values():
    prefix = snippet['prefix']
    description = snippet['description']
    
    read_me_new.append(f"| `{prefix}` | {description} |")

with open('README.md', 'w') as f:
    f.write("\n".join(read_me_new))
    
read_me_base.close()
snippet_text.close()