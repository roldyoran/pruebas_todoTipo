from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('a.jpg')
my_art.to_file('tania.txt', columns=60, monochrome=True)
my_art.to_html_file('ascii_art.html', columns=49, width_ratio=2)

