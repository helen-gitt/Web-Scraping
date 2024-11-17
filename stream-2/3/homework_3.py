import re

text = """Welcome to the Regex Training Center! 

01/02/2021, 12-25-2020, 2021.03.15, 2022/04/30, 2023.06.20, and 2021.07.04. You can
also find dates with words: March 14, 2022, and December 25, 2020. 

(123) 456-7890, +1-800-555-1234, 800.555.1234, 800-555-1234, and 123.456.7890. 
Other formats include international numbers: +44 20 7946 0958, +91 98765 43210.

john.doe@example.com, jane_doe123@domain.org, support@service.net, info@company.co.uk, 
and contact.us@my-website.com. You might also find these tricky: weird.address+spam@gmail.com,
"quotes.included@funny.domain", and this.one.with.periods@weird.co.in.

http://example.com, https://secure.website.org, http://sub.domain.co, 
www.redirect.com, and ftp://ftp.downloads.com. Don't forget paths and parameters:
https://my.site.com/path/to/resource?param1=value1&param2=value2, 
http://www.files.net/files.zip, https://example.co.in/api/v1/resource, and 
https://another-site.org/downloads?query=search#anchor. 

0x1A3F, 0xBEEF, 0xDEADBEEF, 0x123456789ABCDEF, 0xA1B2C3, and 0x0. 

#FF5733, #C70039, #900C3F, #581845, #DAF7A6, and #FFC300. RGB color codes can be tricky: 
rgb(255, 99, 71), rgba(255, 99, 71, 0.5).

123-45-6789, 987-65-4321, 111-22-3333, 555-66-7777, and 999-88-7777. Note that Social 
Security numbers might also be written like 123 45 6789 or 123456789.

1234567890, !@#$%^&*()_+-=[]{}|;':",./<>?, 3.14159, 42, and -273.15."""

#dates
def find_dates(text):
    date_pattern = r'\b((?:\d{2}[-/]\d{2}[-/]\d{4})|(?:\d{4}[-./]\d{2}[-./]\d{2})|(?:[A-Za-z]+\s\d{1,2},\s\d{4}))\b'
    dates = re.findall(date_pattern, text)
    return dates

#phone_numbers
def find_phone_numbers(text):
    local_numbers = [
        phone for phone in re.findall(
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            text
        )
        if not re.match(r'^\d{10}$', phone)
    ]
    international_numbers = re.findall(r'\+44\s\d{2}\s\d{4}\s\d{4}|\+91\s\d{5}\s\d{5}', text)
    return local_numbers + international_numbers

#email
def find_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

#URL
def find_urls(text):
    url_pattern = r'(https?|ftp)://[^\s/$.?#].[^\s]*|www\.[^\s/$.?#].[^\s]*'
    urls = re.findall(url_pattern, text)
    return urls

#hex_values
def find_hex(text):
    hex_pattern = r'0x[0-9A-Fa-f]+|#[0-9A-Fa-f]{6}'
    hex_values = re.findall(hex_pattern, text)
    return hex_values

#rgb_colors
def find_colors(text):
    color_pattern = r'(?:rgb|rgba)\(\d{1,3},\s*\d{1,3},\s*\d{1,3}(?:,\s*(?:0|0?\.\d+|1))?\)'
    colors = re.findall(color_pattern, text)
    return colors

#security_numbers
def find_ssn(text):
    ssn_pattern = r'\b\d{3}[- ]?\d{2}[- ]?\d{4}\b'
    ssn_numbers = re.findall(ssn_pattern, text)
    return ssn_numbers

if __name__ == '__main__':
    print("Dates found:", find_dates(text))
    print("Phone numbers found:", find_phone_numbers(text))
    print("Emails found:", find_emails(text))
    print("URLs found:", find_urls(text))
    print("HEX values found:", find_hex(text))
    print("Colors found:", find_colors(text))
    print("SSN found:", find_ssn(text))


#### XPath

    from lxml import html

    # Input для введення пошукового запиту
    search_input_xpath = "//input[@id='text-input-what']"

    # Input для введення регіону
    search_region_xpath = "//input[@id='text-input-where']"

    # Кнопка пошуку
    search_button_xpath = "//button[@class='yosegi-InlineWhatWhere-primaryButton']"




