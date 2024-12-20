from natasha import (
    Segmenter,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    
    Doc
)

text = 'Специалисты собрали более трех тысяч тонн загрязненного песка с кубанского берега после крушения танкеров с нефтепродуктами, сообщили в пресс-службе МЧС.'

segmenter = Segmenter()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

doc = Doc(text)
doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)

sent = doc.sents[0]
sent.morph.print()
sent.syntax.print()
        