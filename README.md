# Tron

An Omarchy theme for the Grid: near-black backdrops, cyan circuitry, and a
single orange line for the programs that went rogue.

![grid](backgrounds/1-grid.png)

## Install

```bash
omarchy theme install https://github.com/<you>/omarchy-tron.git
omarchy theme set tron
```

`omarchy theme install` strips the `omarchy-` prefix, so the repo installs
under the theme name **tron**.

## Develop against it locally

Point Omarchy at your working copy instead of a clone, so edits apply on the
next `omarchy theme set`:

```bash
ln -sfn ~/Work/omarchy-tron ~/.config/omarchy/themes/tron
omarchy theme set tron
```

A symlinked theme counts as hand-written rather than cloned, which means
Omarchy will stage every file in it — including any `hyprland.lua` or terminal
config you add. Themes installed from a git repo are restricted to colour.

## What's in here

| File | Purpose |
|------|---------|
| `colors.toml` | The whole palette. Omarchy renders Alacritty, Ghostty, Kitty, foot, Hyprland, btop, Neovim, Chromium, the shell, and the lock screen from it. |
| `icons.theme` | GTK icon theme to pair with it. |
| `backgrounds/` | Wallpapers, cycled with `omarchy theme bg next`. |
| `tools/` | Regenerates `backgrounds/` from vector primitives. |

## Palette

| Role | Colour | |
|------|--------|--|
| accent / cyan | `#4dd7f5` | the Grid |
| orange | `#ff9f1c` | Clu |
| background | `#050b0f` | |
| foreground | `#cfeff8` | |
| red | `#ff4d6d` | |
| yellow | `#ffc93c` | |
| green | `#3ff0a0` | |
| blue | `#2f9fff` | |
| magenta | `#b06dff` | |

Active window borders run a 45° cyan-to-orange gradient; inactive ones fall
back to the dim `#123a47` selection colour.

## Backgrounds

Every wallpaper is generated, not photographed — rerun the generator after
changing a colour in `tools/gen_mvg.py`:

```bash
./tools/generate-backgrounds.sh    # needs ImageMagick 7 + python3
```

1. **grid** — the light-cycle plane receding to a glowing horizon
2. **circuits** — board traces with a few hot orange runs
3. **identity-disc** — concentric rings on black

## License

MIT
