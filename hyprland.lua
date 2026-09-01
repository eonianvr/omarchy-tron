-- Tron wants the focused window to look powered on, so this file goes past the
-- border colors Omarchy would generate from colors.toml on its own.
--
-- Hyprland has no glow primitive. What it has is a drop shadow whose color and
-- falloff are ours to pick, so a wide, offset-less, low-power shadow in accent
-- cyan reads as a halo bleeding off the window edge. color_inactive is fully
-- transparent, which means only the focused window carries it.

local active_border_color = { colors = { "rgba(7df4ffff)", "rgba(ff9f1cff)" }, angle = 45 }
local inactive_border_color = "rgba(11384aaa)"

hl.config({
  general = {
    -- Thick enough for the gradient to actually be legible as a gradient.
    border_size = 3,

    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },

  decoration = {
    -- range is how far the halo reaches. Hyprland's default render_power of 3
    -- falls off fast enough to keep the light on the frame instead of washing
    -- into the window, which matters here: with no gaps between windows the
    -- shadow has nowhere outside to go and bleeds inward over the content.
    shadow = {
      enabled = true,
      range = 26,
      render_power = 3,
      sharp = false,
      scale = 1.0,
      color = "rgba(5ee7ff48)",
      color_inactive = "rgba(00000000)",
    },

    -- Unfocused windows fall back into the Grid so the lit one stands out.
    dim_inactive = true,
    dim_strength = 0.14,
  },

  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },

    groupbar = {
      text_color = "rgb(eafcff)",
      text_color_inactive = "rgba(a9dced90)",
      indicator_height = 3,
      col = {
        active = "rgba(5ee7ff40)",
        inactive = "rgba(0a1f2a30)",
      },
    },
  },
})
