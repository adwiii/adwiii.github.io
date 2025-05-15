
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd
import numpy as np
import os

# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path_parent = os.path.dirname(dir_path)
tsv_file = f'{dir_path}/publications.tsv'
publications = pd.read_csv(tsv_file, sep="\t", header=0)
publications


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


def format_bibtex(bibtex):
    return bibtex

# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
total_bibtex = ''
for row, item in publications.iterrows():
    
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += "collection: publications"
    
    md += "\npermalink: /publication/" + html_filename
    
    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
    
    md += "\ndate: " + str(item.pub_date) 
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"

    md += "\nbibtex: '" + format_bibtex(item.bibtex) + "'"
    image = (item.image if type(item.image) == str else '')
    if len(image) > 0:
        md += "\nimage: '" + image + "'"

    gh = (item.github if type(item.github) == str else '')
    if len(gh) > 0:
        md += "\ngithub: '" + gh + "'"

    md += f"\npaper_type: '{item.paper_type}'"

    short_venue = (item.short_venue if type(item.short_venue) == str else '')
    if len(short_venue) > 0:
        if short_venue.lower() == "journal":
            md += "\njournal: true"
            md += f"\nyear: {item.pub_date[:item.pub_date.find('-')]}"
        else:
            md += "\njournal: false"
            md += "\nshort_venue: \"" + short_venue + "\""
            series = short_venue[:short_venue.find('\'')]
            md += f"\nseries: {series}"
            md += f"\nshort_year: \"{short_venue[len(series):]}\""
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>"
    if len(gh) > 0 and len(str(item.paper_url)) > 5:
        md += ('&nbsp;' * 2)
    if len(gh) > 0:
        md += '\n<a href="' + gh + '"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>'
    if len(gh) > 0 or len(str(item.paper_url)) > 5:
        md += '\n'
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"

    # Recommended citation is already included earlier
#     md += "\nRecommended citation: " + item.citation
    
    md_filename = os.path.basename(md_filename)

    total_bibtex += item.bibtex + '\n'

    with open(f"{dir_path_parent}/_publications/" + md_filename, 'w') as f:
        f.write(md)

with open(f"{dir_path}/publications.bib", "w") as f:
    f.write(total_bibtex)


