"""Generate cover.jpg for 2017-10-15 protobuf/gRPC article.
Style: deep blue to indigo gradient + binary stream accent + title.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = r"D:\workspace\github\my-blog\content\post\网络\2017-10-15\image\cover.jpg"
FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FONT_PATH_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"

# 1600x900 (16:9)
W, H = 1600, 900

# Theme: network category badge #1d3557 + indigo/violet (proto3 binary)
TOP_COLOR = (29, 53, 87)        # #1d3557 deep blue (网络分类色)
MID_COLOR = (48, 71, 142)       # #30478e indigo
BOTTOM_COLOR = (90, 50, 138)    # #5a328a violet (暗示二进制 / proto3)


def hex_to_rgb(hex_str):
    return tuple(int(hex_str[i:i+2], 16) for i in (1, 3, 5))


def make_gradient(top, mid, bottom):
    """3-stop vertical gradient."""
    img = Image.new("RGB", (W, H), top)
    draw = ImageDraw.Draw(img)
    half = H // 2
    for y in range(half):
        ratio = y / half
        r = int(top[0] * (1 - ratio) + mid[0] * ratio)
        g = int(top[1] * (1 - ratio) + mid[1] * ratio)
        b = int(top[2] * (1 - ratio) + mid[2] * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    for y in range(half, H):
        ratio = (y - half) / (H - half)
        r = int(mid[0] * (1 - ratio) + bottom[0] * ratio)
        g = int(mid[1] * (1 - ratio) + bottom[1] * ratio)
        b = int(mid[2] * (1 - ratio) + bottom[2] * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    return img


def add_binary_pattern(img):
    """Subtle scattered 'bits' to suggest binary / proto3 wire format."""
    import random
    random.seed(42)
    draw = ImageDraw.Draw(img, "RGBA")
    for _ in range(420):
        x = random.randint(0, W)
        y = random.randint(0, H)
        size = random.choice([2, 2, 3, 4])
        opacity = random.randint(30, 90)
        draw.rectangle([x, y, x + size, y + size], fill=(180, 220, 255, opacity))


def add_title(img, title, subtitle, date_str):
    draw = ImageDraw.Draw(img)
    try:
        title_font = ImageFont.truetype(FONT_PATH_BOLD, 86)
    except Exception:
        title_font = ImageFont.truetype(FONT_PATH, 86)
    try:
        sub_font = ImageFont.truetype(FONT_PATH, 34)
    except Exception:
        sub_font = ImageFont.truetype(FONT_PATH, 34)
    try:
        date_font = ImageFont.truetype(FONT_PATH, 28)
    except Exception:
        date_font = ImageFont.truetype(FONT_PATH, 28)

    # Title - centered, with subtle shadow
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    title_h = title_bbox[3] - title_bbox[1]
    title_x = (W - title_w) // 2
    title_y = H // 2 - title_h - 40

    for offset in [(3, 3), (-3, 3), (3, -3), (-3, -3)]:
        draw.text((title_x + offset[0], title_y + offset[1]), title,
                  font=title_font, fill=(0, 0, 0, 100))
    draw.text((title_x, title_y), title, font=title_font, fill=(245, 250, 255))

    # Subtitle
    sub_bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
    sub_w = sub_bbox[2] - sub_bbox[0]
    sub_x = (W - sub_w) // 2
    sub_y = title_y + title_h + 30
    draw.text((sub_x, sub_y), subtitle, font=sub_font, fill=(200, 220, 240))

    # Date - bottom right
    date_bbox = draw.textbbox((0, 0), date_str, font=date_font)
    date_w = date_bbox[2] - date_bbox[0]
    date_x = W - date_w - 60
    date_y = H - 60
    draw.text((date_x, date_y), date_str, font=date_font, fill=(200, 220, 240))


def add_decoration(img):
    draw = ImageDraw.Draw(img, "RGBA")
    # Decorative line below title area
    line_y = H // 2 + 60
    line_w = 220
    line_x_start = (W - line_w) // 2
    draw.rectangle([line_x_start, line_y, line_x_start + line_w, line_y + 3],
                   fill=(255, 255, 255, 200))
    # Top-left corner accent
    draw.rectangle([0, 0, 220, 8], fill=(255, 255, 255, 100))
    # Bottom-right corner accent
    draw.rectangle([W - 220, H - 8, W, H], fill=(255, 255, 255, 100))


def main():
    img = make_gradient(TOP_COLOR, MID_COLOR, BOTTOM_COLOR)
    add_binary_pattern(img)
    add_decoration(img)
    add_title(
        img,
        title="ProtoBuf & gRPC",
        subtitle="proto3 时代的跨语言 RPC 实战",
        date_str="2017-10-15",
    )
    img.save(OUT, "JPEG", quality=88)
    print(f"saved: {OUT}")


if __name__ == "__main__":
    main()
