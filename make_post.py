"""Script to create a new post and make it easy to edit"""
from subprocess import run
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from string import Template
import platform
import re


template = Template("""---
layout: post
title: "${title}"
date: $post_date $post_time -0700
type: $type
---

[Your content here]
""")

# Read in the command-line options
parser = ArgumentParser()
parser.add_argument('--date', help='Date of proposal submission in MM-DD[-YYYY]', type=str, required=True)
parser.add_argument('--type', help='Type of the post', type=str, required=True, choices=['award', 'join', 'paper', 'presentation'])
parser.add_argument('title', help='Title of the post', nargs='+', type=str)
args = parser.parse_args()

# Extract the input date
date_re = re.compile("(?P<month>\d{1,2})-(?P<day>\d{1,2})-?(?P<year>\d{2,4})?")
match = date_re.match(args.date)
if match is None:
    raise ValueError('Expected date in MM-DD-YYYY or MM-DD format.')
m = match.groupdict()

#  Get either the current year or the one specified by the user
year = m['year']
if year is None:
    year = datetime.now().year
else:
    year = int(m['year'])
if year < 2000: 
    year += 2000  # If this is still used in 2100+, we've got other problems

#  Combine the year with the month and day to YYYY-MM-DD format
month = int(m['month'])
day = int(m['day'])
post_date = f'{year}-{month:02}-{day:02}'
print(f'Post will be for {post_date}')

# Make short version of the title
short_title = "-".join([x.lower() for x in args.title[:3]])

# Format the post
post = template.substitute(
    title=" ".join(args.title),
    post_date=post_date,
    post_time=datetime.now().strftime('%H:%M:%S'),
    type=args.type
)

# Write the post to disk
post_path = Path(__file__).parent / '_posts' / f'{post_date}-{short_title}.markdown'
print(f'Writing to {post_path}')
with post_path.open('w') as fp:
    fp.write(post)

# Open it with text editor
if platform.system() == "Windows":
    editor = "notepad.exe"
else: 
    editor = "vim"  # vim forever! (TODO: Make this changeable by users)
print(f'Opening with {editor}')

proc = run([editor, str(post_path)], shell=True)
print(f'Done! Don\'t forget to git add the resultant file "git add {post_path.relative_to(Path().absolute())}"')
