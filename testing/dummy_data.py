# contains dummy scrapy item for testing purposes.

from scraping.rulings import RulingItem

# case_incomplete: for testing a simple keyword extraction in the case where a ruling does not contain all 3 chapters
case_incomplete = {'input_item': RulingItem(), 'expected_output': RulingItem()}
case_incomplete['input_item']['core_issue'] = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam ' \
                                              'nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, ' \
                                              'sed diam voluptua. At vero eos et accusam et justo duo dolores et ea ' \
                                              'rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ' \
                                              'ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur ' \
                                              'sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et ' \
                                              'dolore magna aliquyam erat, sed Abkommen. At vero eos et accusam et ' \
                                              'justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea ' \
                                              'takimata sanctus est Lorem ipsum dolor sit amet.'
case_incomplete['input_item']['paragraph'] = 'The chapter \'paragraph\' does not contain any keyword.'

case_incomplete['expected_output']['international_treaties'] = {
    'contexts': [{
        'chapter': 'core_issue',
        'keyword': 'sed Abkommen',
        'sentence': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt '
                    'ut labore et dolore magna aliquyam erat, sed Abkommen.'
    }],
    'keywords': {'sed Abkommen': 1}
}

# case_keyword_completeness: for testing if all expected keywords related with international treaties are extracted.
case_completeness_int_treaties = {'input_item': RulingItem(), 'expected_output': RulingItem()}
case_completeness_int_treaties['input_item']['core_issue'] = '''
    Völkerrechtliches Abkommen
    Völkerrechtliche Abkommen
    Völkerrechtlichen Abkommen
    Völkerrechtlichen Abkommens
    Völkerrechtlicher Abkommen
    Internationales Abkommen
    Internationale Abkommen
    Internationalen Abkommen
    Internationalen Abkommens
    Internationaler Abkommen
    Völkerrechtliches Übereinkommen
    Völkerrechtliche Übereinkommen
    Völkerrechtlichen Übereinkommen
    Völkerrechtlichen Übereinkommens
    Völkerrechtlicher Übereinkommen
    Internationales Übereinkommen
    Internationale Übereinkommen
    Internationalen Übereinkommen
    Internationalen Übereinkommens
    Internationaler Übereinkommen
    Übereinkommen (potentially too broad?)
    Abkommen (potentially too broad?)
    Völkerrechtlicher Vertrag
    Völkerrechtlichen Vertrags
    Völkerrechtlichen Vertrages
    Völkerrechtlichen Vertrag
    Völkerrechtliche Verträge
    Völkerrechtlichen Verträge
    Völkerrechtlicher Verträge
    Internationaler Vertrag
    Internationalen Vertrags
    Internationalen Vertrages
    Internationalen Vertrag
    Internationale Verträge
    Internationalen Verträge
    Internationaler Verträge
    Internationaler Pakt
    Internationalen Pakts
    Internationalen Paktes
    Internationalen Pakt
    Internationale Pakte
    Internationalen Pakte
    Internationaler Pakte
    Völkerrechtlicher Pakt
    Völkerrechtlichen Pakts
    Völkerrechtlichen Paktes
    Völkerrechtlichen Pakt
    Völkerrechtliche Pakte
    Völkerrechtlichen Pakte
    Völkerrechtlicher Pakte
    Pakt (too broad?)
    Pakte (idem)
    Pakts (idem)
    Traité international
    Traités internationaux
    Traité
    Traités
    Accord international
    Accords internationaux
    Accord (probably too broad)
    Convention internationale
    Conventions internationales
    Convention (too broad)
    Conventions (idem)
    Contrat international
    Contrats internationaux
    Pacte international
    Pactes internationaux
    Pacte (too broad?)
    Trattato internazionale
    Trattati internazionali
    Trattato di stato
    Trattati di stato
    Convenzione internazionale
    Convenzioni internazionali
    Accordo internazionale
    Accordi internazionali
    Patto internazionale
    Patti internazionali
    Patto (probably too broad)
    Patti
Update 25.11.16:
    Internationales Vertragsrecht
    Internationale Vertragsrecht
    Internationalen Vertragesrecht
    Internationalen Vertragsrechts
    Internationalem Vertragsrecht
Updatevorschläge Nicolas
    Staatsvertrag
    Staatsverträge
    Staatsvertrags
    Staatsvertrages
    Doppelbesteuerungsabkommen (Bsp für einen bestimmten Vertrag)
    Doppelbesteuerungsabkommens
    convenzione sulla doppia imposizione
    patto di non aggressione
'''
case_completeness_int_treaties['expected_output'] = [
    'Völkerrechtliches Abkommen', 'Völkerrechtliche Abkommen', 'Völkerrechtlichen Abkommen',
    'Völkerrechtlichen Abkommens', 'Völkerrechtlicher Abkommen', 'Internationales Abkommen', 'Internationale Abkommen',
    'Internationalen Abkommen', 'Internationalen Abkommens', 'Internationaler Abkommen',
    'Völkerrechtliches Übereinkommen', 'Völkerrechtliche Übereinkommen', 'Völkerrechtlichen Übereinkommen',
    'Völkerrechtlichen Übereinkommens', 'Völkerrechtlicher Übereinkommen', 'Internationales Übereinkommen',
    'Internationale Übereinkommen', 'Internationalen Übereinkommen', 'Internationalen Übereinkommens',
    'Internationaler Übereinkommen', 'Übereinkommen', 'Abkommen',
    'Völkerrechtlicher Vertrag', 'Völkerrechtlichen Vertrags', 'Völkerrechtlichen Vertrages',
    'Völkerrechtlichen Vertrag', 'Völkerrechtliche Verträge', 'Völkerrechtlichen Verträge',
    'Völkerrechtlicher Verträge', 'Internationaler Vertrag', 'Internationalen Vertrags', 'Internationalen Vertrages',
    'Internationalen Vertrag', 'Internationale Verträge', 'Internationalen Verträge', 'Internationaler Verträge',
    'Internationaler Pakt', 'Internationalen Pakts', 'Internationalen Paktes', 'Internationalen Pakt',
    'Internationale Pakte', 'Internationalen Pakte', 'Internationaler Pakte', 'Völkerrechtlicher Pakt',
    'Völkerrechtlichen Pakts', 'Völkerrechtlichen Paktes', 'Völkerrechtlichen Pakt', 'Völkerrechtliche Pakte',
    'Völkerrechtlichen Pakte', 'Völkerrechtlicher Pakte', 'Pakt', 'Pakte', 'Pakts',
    'Traité international', 'Traités internationaux', 'Traité', 'Traités', 'Accord international',
    'Accords internationaux', 'Accord', 'Convention internationale', 'Conventions internationales',
    'Convention', 'Conventions', 'Contrat international', 'Contrats internationaux',
    'Pacte international', 'Pactes internationaux', 'Pacte', 'Trattato internazionale',
    'Trattati internazionali', 'Trattato di stato', 'Trattati di stato', 'Convenzione internazionale',
    'Convenzioni internazionali', 'Accordo internazionale', 'Accordi internazionali', 'Patto internazionale',
    'Patti internazionali', 'Patto', 'Patti', 'Internationales Vertragsrecht', 'Internationale Vertragsrecht',
    'Internationalen Vertragesrecht', 'Internationalen Vertragsrechts', 'Internationalem Vertragsrecht',
    'Staatsvertrag', 'Staatsverträge', 'Staatsvertrags', 'Staatsvertrages', 'Doppelbesteuerungsabkommen',
    'Doppelbesteuerungsabkommens', 'convenzione sulla doppia', 'patto di non'
]

# keyword_completeness: for testing if all expected keywords related with international customary law are extracted.
case_completeness_customary_int_law = {'input_item': RulingItem(), 'expected_output': RulingItem()}
case_completeness_customary_int_law['input_item']['core_issue'] = '''
    Droit international coutumier
    Droit coutumier international
    Coutumier (too broad)
    Coutume internationale
    Völkergewohnheitsrecht
    Völkergewohnheitsrechts
    internationales Gewohnheitsrecht
    internationale Gewohnheitsrecht
    internationalen Gewohnheitsrecht
    internationalen Gewohnheitsrechts
    internationalem Gewohnheitsrecht
    völkerrechtliches Gewohnheitsrecht
    völkerrechtliche Gewohnheitsrecht
    völkerrechtlichen Gewohnheitsrechts
    völkerrechtlichem Gewohnheitsrecht
    gewohnheitsrechtliches Völkerrecht
    gewohnheitsrechtliche Völkerrecht
    gewohnheitsrechtlichen Völkerrecht
    gewohnheitsrechtlichen Völkerrechts
    gewohnheitsrechtlichem Völkerrecht
    gewohnheitsrechtlich (too broad)
    ius gentium
    droit des gens (too broad, I think, judging from a past research project)
    opinio juris
    opinio iuris
    diritto consuetudinario
    diritto internazionale consuetudinario
    diritto consuetudinario internazionale
    consuetudinario (too broad)
    consuetudine internazionale
'''
case_completeness_customary_int_law['expected_output'] = [
    'Droit international coutumier', 'Droit coutumier international', 'Coutumier', 'Coutume internationale',
    'Völkergewohnheitsrecht', 'Völkergewohnheitsrechts', 'internationales Gewohnheitsrecht',
    'internationale Gewohnheitsrecht', 'internationalen Gewohnheitsrecht', 'internationalen Gewohnheitsrechts',
    'internationalem Gewohnheitsrecht', 'völkerrechtliches Gewohnheitsrecht', 'völkerrechtliche Gewohnheitsrecht',
    'völkerrechtlichen Gewohnheitsrechts', 'völkerrechtlichem Gewohnheitsrecht', 'gewohnheitsrechtliches Völkerrecht',
    'gewohnheitsrechtliche Völkerrecht', 'gewohnheitsrechtlichen Völkerrecht', 'gewohnheitsrechtlichen Völkerrechts',
    'gewohnheitsrechtlichem Völkerrecht', 'gewohnheitsrechtlich', 'ius gentium', 'droit des gens', 'opinio juris',
    'opinio iuris', 'diritto consuetudinario', 'diritto internazionale consuetudinario',
    'diritto consuetudinario internazionale', 'consuetudinario', 'consuetudine internazionale'
]

# keyword completeness: for testing if all expected keywords related with international law in general are extracted.
case_completeness_int_law_in_general = {'input_item': RulingItem(), 'expected_output': RulingItem()}
case_completeness_int_law_in_general['input_item']['core_issue'] = '''
    Völkerrecht
    Völkerrechts
    Völkerrechtlich
    Völkerrechtliche
    Völkerrechtlichen
    Völkerrechtliches
    Internationales Recht
    Internationale Recht
    Internationalen Rechts
    Internationalem Recht
    Droit international
    Droit international public
    Droit international privé
    Droits internationaux
    Diritto internazionale
    Diritto internazionale pubblico
    Diritto internazionale private
    Diritti internazionali
'''
case_completeness_int_law_in_general['expected_output'] = [
    'Völkerrecht', 'Völkerrechts', 'Völkerrechtlich', 'Völkerrechtliche', 'Völkerrechtlichen', 'Völkerrechtliches',
    'Internationales Recht', 'Internationale Recht', 'Internationalen Rechts', 'Internationalem Recht',
    'Droit international', 'Droit international public', 'Droit international privé', 'Droits internationaux',
    'Diritto internazionale', 'Diritto internazionale pubblico', 'Diritto internazionale private',
    'Diritti internazionali'
]

title_of_judgement_examples = """
88. Auszug aus dem Urteil der Schuldbetreibungs- und Konkurskammer vom 18. November 1998 i.S. F. (Beschwerde)
46. Auszug aus dem Urteil der I. Zivilabteilung vom 6. Mai 1998 i.S. X. gegen Y. GmbH (Berufung)
23. Auszug aus dem Urteil des Kassationshofes i.S. X. gegen Staatsanwaltschaft des Kantons Zürich und Y.
14. Auszug aus dem Urteil der Schuldbetreibungs- und Konkurskammer vom 27. Januar 1988 i.S. B. (Rekurs) (Nichtigkeitsbeschwerde)
6S.681/2001 vom 2. Juli 2002
1. Extrait de l'arrêt de la IIe Cour de droit public dans la cause X. contre Service de la population du canton de Vaud (recours en matière de droit public)
2C_460/2009 du 4 novembre 2009
7. Auszug aus dem Urteil der II. öffentlich-rechtlichen Abteilung i.S. A. und Mitb. gegen Sicherheitsdirektion und Regierungsrat des Kantons Zürich (Beschwerde in öffentlich-rechtlichen Angelegenheiten)
2C_269/2009 vom 5. Januar 2010
10. Auszug aus dem Entscheid der Schuldbetreibungs- und Konkurskammer vom 15. Januar 1988 i.S. V. (Rekurs)
52. Auszug aus dem Urteil vom 26. Oktober 2000 i.S. S. gegen VERA Sammelstiftung in Liquidation, Olten, und Verwaltungsgericht des Kantons Bern




89. Extrait de l'arrêt de la Ire Cour civile du 13 novembre 1998 dans la cause Banque Audi (Suisse) S.A. contre Volkswagen Bank GmbH (recours en réforme)
9. Arrêt de la Cour de cassation pénale dans la cause Union Démocratique du Centre du Canton de Genève contre Procureur général du canton de Genève (pourvoi en nullité)
6S.625/2001 du 4 décembre 2001
13. Extrait de l'arrêt de la Chambre des poursuites et des faillites du 15 février 1988 dans la cause F. (recours LP)
51. Extrait de l'arrêt du 26 septembre 2000 dans la cause I. contre 1. Fondation collective LPP de la Ticino Vie, 2. Fondation institution supplétive LPP et Tribunal des assurances du canton de Vaud
32. Arrêt de la Ire Cour de droit social dans la cause T. contre Corps de Police de la République et canton de Genève (recours constitutionnel subsidiaire)
8D_8/2009 du 16 août 2010




11. Estratto della sentenza 10 giugno 1988 della Camera delle esecuzioni e dei fallimenti nella causa X. contro Y. e Ufficio esecuzione e fallimenti di Lugano (ricorso)
68. Estratto della sentenza 4 dicembre 1974 della Corte di Cassazione penale nella causa X e Y contro Procuratore pubblico sottocenerino.
73. Sentenza 11 novembre 1955 della II Corte civile nella causa Intervisa SA e Visafin SA contro Visa SA, in liquidazione concordataria.
"""