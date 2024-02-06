def store_result(headline, content, link):
    """stores data in a text file

    Args:
        headline_text (_type_): Headline
        body_text (_type_): content of the news
        url (_type_): Link to that article
    """
    with open('output.txt', 'a', encoding='utf-8') as op:
        op.write("===" * 100 + '\n')
        op.write(f'Headline: {headline}\n')
        op.write(f'Body: {content}\n')
        op.write(f'Link: {link}\n')
        op.write('\n')
