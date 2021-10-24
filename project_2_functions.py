def extract_url(bad_url):
    # Extract a part of the url that works from a bad url
    # /url?q=[https://www.forbes.com/sites/bernardmarr/2019/06/03/5-amazing-examples-of-natural-language-processing-nlp-in-practice/]&sa=U&ved=2ahUKEwjEtaihyeHzAhXOYisKHQOzDkkQFnoECAgQAg&usg=AOvVaw2IaniwIYEofrmlXKj_Hgb_
    # Extract the one in the square bracket

    # Find the index of h in https
    http_index = bad_url.find('https://')

    # find the index of the first & in the bad link
    and_index = bad_url.find('&')

    # extract the substring
    return bad_url[http_index:and_index]
