# Alfred Snippets

For a long time I was using [aText](https://www.trankynam.com/atext/) for inserting snippets into documents. Unfortunately, aText becomes more and more outdated. But: [Alfred](https://www.alfredapp.com/) has [great snippet support](https://www.alfredapp.com/help/features/snippets/) in version 3.

Here's my collection of Alfred 3 snippets and also a script to convert aText snippets to Alfred snippets.

## Conversion Script

`convert-aText-to-Alfred.py` will take an aText-exported `.csv` file and create a `.alfredsnippets` file from it.

The aText `.csv` is a simple comma-separated list of `keyword,entry,[name]` form; so the conversion script can also be used to convert an arbitrary `.csv` file into a collection of Alfred snippets.

The only non-standard Python package used is [*Click*](http://click.pocoo.org/), which is awesome.  
`pip install click` it!

The script is somewhat general, but mainly tailored to my needs. If you want to extend it, feel free to file a pull request or enhancement report.

## Snippets

Coming up!
