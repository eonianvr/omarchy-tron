import math, random, sys

W, H = 3840, 2160
CYAN = "#4dd7f5"
DEEP = "#14556b"
ORANGE = "#ff9f1c"
OUT = sys.argv[1]

def head(extra=""):
    return ["push graphic-context", "viewbox 0 0 %d %d" % (W, H), "fill none", extra]

# ---------------------------------------------------------------- grid horizon
def grid():
    horizon = 1180.0
    vpx = W / 2.0
    K = (H - horizon)  # depth-1 row sits on the bottom edge
    d = head()
    # receding horizontal rows
    d.append("stroke-linecap round")
    for i in range(1, 90):
        y = horizon + K / i
        if y < horizon + 1.2:
            break
        w = max(0.9, 7.0 / (i ** 0.62))
        d.append("stroke-width %.2f" % w)
        d.append("stroke '%s'" % (CYAN if i <= 26 else DEEP))
        d.append("line 0,%.2f %d,%.2f" % (y, W, y))
    # converging verticals
    for s in range(-13000, 13001, 260):
        if s == 0:
            continue
        w = 3.4 if abs(s) < 3000 else 2.2
        d.append("stroke-width %.2f" % w)
        d.append("stroke '%s'" % (CYAN if abs(s) < 6500 else DEEP))
        d.append("line %.1f,%d %.1f,%.1f" % (vpx + s, H, vpx, horizon))
    # the horizon itself, brightest
    d.append("stroke-width 5")
    d.append("stroke '%s'" % CYAN)
    d.append("line 0,%.2f %d,%.2f" % (horizon, W, horizon))
    # a lone light-cycle ribbon cutting across the plane
    d.append("stroke '%s'" % ORANGE)
    d.append("stroke-width 6")
    d.append("path 'M 620,2160 L 1500,1420 L 2450,1420 L 2980,1235'")
    d.append("pop graphic-context")
    return d

# -------------------------------------------------------------------- circuits
def circuits():
    random.seed(1982)
    step = 60
    d = head()
    d.append("stroke-linecap round")
    d.append("stroke-linejoin round")
    traces = []
    for _ in range(95):
        x = random.randrange(2, W // step - 2) * step
        y = random.randrange(2, H // step - 2) * step
        pts = [(x, y)]
        horiz = random.random() < 0.5
        for _ in range(random.randint(3, 9)):
            leg = random.randint(2, 9) * step
            sign = random.choice((-1, 1))
            nx, ny = pts[-1]
            if horiz:
                nx = min(max(nx + sign * leg, step), W - step)
            else:
                ny = min(max(ny + sign * leg, step), H - step)
            pts.append((nx, ny))
            horiz = not horiz
        traces.append(pts)
    for pts in traces:
        hot = random.random() < 0.12
        d.append("stroke '%s'" % (ORANGE if hot else (CYAN if random.random() < 0.45 else DEEP)))
        d.append("stroke-width %.1f" % (3.6 if hot else random.choice((2.0, 2.6, 3.4))))
        d.append("path '%s'" % " L ".join(["M %d,%d" % pts[0]] + ["%d,%d" % p for p in pts[1:]]).replace("M ", "M ", 1))
        # solder pads at the ends
        for px, py in (pts[0], pts[-1]):
            d.append("fill '%s'" % (ORANGE if hot else CYAN))
            d.append("stroke none")
            d.append("circle %d,%d %d,%d" % (px, py, px + 7, py))
            d.append("fill none")
            d.append("stroke '%s'" % (ORANGE if hot else CYAN))
    d.append("pop graphic-context")
    return d

# ------------------------------------------------------------------ identity disc
def disc():
    cx, cy = W / 2.0, H / 2.0
    d = head()
    for r, w, col in [
        (760, 10, CYAN), (700, 3, DEEP), (612, 6, CYAN), (596, 2, DEEP),
        (470, 4, DEEP), (392, 14, CYAN), (300, 3, DEEP), (206, 7, CYAN),
        (120, 2, DEEP), (64, 10, ORANGE),
    ]:
        d.append("stroke '%s'" % col)
        d.append("stroke-width %d" % w)
        d.append("circle %.0f,%.0f %.0f,%.0f" % (cx, cy, cx + r, cy))
    # radial spokes broken into arc segments
    d.append("stroke-width 5")
    d.append("stroke '%s'" % CYAN)
    for k in range(24):
        a = math.radians(k * 15 + 7.5)
        x1, y1 = cx + 392 * math.cos(a), cy + 392 * math.sin(a)
        x2, y2 = cx + 612 * math.cos(a), cy + 612 * math.sin(a)
        if k % 3:
            d.append("line %.1f,%.1f %.1f,%.1f" % (x1, y1, x2, y2))
    # tangent leads running off the frame
    d.append("stroke '%s'" % DEEP)
    d.append("stroke-width 3")
    for k in range(8):
        a = math.radians(k * 45 + 22.5)
        x1, y1 = cx + 770 * math.cos(a), cy + 770 * math.sin(a)
        x2, y2 = cx + 2600 * math.cos(a), cy + 2600 * math.sin(a)
        d.append("line %.1f,%.1f %.1f,%.1f" % (x1, y1, x2, y2))
    d.append("pop graphic-context")
    return d

print("\n".join({"grid": grid, "circuits": circuits, "disc": disc}[OUT]()))
