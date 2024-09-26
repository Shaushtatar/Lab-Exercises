This wrapper includes some functions for searching through the https://dictionaryapi.dev/ dictionary API.

The first function, getjson(), gets the word desired through input, and converts it to a URL.

The functions pertaining to definition, pronunciation, and examples all work rather similarly.
Because definition and examples are in the same dictionary, their code is nearly identical. 
Both send a for loop through the elements of "meanings", which separates between different word types.
Then, inside each word type, it goes through each definition.
The only difference is that for definition, it takes the definition key, which always exists.
But for example, it has to make sure there exists an example key. For some, it doesn't exist. 
This would cause a KeyError which would activate the except clause.

The pronunciation function works similarly but requires a different path.
It only needs one for loop, through the pronunciations list.
However, like examples, it needs to make sure a text key actually exists for each pronunciation.

The final function is quite straightforward, simply getting the wiktionary page for a word. 