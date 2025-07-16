import xml.etree.ElementTree as ET

# Load the SVG file
tree = ET.parse('assets/BD_Map_admin.svg')
root = tree.getroot()

# Define SVG namespace (often required)
ns = {'svg': 'http://www.w3.org/2000/svg'}

# Find all <text> elements with font-size="17.8907"
output = []

for text in root.findall('.//svg:text', ns):
    font_size = text.attrib.get('font-size')
    if font_size == '17.8907':
        id = text.attrib.get('id')
        t = text.findall()
        if id:
            js = {
                'text-id' : id,
                'name':t
            }
            output.append(js)

print(output)

