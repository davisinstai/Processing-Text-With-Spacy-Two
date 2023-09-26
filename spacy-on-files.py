# import glob in case user enters a file pattern

# import zipfile in case user enters a zipfile

# import spacy for nlp

# import re so we can fix up some things in the texts


# make a dictionary called 'corpus'


# initialize spacy with model 'en_core_web_sm'


# try to do this
try:
    # ask the user to input a zip file or pattern
    pattern = 
    # if pattern ends with '.zip'
    if ...
        # make a ZipFile of pattern
        zipf = zipfile.ZipFile(pattern)
        # for each file_name in the zip file
        for file_name in zipf.namelist():
            # print file_name

            # open file_name as f; refer to the notebook!
            with ... f:
                # get all the text
                text = ''.join([x.decode('utf-8') for x in f.readlines()])
                # run spacy on the text; put the result in the 'corpus' dictionary using file_name as the key

    else: # pattern doesn't end with '.zip'
        # get everything matching file_name using glob; refer to the notebook!
        for file_name in glob.glob(pattern):
            # print file_name

            # open file_name as f
            with ... f:
                # get all the text
                text = ''.join(f.readlines())
                # run spacy on the text; put the result in the 'corpus' dictionary using file_name as the key

# if it doesn't work, say why
except Exception as e:
    print(e)

# keep going til the user quits with Ctrl-C
while True:
    # print the corpus keys

    # set the document name to something that doesn't exist, like the empty string

    # until the document given by the user is in `corpus`
    while document not in corpus:
        # ask the user for a value for `document`

    # set the goal to something that doesn't exist, like the empty string

    # until the goal is 'doc', 'table' or 'statistics'
    while ...:
        # ask the user for a value for 'goal' from 'doc', 'table' or 'statistics'; don't forget to escape!

        # if the goal is 'doc'
        if ...:
            # define 'text' and set the title to be the document key (file name)
            text = '# ' + document + '\n\n'
            # walk over the tokens in the document

                # if the token is a noun, add it to 'text' and make it boldface (HTML: <b> at the start, </b> at the end)
                if :

                # otherwise, if it's a verb, add it to 'text' and make it italicized (HTML: <i> at the start, </i> at the end)
                elif :

                # otherwise, just add it to 'text'!
                else:

                # add any whitespace following the token using attribute whitespace_
                text = text + token.whitespace_
            # open an output file, named after the document with _text.md appended
            with open(document + '_text.md', 'w') as outf:
                # write 'text'

        # if the goal is 'table'
        elif ...:
            # Make the tokens table
            tokens_table = "| Tokens | Lemmas | Coarse | Fine | Shapes | Morphology |\n| ------ | ------ | ------ | ---- | ------ | ---------- | \n"
            # walk over the tokens in the document

                # if the token's part of speech is not 'SPACE'
                if :
                    # add the the text, lemma, coarse- and fine-grained parts of speech, word shape and morphology for this token to `tokens_table`; don't forget the newline character! refer to project 2a
                    tokens_table  = 
            # Make the entities table
            entities_table = "| Text | Type |\n| ---- | ---- |\n"
            # walk over the entities in the document
                # add the text and label for this entity to 'entities_table'; don't forget the newline character! refer to project 2a
                entities_table = 
            # open an output file, named after the document with _table.md appended
            with ...   outf:
                # write 'tokens_table'

                # write 'entities_table'

        #if the goal is 'statistics'
        elif ...:
            # make a dictionary for the statistics called 'stats'

            # walk over the tokens in the document
            for ...:
                # if the token's part of speech is not 'SPACE'
                if token.pos_ != 'SPACE':
                    # add the token and its part of speech tag ('pos_') to 'stats' (check if it is in 'stats' first!)
                    if token.text + token.pos_ not in stats:
                        
                    # increment its count

            # walk over the entities in the document
            for ...:
                # add the entity and its label ('label_') to 'stat's (check if it is in 'stat's first!)
                if entity.text + entity.label_ not in stats:
                    
                # increment its count
                
            # open an output file, named after the document with _stats.md appended
            with ... outf:
                # write the header for a table of tokens/entities and counts
                outf.write('| Token/Entity | Count |\n | ------------ | ----- |\n')
                # print the key and count for each entry in 'stats'
                for key in sorted(stats.keys()):
                    # print the key and the count
                    
