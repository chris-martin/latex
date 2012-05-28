import sys

def split(xs, sep):
  chunk = []
  for x in xs:
    if x == sep:
      if len(chunk) != 0:
        yield chunk
        chunk = []
    else:
      chunk.append(x)
  if len(chunk) != 0:
    yield chunk

def verb(a, b, py=False):
  lines = a.readlines()
  chunks = [lines] if py else split(lines, '\n')
  for chunk in chunks:
    b.write('\\begin{python}' if py else '\\begin{Verbatim}[samepage=true]\n')
    for line in chunk:
      b.write(line)
    b.write('\\end{python}' if py else '\\end{Verbatim}\n')
  b.flush()

for a in sys.argv[1:]:
  verb(open(a), open('%s.tex' % a, 'w'), py=a.endswith('.py'))

