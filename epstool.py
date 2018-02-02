import sys
import contextlib
from math import pi, ceil, sin, cos
from datetime import datetime
from pathlib import Path

_STDOUT = None

_HEADER = """%!PS-Adobe-3.0 EPSF-3.0
%%Title: {TITLE}
%%Creator: {AUTHOR}
%%CreationDate: {DATE}
%%BoundingBox: 0 0 {X:d} {Y:d}
%%HiResBoundingBox: 0.0000000 0.0000000 {X:11.7f} {Y:11.7f}
%%EndComments
1 setlinecap
0.0000000 0.0000000 0.0000000 setrgbcolor
{ε:11.7f} setlinewidth
{CS:11.7f} {CS:11.7f} scale
"""

_BACKGROUND = """
gsave
  0.0000000   0.0000000 moveto
{X:11.7f}   0.0000000 lineto
{X:11.7f} {Y:11.7f} lineto
  0.0000000 {Y:11.7f} lineto
closepath
1 1 1 setrgbcolor
fill
grestore
"""

_FOOTER = """
  0.0000000   0.0000000 moveto
{X:11.7f}   0.0000000 lineto
{X:11.7f} {Y:11.7f} lineto
  0.0000000 {Y:11.7f} lineto
closepath
clip
"""

def epsbuf(buff, title, date, author, background, X, Y, ε, scale, content_scale):
    _STDOUT = sys.stdout
    try:
        sys.stdout = buff
        print(_HEADER.format(TITLE=title, DATE=datetime.now(), AUTHOR=author,
                             X=ceil(X*scale), Y=ceil(Y*scale), ε=2.5*ε, CS=content_scale))
        if background: print(_BACKGROUND.format(X=X, Y=Y))
        yield
        print(_FOOTER.format(X=X, Y=Y))
    finally:
        sys.stdout = _STDOUT
        _STDOUT = None


@contextlib.contextmanager
def epsoutput(path=Path("test.eps"),
              title=None,
              date=None,
              author="Anonymous epstool",
              background=False,
              X=1, Y=1, ε=1/180,
              scale=180.0, content_scale=180.0):
    global _STDOUT
    assert _STDOUT is None, "No recursive eps writing contexts!"
    assert isinstance(path, Path) or isinstance(path, str), "The first argument should be a path!"
    path = Path(path)
    if date is None: date=datetime.now()
    if title is None: title = str(path.name)
    yield from epsbuf(path.open("w"), title, date, author, background, X, Y, ε, scale, content_scale)

redarc = lambda R: " gsave 0.2 setlinewidth 1 0 0 setrgbcolor " + arc(0,pi/2,R) + "grestore"

def point(x, y):
    return " {x:11.7f} {y:11.7f} moveto {x:11.7f} {y:11.7f} lineto stroke".format(x=x, y=y)

def arc(fi1, fi2, R, x=0, y=0):
    fi1 = fi1*180/pi
    fi2 = fi2*180/pi
    return " {x:11.7f} {y:11.7f} {R:11.7f} {fi1:11.7f} {fi2:11.7f} arc stroke".format(
        x=x, y=y, R=R, fi1=fi1, fi2=fi2)

def arc_point(a, R):
    x = R*cos(a)
    y = R*sin(a)
    return " {x:11.7f} {y:11.7f} moveto {x:11.7f} {y:11.7f} lineto stroke".format(x=x, y=y)

