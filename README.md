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
| `colors.toml` | The whole palette. Omarchy renders Alacritty, Ghostty, Kitty, foot, btop, Neovim, Chromium, the shell, and the lock screen from it. |
| `hyprland.lua` | Window glow: thick gradient borders, the accent-cyan halo on the focused window, dimming for everything else. Replaces the file Omarchy would generate. |
| `shell.controls.toml` | Replaces just the `[controls]` section of the generated `shell.toml`, so hover/focus/selected chrome in the bar and menus lights up. |
| `icons.theme` | GTK icon theme to pair with it. |
| `backgrounds/` | Wallpapers, cycled with `omarchy theme bg next`. |
| `tools/` | Regenerates `backgrounds/` from vector primitives. |

## Palette

| Role | Colour | |
|------|--------|--|
| accent / cyan | `#5ee7ff` | the Grid |
| orange | `#ff9f1c` | Clu |
| background | `#050b0f` | |
| foreground | `#d6f4fc` | |
| red | `#ff4d6d` | |
| yellow | `#ffc93c` | |
| green | `#3ff0a0` | |
| blue | `#3aa9ff` | |
| magenta | `#b06dff` | |

Active window borders run a 45° cyan-to-orange gradient at full alpha; inactive
ones fall back to a dim `#11384a`.

## Glow

Hyprland has no glow primitive, so `hyprland.lua` builds one out of the drop
shadow: `range = 44` with `render_power = 2` (a slower falloff than the default
3) spreads accent cyan off the window edge instead of hugging it, and
`color_inactive` is fully transparent so only the focused window carries it.
Unfocused windows are dimmed 20% on top of that.

**This needs gaps and borders to be visible.** Omarchy's `window-no-gaps`
toggle sets `gaps_out`, `gaps_in`, and `border_size` to 0, and it loads after
the theme, so it wins — the halo has nowhere to render and the gradient border
has no width. Turn it off with `SUPER + SHIFT + BACKSPACE`, or:

```bash
omarchy-hyprland-toggle window-no-gaps off
```

In the shell, hover is cyan at 75% border alpha and keyboard/tab focus goes one
louder — 2px, fully opaque `#8df2ff`. Popups, notifications, and the lock input
already track the Hyprland active-border gradient, so they pick up the
cyan-to-orange edge for free.

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
