import yaml
from jinja2 import Environment, FileSystemLoader
from hymns import hymns
import os

# Define the paths for the YAML file and template
yaml_file_path = "data.yaml"
template_file_path = "template.html"
output_file_path = "output.html"

# Load data from YAML
with open(yaml_file_path, 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Load hymn details to the same variable
hymn_details = []
for hymn in data.get("program", []):
    if hymn.get("type", None) == "hymn":
        number = hymn["record"]["number"]
        hymn["record"]["title"] = hymns.get(number, ["", ""])[0]
        hymn["record"]["url"] = hymns.get(number, ["", ""])[1]
        #hymn_details.append( tmp_hymn )
#data["music_final"] = hymn_details

# Set up Jinja2 environment and load the HTML template
env = Environment(loader=FileSystemLoader(searchpath=os.path.dirname(template_file_path)))
template = env.get_template(os.path.basename(template_file_path))

# Render the template with data from YAML
rendered_html = template.render(data)

# Write the rendered HTML to a file
with open(output_file_path, "w") as output_file:
    output_file.write(rendered_html)

print(f"HTML file generated at {output_file_path}")
