import re
import xml.etree.ElementTree as ET

from lxml import etree

text = """Welcome to the Regex Training Center! Let's start with some dates:
01/02/2021, 12-25-2020, 2021.03.15, 2022/04/30, 2023.06.20, and 2021.07.04. You can
also find dates with words: March 14, 2022, and December 25, 2020.

Now let's move on to some phone numbers:
(123) 456-7890, +1-800-555-1234, 800.555.1234, 800-555-1234, and 123.456.7890.
Other formats include international numbers: +44 20 7946 0958, +91 98765 43210.

Here are some email addresses to find:
[john.doe@example.com](mailto:john.doe@example.com), [jane_doe123@domain.org](mailto:jane_doe123@domain.org), [support@service.net](mailto:support@service.net), [info@company.co.uk](mailto:info@company.co.uk),
and [contact.us@my-website.com](mailto:contact.us@my-website.com). You might also find these tricky: [weird.address+spam@gmail.com](mailto:weird.address+spam@gmail.com),
"quotes.included@funny.domain", and [this.one.with.periods@weird.co.in](mailto:this.one.with.periods@weird.co.in).

Need some URLs to extract? Try these:
[http://example.com](http://example.com/), [https://secure.website.org](https://secure.website.org/), [http://sub.domain.co](http://sub.domain.co/),
[www.redirect.com](http://www.redirect.com/), and [ftp://ftp.downloads.com](ftp://ftp.downloads.com/). Don't forget paths and parameters:
https://my.site.com/path/to/resource?param1=value1&param2=value2,
http://www.files.net/files.zip, https://example.co.in/api/v1/resource, and
https://another-site.org/downloads?query=search#anchor.

Hexadecimal numbers appear in various contexts:
0x1A3F, 0xBEEF, 0xDEADBEEF, 0x123456789ABCDEF, 0xA1B2C3, and 0x0. You might also find these:
#FF5733, #C70039, #900C3F, #581845, #DAF7A6, and #FFC300. RGB color codes can be tricky:
rgb(255, 99, 71), rgba(255, 99, 71, 1).

For those interested in Social Security numbers, here's some data:
123-45-6789, 987-65-4321, 111-22-3333, 555-66-7777, and 999-88-7777. Note that Social
Security numbers might also be written like 123 45 6789 or 123456789.

Let's throw in some random sentences for good measure:

- The quick brown fox jumps over the lazy dog.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- Jack and Jill went up the hill to fetch a pail of water.
- She sells seashells by the seashore.

Finally, let's include some special characters and numbers:
1234567890, !@#$%^&*()_+-=[]{}|;':",./<>?, 3.14159, 42, and -273.15.

That's it! I hope you find this useful for your regex training."""


def use_re():
    print("Function use_re is running.")  # Відладочний текст
    #dates = re.findall(r'(\d{4}(\.|\/)\d{2}(\.|\/)\d{2})', text)
    dates = re.findall(r'\d{4}(?:[.\-/])\d{2}(?:[.\-/])\d{2}', text)
    #print(dates)
    print("Extracted dates:", dates)

    if __name__ == "__main__":
        use_re()


    pattern = r'rgba\(\d{1,3},\s{0,1}\d{1,3},\s?\d{1,3},\s?([0-9\.]+)\)'
    search = re.search(pattern, text)
    color = search.group(0)
    transparent = search.group(1)
    print('color is:', color, ' transparent is:', transparent)


xml = r"""<?xml version="1.0"?>
<data>
    <info>
        <fact>When a cat drinks, its tongue - which has tiny barbs on it - scoops the liquid up backwards.</fact>
        <length>92</length>
    </info>
    <info>
        <fact>Cats spend nearly 1\/3 of their waking hours cleaning themselves.</fact>
        <length attr="value">64</length>
    </info>
    <info>
        <fact>When a cat drinks, its tongue - which has tiny barbs on it - scoops the liquid up backwards.</fact>
        <length>92</length>
    </info>
    <info>
        <fact>When a cat drinks, its tongue - which has tiny barbs on it - scoops the liquid up backwards.</fact>
        <length>92</length>
    </info>
    <info>
        <fact>When a cat drinks, its tongue - which has tiny barbs on it - scoops the liquid up backwards.</fact>
        <length>92</length>
    </info>
</data>"""


def parse_xml():
    root = ET.fromstring(xml)

    facts = root.findall('.//fact')
    facts = [fact.text for fact in facts]
    # print(facts)

    facts = root.findall('.//info[@number="2"]/fact')
    facts = [fact.text for fact in facts]
    # print(facts)

    info = root.findall('.//length')
    info = [i.text for i in info]
    # print(info)

    info = root.findall('.//length[@attr="value"]/../fact')
    info = [i.text for i in info]
    # print(info)


html = """<html>
    <head>
        <title>My page</title>
    </head>
    <body>
        <h2>Welcome to my <a href="#">next page</a></h2>
        <p>This is the first paragraph</p>.
        <p>This is the second paragraph</p>.
        <!-- this is the end -->
    </body>
</html>"""


def parse_html():
    tree = etree.HTML(html)

    xpath = '//h2/a'

    tag_a = tree.xpath(xpath)

    print(tag_a[0].text)


if __name__ == '__main__':
    # use_re()
    # parse_xml()
    parse_html()

